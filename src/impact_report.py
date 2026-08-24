"""Impact Report Generator Module."""

from typing import Dict, List


class ImpactReport:
    """Formats analysis results into a user-friendly report."""

    @staticmethod
    def generate_report(changes: Dict, semantic_info: List[Dict], undo_plan: Dict) -> str:
        """Generate a plain-English impact report."""
        lines = ["=" * 50, "SafeShell++ Impact Report", "=" * 50]
        counts = {
            "files_deleted": ("Files to be deleted", "[HIGH]"),
            "files_modified": ("Files to be modified", "[MEDIUM]"),
            "files_created": ("Files to be created", "[LOW]"),
            "processes_killed": ("Processes to be killed", "[INFO]"),
        }
        for key, (label, marker) in counts.items():
            count = len(changes.get(key, []))
            if count:
                lines.append(f"{marker} {label}: {count}")

        critical = [item["path"] for item in semantic_info if item.get("importance", 0) > 0.8]
        if critical:
            lines.append("\nCRITICAL FILES AFFECTED:")
            lines.extend(f"   - {path}" for path in critical)
        lines.append("\nRecommended Action: " + undo_plan.get("recommended_action", "proceed"))
        lines.append("Steps:")
        lines.extend(f"   - {step}" for step in undo_plan.get("steps", []))
        lines.append("\n" + "=" * 50)
        return "\n".join(lines)


if __name__ == "__main__":
    print(ImpactReport.generate_report({}, [], {"recommended_action": "proceed", "steps": []}))
