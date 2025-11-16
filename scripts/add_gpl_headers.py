#!/usr/bin/env python3
"""
Script to add GPL v3 license headers to all Python source files.

Copyright (C) 2025

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

import os
from pathlib import Path

GPL_HEADER = '''"""
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
'''

def has_gpl_header(content):
    """Check if file already has GPL header."""
    return "GNU General Public License" in content

def add_header_to_file(filepath):
    """Add GPL header to a Python file if it doesn't have one."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if has_gpl_header(content):
        print(f"✓ {filepath} - Already has GPL header")
        return
    
    # Find the first docstring
    lines = content.split('\n')
    new_lines = []
    in_docstring = False
    docstring_end = -1
    
    for i, line in enumerate(lines):
        if '"""' in line and not in_docstring:
            in_docstring = True
            if line.count('"""') == 2:  # Single line docstring
                docstring_end = i
                break
        elif '"""' in line and in_docstring:
            docstring_end = i
            break
    
    if docstring_end >= 0:
        # Insert GPL header after the first docstring
        new_content = '\n'.join(lines[:docstring_end+1]) + '\n\n' + GPL_HEADER + '\n' + '\n'.join(lines[docstring_end+1:])
    else:
        # No docstring found, add at the beginning
        new_content = GPL_HEADER + '\n\n' + content
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ {filepath} - Added GPL header")

def main():
    """Add GPL headers to all Python source files."""
    project_root = Path(__file__).parent.parent
    
    # Find all Python files in src/ directory
    src_dir = project_root / 'src'
    python_files = list(src_dir.rglob('*.py'))
    
    print(f"Found {len(python_files)} Python files in src/")
    print()
    
    for filepath in python_files:
        if filepath.name == '__init__.py':
            continue  # Skip __init__.py files
        add_header_to_file(filepath)
    
    print()
    print("✅ GPL headers added to all source files")

if __name__ == '__main__':
    main()
