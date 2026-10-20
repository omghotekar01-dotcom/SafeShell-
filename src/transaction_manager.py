"""Transaction Manager Module."""

import time
from typing import Optional


class TransactionManager:
    """Tracks placeholder transaction identifiers in memory; no snapshots are created."""

    def __init__(self, snapshot_dir: str = "/snapshots"):
        self.snapshot_dir = snapshot_dir
        self.current_snapshot: Optional[str] = None

    def begin_transaction(self) -> str:
        """Create an in-memory transaction identifier for the demonstration."""
        snapshot_id = f"snapshot_{int(time.time())}"
        self.current_snapshot = snapshot_id
        print(f"[TransactionManager] Snapshot created: {snapshot_id}")
        return snapshot_id

    def commit(self):
        """Clear the in-memory transaction marker without executing changes."""
        if self.current_snapshot:
            print(f"[TransactionManager] Committed transaction {self.current_snapshot}")
            self.current_snapshot = None
        else:
            print("[TransactionManager] No active transaction.")

    def rollback(self):
        """Clear the in-memory transaction marker; does not restore system state."""
        if self.current_snapshot:
            print(f"[TransactionManager] Rolling back to {self.current_snapshot}")
            self.current_snapshot = None
        else:
            print("[TransactionManager] No active transaction to rollback.")


if __name__ == "__main__":
    manager = TransactionManager()
    manager.begin_transaction()
    manager.rollback()
