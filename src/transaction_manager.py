"""Transaction Manager Module."""

import time
from typing import Optional


class TransactionManager:
    """Creates system snapshots and allows commit or rollback."""

    def __init__(self, snapshot_dir: str = "/snapshots"):
        self.snapshot_dir = snapshot_dir
        self.current_snapshot: Optional[str] = None

    def begin_transaction(self) -> str:
        """Create a simulated filesystem snapshot and return its identifier."""
        snapshot_id = f"snapshot_{int(time.time())}"
        self.current_snapshot = snapshot_id
        print(f"[TransactionManager] Snapshot created: {snapshot_id}")
        return snapshot_id

    def commit(self):
        """Commit changes permanently."""
        if self.current_snapshot:
            print(f"[TransactionManager] Committed transaction {self.current_snapshot}")
            self.current_snapshot = None
        else:
            print("[TransactionManager] No active transaction.")

    def rollback(self):
        """Restore system state to the active snapshot."""
        if self.current_snapshot:
            print(f"[TransactionManager] Rolling back to {self.current_snapshot}")
            self.current_snapshot = None
        else:
            print("[TransactionManager] No active transaction to rollback.")


if __name__ == "__main__":
    manager = TransactionManager()
    manager.begin_transaction()
    manager.rollback()
