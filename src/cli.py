"""SafeShell++ command line interface."""

import os
import sys
from typing import List

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from command_interceptor import CommandInterceptor
from impact_report import ImpactReport
from semantic_analyzer import SemanticAnalyzer
from simulator import SandboxSimulator
from transaction_manager import TransactionManager
from undo_plan_generator import UndoPlanGenerator


class SafeShellCLI:
    def __init__(self):
        self.interceptor = CommandInterceptor()
        self.analyzer = SemanticAnalyzer()
        self.simulator = SandboxSimulator()
        self.undo_gen = UndoPlanGenerator()
        self.txn_manager = TransactionManager()
        self.report_gen = ImpactReport()

    def run(self):
        """Read commands, analyse and simulate them, then ask for confirmation."""
        print("SafeShell++ is active. Type 'exit' to quit.")
        while True:
            try:
                user_input = input("safeshell> ")
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if user_input.strip().lower() in ["exit", "quit"]:
                break
            parts = self.interceptor.parse_command(user_input)
            if not parts:
                continue
            paths = self._extract_paths(parts)
            semantic_info = self.analyzer.analyze_paths(paths)
            changes = self.simulator.run_simulated(parts)
            undo_plan = self.undo_gen.generate_undo_plan(changes, semantic_info)
            print(self.report_gen.generate_report(changes, semantic_info, undo_plan))
            decision = input("Proceed? (proceed/archive/cancel): ").strip().lower()
            if decision in ["proceed", "archive"]:
                self.txn_manager.begin_transaction()
                print("Archiving files..." if decision == "archive" else "Executing command...")
                self.txn_manager.commit()
            else:
                print("Command cancelled.")

    def _extract_paths(self, parts: List[str]) -> List[str]:
        """Extract arguments that look like file paths."""
        return [arg for arg in parts[1:] if not arg.startswith("-") and ("/" in arg or os.path.exists(arg))]


if __name__ == "__main__":
    SafeShellCLI().run()
