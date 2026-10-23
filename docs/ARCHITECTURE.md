# Architecture

## Modules

- `clipvault.cli` - `STORE` path constant plus the `save` and `list` click
  commands. Each command is a self-contained read-modify-write of the JSON
  array.

## Data flow

`save TEXT` -> read JSON array (or create one) -> append -> write back -> confirm. `list` -> read JSON array -> print numbered lines.

## Design decisions

- A JSON array instead of SQLite: the data is a flat list, and a readable
  file is the feature.
- The store path is a module-level constant so tests can monkeypatch it
  without argument plumbing.
- Output uses `markup=False` so clipboard content is never interpreted as
  rich markup.

## Testing strategy

- Unit tests cover the core logic (the save/list round trip against a JSON store).
- CLI tests use `click.testing.CliRunner`, so command wiring is exercised
  without a real terminal or subprocess.
- `pyproject.toml` sets `pythonpath = ["src"]`, so `python3 -m pytest -q` works
  from a fresh clone.
