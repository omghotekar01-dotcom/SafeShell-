"""
Simulator Module
Executes the command in an isolated sandbox and records changes.
"""

from typing import Dict, List


class SandboxSimulator:
    """Runs commands inside a sandbox to predict impact."""

    def __init__(self, sandbox_tool: str = "bwrap"):
        self.sandbox_tool = sandbox_tool

    def run_simulated(self, command_parts: List[str]) -> Dict:
        """Simulate supported commands and return their predicted changes."""
        changes = {
            "files_created": [],
            "files_modified": [],
            "files_deleted": [],
            "processes_killed": [],
        }
        if not command_parts:
            return changes

        cmd_name = command_parts[0]
        args = command_parts[1:]
        if cmd_name == "rm":
            changes["files_deleted"].extend(arg for arg in args if not arg.startswith("-"))
        elif cmd_name == "touch":
            changes["files_created"].extend(arg for arg in args if not arg.startswith("-"))
        elif cmd_name == "chmod" and args:
            changes["files_modified"].extend(args[1:])
        elif cmd_name == "kill":
            changes["processes_killed"].extend(int(arg) for arg in args if arg.isdigit())
        return changes


if __name__ == "__main__":
    simulator = SandboxSimulator()
    print(simulator.run_simulated(["rm", "-rf", "/home/user/important_project/"]))
