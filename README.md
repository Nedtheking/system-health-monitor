# System Health Monitoring Tool

A modular, menu-driven Python tool that diagnoses local system health — CPU load, memory usage, and disk usage across drives — and reports it in plain language for non-technical users.

## Modes
- **Quick Scan** — surfaces only problems / warnings.
- **Full Report** — complete CPU, RAM, and disk breakdown with a summary.
- **Modular Checks** — run individual checks on demand (CPU, RAM, disk).

## Design
- **Read-only and low-overhead** — diagnostics only; never modifies the system.
- **Modular architecture** — each check (`cpu_check.py`, `ram_check.py`, `disk_check.py`) is independent, with separate data-collection and reporting layers for maintainability.

## Structure
| File | Responsibility |
|---|---|
| `main.py` | Menu / entry point |
| `quick_scan.py` | Problems-only scan |
| `full_report.py` | Full CPU + RAM + disk report |
| `modular_scan.py` | On-demand individual checks |
| `cpu_check.py` / `ram_check.py` / `disk_check.py` | Individual metric collectors |

## Run it
```bash
pip install -r requirements.txt   # if a requirements file is present
python main.py
```

## Tech
Python 3.10
