"""
Semantic Analyzer Module
Uses a local LLM to classify files and directories by importance and category.
"""

import json
from typing import Dict, List


class SemanticAnalyzer:
    """Analyses the semantic importance of files affected by a command."""

    def __init__(self, model_name: str = "tinyllama"):
        self.model_name = model_name
        self.loaded = False

    def load_model(self):
        """Load the local LLM model (placeholder)."""
        print(f"[SemanticAnalyzer] Loading {self.model_name}...")
        self.loaded = True

    def analyze_path(self, path: str) -> Dict:
        """Return semantic category and importance for one path."""
        category = "unknown"
        importance = 0.5

        if "/etc/" in path or "/boot/" in path or "/usr/" in path:
            category = "system_config"
            importance = 0.9
        elif "/home/" in path:
            if any(ext in path.lower() for ext in [".jpg", ".png", ".mp4", ".zip", ".tar", ".gz"]):
                category = "personal_media"
                importance = 0.95
            elif any(ext in path.lower() for ext in [".doc", ".pdf", ".txt", ".md"]):
                category = "personal_document"
                importance = 0.9
            else:
                category = "personal_other"
                importance = 0.7
        elif "/tmp/" in path or "/var/tmp/" in path:
            category = "temporary"
            importance = 0.2
        elif "/build/" in path or "/dist/" in path:
            category = "build_artifact"
            importance = 0.4

        return {"path": path, "category": category, "importance": importance}

    def analyze_paths(self, paths: List[str]) -> List[Dict]:
        """Analyse a list of paths and return results."""
        return [self.analyze_path(path) for path in paths]


if __name__ == "__main__":
    analyzer = SemanticAnalyzer()
    sample_paths = ["/home/user/family_photos.zip", "/etc/nginx/nginx.conf", "/tmp/cache.tmp"]
    for result in analyzer.analyze_paths(sample_paths):
        print(json.dumps(result, indent=2))
