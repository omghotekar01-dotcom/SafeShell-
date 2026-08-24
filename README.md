# SafeShell++

Transactional Command Execution with Semantic Intent Analysis, AI-Generated Undo Plans & Proactive Archival

SafeShell++ is an indigenous Linux command safety framework that prevents irreversible damage by intercepting commands, understanding their semantic impact, simulating execution, and offering rollback or archival options.

## Problem
Linux users and administrators often run destructive commands (e.g., `rm -rf`, wrong `chmod`) without realising the full consequences. Existing tools provide no undo mechanism, no semantic understanding, and no transactional safety.

## Solution
SafeShell++ combines:
- **Semantic Intent Analysis** - local LLM classifies files and predicts importance.
- **Sandbox Simulation** - run command in isolated environment to observe exact changes.
- **AI-Generated Undo Plans** - step-by-step rollback instructions.
- **Proactive Archival** - compress and archive instead of delete.
- **Transactional Execution** - commit or rollback using overlayfs/LVM snapshots.

## Modules
- `command_interceptor.py` - hooks into shell
- `semantic_analyzer.py` - LLM-based file classification
- `simulator.py` - sandbox execution and change detection
- `undo_plan_generator.py` - LLM rollback plan generation
- `transaction_manager.py` - snapshot/commit/rollback
- `impact_report.py` - human-readable risk summary
- `cli.py` - command line interface

## Status
Prototype / Skeleton code. Full implementation in progress.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Install sandbox tools: `sudo apt install bubblewrap`
3. Run: `python src/cli.py`
4. Run tests: `pytest`

## Architecture
See `architecture.png` for system design.

## License
MIT
