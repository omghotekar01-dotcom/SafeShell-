# SafeShell++

SafeShell++ is a **command-safety research prototype** for exploring how a shell assistant might explain a command's likely impact and suggest a safer action before execution.

The current implementation is a Python command-line demonstration. It parses commands, applies path-based heuristics, predicts effects for a small command subset, and prints an impact report. It **does not** execute commands in a sandbox, create real filesystem snapshots, or guarantee rollback.

## What the current prototype does

1. Parse an entered command into arguments.
2. Inspect paths using heuristic importance rules.
3. Predict likely changes for selected commands such as `rm`, `touch`, `chmod`, and `kill`.
4. Generate a suggested action and a text-based impact report.
5. Ask whether to proceed, archive, or cancel.

The confirmation step is currently illustrative: it records and clears an in-memory transaction identifier. Selecting **Proceed** does not run the shell command, and **Archive** does not yet archive the affected files.

## Run locally

Use Python 3.10+ and install the dependencies:

```bash
python -m pip install -r requirements.txt
python src/cli.py
```

For the included unit tests:

```bash
python -m pytest tests -q
```

The module tests exercise parsing, impact prediction, reporting, and transaction-state handling. Passing them would not establish that real-world command execution or recovery is safe.

## Code map

| File | Current responsibility |
| --- | --- |
| `src/cli.py` | Interactive command prompt and confirmation flow |
| `src/command_interceptor.py` | Command parsing |
| `src/semantic_analyzer.py` | Heuristic categorization of paths |
| `src/simulator.py` | Predicted effects for a limited set of commands |
| `src/undo_plan_generator.py` | Suggested response to predicted changes |
| `src/transaction_manager.py` | In-memory transaction state (placeholder) |
| `src/impact_report.py` | Human-readable summary |
| `tests/test_basic.py` | Basic component tests |

## Planned, not implemented

The original design explores integration with local language models, isolated command execution, archival, and actual snapshot/restore mechanisms. These are **future engineering tasks**, not guarantees of the current code. The architecture sketch is in `architecture.png`.

## Safety boundaries

Do not use SafeShell++ as a protective wrapper around real destructive commands. The simulator does not inspect the filesystem or all command flags, and its predicted change list can differ from the actual effect of a command. Use ordinary shell precautions, backups, and a separate disposable test environment for experimentation.

## License

MIT.
