# clipvault

Append-only clipboard history stored in a plain JSON file you can save to and list from the terminal.

## Problem

Useful snippets - a command that worked, an ID you pasted twice, a paragraph you rewrote - disappear the moment the clipboard is overwritten. clipvault keeps a small, human-readable history of the things you deliberately save.

## Features

- `save TEXT` appends an entry, `list` prints the numbered history
- Storage is a plain JSON array at `~/.clipvault.json` - greppable, yours
- No daemon, no database, no network access
- Entries are printed with markup disabled, so text containing `[brackets]`
  shows up exactly as it was stored

## Example

```shell
python3 -m clipvault.cli save 'hello world'
python3 -m clipvault.cli list
```

```text
Saved
0: hello world
```

A captured run of the same command is committed at `results/demo-output.txt`.

## Architecture

A single module, `src/clipvault/cli.py`:

- `STORE` is the JSON path (`~/.clipvault.json`); tests monkeypatch it to a
  temporary path, so the suite never touches your real history.
- `save` reads the array (or starts a new one), appends and writes it back.
- `list` reads the array and prints one numbered line per entry.

`click` provides the command group; `rich` renders the output.

## Requirements

- Python 3.10 or newer
- `click`, `rich`

## Installation

```shell
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

On Windows activate the environment with `.venv/Scripts/activate` instead.

## Quick start

```shell
PYTHONPATH=src python3 -m clipvault.cli save 'kubectl get pods -A'
PYTHONPATH=src python3 -m clipvault.cli list
```

## Configuration

The store path is the module constant `cli.STORE`, defaulting to `~/.clipvault.json`. There is no `--store` flag yet; tests redirect it to a temporary file.

## Testing

```shell
python3 -m pytest -q
```

Tests run from a clean clone: `pyproject.toml` sets pytest's `pythonpath` to
`src`, so no install step is needed to run them.

## Project structure

```text
clipvault/
|-- src/clipvault/
|   `-- cli.py            # save / list commands and the store path
|-- tests/
|   |-- test_store.py     # import check
|   `-- test_cli.py       # save -> list round trip
|-- results/              # captured demo output
|-- docs/                 # ARCHITECTURE.md, USAGE.md
`-- pyproject.toml
```

## Limitations

- No `delete`, `search` or size cap: the file only grows.
- No deduplication - saving the same text twice stores it twice.
- Text is passed as a command-line argument, so it is visible in shell
  history and the process list; there is no system-clipboard integration.
- Writes are not locked, so two concurrent saves can lose an entry.
- JSON is stored in plaintext: do not save secrets here.

## Roadmap

- `--store` flag and a `CLIPVAULT_STORE` environment variable
- `delete` / `clear` commands and a maximum history size
- `search SUBSTRING` command
- Read-from-stdin mode so nothing lands in shell history

## Security notes

Local file only, no network access. The store is plaintext JSON: treat it like a text file you would not want read by others, and keep credentials out of it.

## License

MIT - see [LICENSE](LICENSE).
