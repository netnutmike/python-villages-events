# Preamble Usage Notes

## Important: Shell Escaping

When using the `--preamble` option, be aware of how your shell interprets escape sequences.

### Correct Usage

**For newlines in the preamble, use `$'...'` syntax (bash/zsh):**

```bash
# This works - newline is interpreted
villages-events --preamble $'Events:\n'

# This also works - no newline, separator added automatically
villages-events --preamble "Events:"

# This works - explicit newline
villages-events --preamble "Events:
"
```

**What DOESN'T work:**

```bash
# This does NOT work - \n is treated as literal backslash-n
villages-events --preamble 'Events:\n'

# This does NOT work - single quotes don't interpret \n
villages-events --preamble "Events:\n"  # (in some shells)
```

## How the Separator Works

The code checks if the preamble ends with an actual newline character (`\n`):

```python
if args.preamble:
    print(args.preamble, end='')
    # Add separator if preamble doesn't end with newline
    if not args.preamble.endswith('\n'):
        print()  # Add newline separator
```

### Examples

**1. Simple label (separator added automatically):**
```bash
villages-events --preamble "Events:"
# Output:
# Events:
# Brownwood,Jazz Band#
```

**2. With explicit newline (no extra separator):**
```bash
villages-events --preamble $'Events:\n'
# Output:
# Events:
# Brownwood,Jazz Band#
```

**3. Multiple lines:**
```bash
villages-events --preamble $'Schedule\n--------\n'
# Output:
# Schedule
# --------
# Brownwood,Jazz Band#
```

## Testing

To verify the separator is working:

```bash
# Test 1: Without newline (should add separator)
python -m src.villages_events --preamble "Test:" --version
# Expected: Test:\nvillages_events.py 1.0.0

# Test 2: With newline (should not add extra separator)
python -m src.villages_events --preamble $'Test:\n' --version
# Expected: Test:\nvillages_events.py 1.0.0
```

## Troubleshooting

### "I don't see a separator"

**Check:**
1. Are you using the latest code? Run: `pip install -e . --force-reinstall --no-deps`
2. Clear Python cache: `find . -type d -name "__pycache__" -exec rm -rf {} +`
3. Verify the code:
   ```bash
   grep -A 3 "Add separator if preamble" src/villages_events.py
   ```

### "The separator appears even with \\n"

**Cause:** Your shell isn't interpreting `\n` as a newline.

**Solution:** Use `$'...'` syntax:
```bash
# Wrong
villages-events --preamble "Events:\n"

# Right
villages-events --preamble $'Events:\n'
```

### "I want NO separator"

**Solution:** End your preamble with a newline:
```bash
villages-events --preamble $'Events:\n'
```

Or use an empty string:
```bash
villages-events --preamble ""
```

## Shell-Specific Notes

### Bash/Zsh
Use `$'...'` for escape sequences:
```bash
villages-events --preamble $'Header:\n'
```

### Fish
Use double quotes with actual newline:
```bash
villages-events --preamble "Header:
"
```

### PowerShell (Windows)
Use backtick for newline:
```powershell
villages-events --preamble "Header:`n"
```

## Configuration File

In `config.yaml`, newlines work normally:

```yaml
preamble: "Events:\n"
```

Or multi-line:

```yaml
preamble: |
  Events:
  --------
```

## Summary

- **Automatic separator**: Added when preamble doesn't end with `\n`
- **No extra separator**: When preamble ends with `\n`
- **Shell escaping**: Use `$'...'` for `\n` in bash/zsh
- **Config file**: Newlines work normally in YAML

The feature is working correctly - just make sure your shell is interpreting escape sequences properly!
