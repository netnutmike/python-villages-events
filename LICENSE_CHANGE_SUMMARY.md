# License Change Summary: MIT → GPL v3

## Overview

The Villages Event Scraper project has been successfully relicensed from MIT License to GNU General Public License v3.0 (GPL v3).

## Changes Made

### 1. License File
- ✅ Replaced `LICENSE` file with full GPL v3.0 text
- ✅ Downloaded from official GNU source

### 2. Source Code Headers
All Python source files now include GPL v3 license headers:
- ✅ `villages_events.py` - Main entry point
- ✅ `src/config.py` - Configuration module
- ✅ `src/config_loader.py` - Config loader
- ✅ `src/token_fetcher.py` - Token fetcher
- ✅ `src/session_manager.py` - Session manager
- ✅ `src/api_client.py` - API client
- ✅ `src/event_processor.py` - Event processor
- ✅ `src/output_formatter.py` - Output formatter
- ✅ `src/exceptions.py` - Custom exceptions
- ✅ `src/__version__.py` - Version information

### 3. Documentation Updates
- ✅ `README.md` - Updated license badge and section
- ✅ `setup.py` - Changed classifier to GPL v3
- ✅ `src/__version__.py` - Updated `__license__` field
- ✅ `docs/CONTRIBUTING.md` - Updated license reference
- ✅ `docs/README.md` - Updated license references
- ✅ `REPOSITORY_SETUP.md` - Updated license references

### 4. Tools Created
- ✅ `scripts/add_gpl_headers.py` - Script to add GPL headers to source files

## GPL v3 License Header

All source files now include this header:

```python
"""
Copyright (C) 2025

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
```

## What GPL v3 Means

### Freedoms Granted
- ✅ Freedom to use the software for any purpose
- ✅ Freedom to study and modify the source code
- ✅ Freedom to distribute copies
- ✅ Freedom to distribute modified versions

### Requirements (Copyleft)
- ⚠️ Modified versions must also be GPL v3
- ⚠️ Source code must be made available
- ⚠️ Changes must be documented
- ⚠️ Same license must be used for derivative works

### Key Differences from MIT

| Aspect | MIT License | GPL v3 License |
|--------|-------------|----------------|
| Type | Permissive | Copyleft |
| Derivative works | Can be proprietary | Must be GPL v3 |
| Source code | Not required to share | Must be shared |
| Patent protection | No | Yes |
| Trademark use | Not addressed | Not granted |
| Compatibility | Very high | Moderate |

## Verification

All tests still pass after license change:
```bash
python -m unittest discover tests -v
# Result: 128 tests passed ✅
```

Version command still works:
```bash
python villages_events.py --version
# Output: villages_events.py 1.0.0
```

## For Contributors

### What This Means for You

1. **Your contributions** will be licensed under GPL v3
2. **You retain copyright** to your contributions
3. **You grant rights** under GPL v3 to all users
4. **Derivative works** must also be GPL v3

### Contributing Under GPL v3

When you contribute to this project:
- Your code will be GPL v3 licensed
- You agree to the GPL v3 terms
- Your contributions help keep the software free
- See `docs/CONTRIBUTING.md` for guidelines

## For Users

### What This Means for You

1. **You can use** this software freely
2. **You can modify** the source code
3. **You can distribute** copies and modifications
4. **You must** keep it GPL v3 if you distribute it

### Using This Software

```bash
# Use freely
python villages_events.py

# Modify freely
# Edit source files as needed

# Distribute freely
# But keep it GPL v3 and include source
```

## For Distributors

If you distribute this software or modified versions:

1. **Include the LICENSE file**
2. **Provide source code** (or offer to provide it)
3. **Keep the GPL v3 license** on all files
4. **Document your changes** in CHANGELOG.md
5. **Include copyright notices** from original authors

## Files Changed

### Modified Files
```
LICENSE                          # Replaced with GPL v3
README.md                        # Updated badge and license section
setup.py                         # Changed classifier
villages_events.py               # Added GPL header
src/__version__.py              # Updated license field
src/config.py                   # Added GPL header
src/config_loader.py            # Added GPL header
src/token_fetcher.py            # Added GPL header
src/session_manager.py          # Added GPL header
src/api_client.py               # Added GPL header
src/event_processor.py          # Added GPL header
src/output_formatter.py         # Added GPL header
src/exceptions.py               # Added GPL header
docs/CONTRIBUTING.md            # Updated license reference
docs/README.md                  # Updated license references
REPOSITORY_SETUP.md             # Updated license references
```

### New Files
```
scripts/add_gpl_headers.py      # Tool to add GPL headers
LICENSE_CHANGE_SUMMARY.md       # This file
```

## Resources

- [GPL v3 Full Text](https://www.gnu.org/licenses/gpl-3.0.html)
- [GPL v3 FAQ](https://www.gnu.org/licenses/gpl-faq.html)
- [How to Apply GPL](https://www.gnu.org/licenses/gpl-howto.html)
- [GPL Compatibility](https://www.gnu.org/licenses/license-compatibility.html)

## Questions?

### Why GPL v3?
GPL v3 ensures that this software and all derivatives remain free and open source.

### Can I use this in commercial software?
Yes, but your software must also be GPL v3 and provide source code.

### Can I use this in proprietary software?
No, GPL v3 requires derivative works to also be GPL v3.

### What if I just use it as-is?
You can use it freely without any restrictions on your own software.

## Status

✅ **License change complete**
✅ **All source files updated**
✅ **All documentation updated**
✅ **All tests passing**
✅ **Ready for use under GPL v3**

---

**Previous License**: MIT License  
**New License**: GNU General Public License v3.0  
**Change Date**: November 16, 2025  
**Status**: Complete ✅
