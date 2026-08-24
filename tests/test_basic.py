"""Basic tests for SafeShell++ modules."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from command_interceptor import CommandInterceptor
from impact_report import ImpactReport
from semantic_analyzer import SemanticAnalyzer
from simulator import SandboxSimulator
from transaction_manager import TransactionManager
from undo_plan_generator import UndoPlanGenerator


def test_interceptor():
    assert CommandInterceptor().parse_command("rm -rf /tmp/test") == ["rm", "-rf", "/tmp/test"]


def test_semantic_analyzer():
    result = SemanticAnalyzer().analyze_path("/etc/passwd")
    assert result["category"] == "system_config"
    assert result["importance"] > 0.8


def test_simulator():
    changes = SandboxSimulator().run_simulated(["rm", "-rf", "/home/user/file.txt"])
    assert "/home/user/file.txt" in changes["files_deleted"]


def test_undo_plan():
    plan = UndoPlanGenerator().generate_undo_plan(
        {"files_deleted": ["/home/user/file.txt"]},
        [{"path": "/home/user/file.txt", "importance": 0.9}],
    )
    assert plan["recommended_action"] in ["proceed", "archive"]


def test_transaction():
    manager = TransactionManager()
    manager.begin_transaction()
    manager.rollback()
    assert manager.current_snapshot is None


def test_impact_report():
    report = ImpactReport.generate_report(
        {"files_deleted": ["/tmp/cache.tmp"]},
        [],
        {"recommended_action": "proceed", "steps": []},
    )
    assert "SafeShell++ Impact Report" in report
