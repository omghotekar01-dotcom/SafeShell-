"""
Undo Plan Generator Module
Uses an LLM to create step-by-step rollback or archival plans.
"""

import json
from typing import Dict, List


class UndoPlanGenerator:
    """Generates undo plans based on changes and semantic importance."""

    def __init__(self, model_name: str = "tinyllama"):
        self.model_name = model_name
        self.loaded = False

    def load_model(self):
        """Load the local LLM (placeholder)."""
        print(f"[UndoPlanGenerator] Loading {self.model_name}...")
        self.loaded = True

    def generate_undo_plan(self, changes: Dict, semantic_info: List[Dict]) -> Dict:
        """Generate a structured rollback or archival plan."""
        steps = []
        recommended_action = "proceed"

        if changes.get("files_deleted"):
            critical_files = [item["path"] for item in semantic_info if item.get("importance", 0) > 0.8]
            if critical_files:
                recommended_action = "archive"
                steps.append("Create archive of critical files before deletion.")
                steps.append(f"Files to archive: {', '.join(critical_files)}")
            else:
                steps.append("No critical files detected. Deletion appears safe.")
        if changes.get("files_modified"):
            steps.append("Create backup of modified files before execution.")
            steps.append(f"Files to backup: {', '.join(changes['files_modified'])}")
        if changes.get("processes_killed"):
            steps.append("Note PIDs of killed processes for potential restart.")
            steps.append(f"Processes: {changes['processes_killed']}")
        steps.append("If needed, restore from overlayfs snapshot.")
        return {"recommended_action": recommended_action, "steps": steps}


if __name__ == "__main__":
    generator = UndoPlanGenerator()
    plan = generator.generate_undo_plan(
        {"files_deleted": ["/home/user/family_photos.zip"]},
        [{"path": "/home/user/family_photos.zip", "importance": 0.95}],
    )
    print(json.dumps(plan, indent=2))
