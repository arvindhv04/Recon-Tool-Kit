# Recon-Tool-Kit

A Python reconnaissance toolkit for authorized security assessments.

## Install

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Run

```bash
.venv/bin/python -m recon_toolkit example.com
```

The target may also be supplied as a URL. Results are written to `report.json`.

Only scan systems you own or have explicit permission to assess.

## Layout

- `recon_toolkit/cli.py`: command-line orchestration
- `recon_toolkit/scanners/`: discovery and vulnerability scanners
- `recon_toolkit/reporting/`: report writers
- `tests/`: test and demonstration scripts

## Thank you nibbas
