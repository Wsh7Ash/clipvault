# Usage

## Commands

| Command | Purpose |
|---|---|
| `clipvault save TEXT` | Append `TEXT` to the history |
| `clipvault list` | Print the numbered history |

## Examples

```shell
clipvault save 'hello world'
clipvault list
```

## Exit codes

- `0` - the command completed successfully
- `1` - click reported a usage error (missing or invalid option)
- `2` - click could not parse the command line

## Output

Output is rendered with `rich` and written to stdout, so it can be captured or
piped. Example runs are committed under `results/`.
