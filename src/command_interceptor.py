"""
Command Interceptor Module
Captures user commands before execution via shell hook or wrapper.
"""

import shlex
from typing import List, Optional


class CommandInterceptor:
    """Intercepts shell commands and prepares them for analysis."""

    def __init__(self, shell: str = "/bin/bash"):
        self.shell = shell
        self.history: List[str] = []

    def parse_command(self, user_input: str) -> List[str]:
        """Parse raw command text, preserving quoted arguments."""
        try:
            parts = shlex.split(user_input)
            if not parts:
                return []
            self.history.append(user_input)
            return parts
        except ValueError:
            return user_input.split()

    def get_command_name(self, parts: List[str]) -> Optional[str]:
        """Return the executable name from parsed command."""
        return parts[0] if parts else None

    def get_arguments(self, parts: List[str]) -> List[str]:
        """Return arguments of the command."""
        return parts[1:] if len(parts) > 1 else []

    def preview_command(self, parts: List[str]) -> str:
        """Return a string representation of the command for display."""
        return " ".join(parts)


if __name__ == "__main__":
    interceptor = CommandInterceptor()
    cmd = interceptor.parse_command("rm -rf /home/user/important_project/")
    print(f"Command: {interceptor.preview_command(cmd)}")
    print(f"Executable: {interceptor.get_command_name(cmd)}")
    print(f"Args: {interceptor.get_arguments(cmd)}")
