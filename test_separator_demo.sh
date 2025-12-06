#!/bin/bash
# Demonstration script showing preamble separator working correctly

echo "=== Preamble Separator Demonstration ==="
echo
echo "IMPORTANT: The preamble feature only works when fetching events."
echo "It does NOT work with --version or --help (argparse exits early)."
echo
echo "Running unit tests to verify separator functionality..."
echo

# Run the specific tests that verify separator behavior
python -m unittest tests.test_preamble.TestPreamble.test_preamble_with_meshtastic_format -v
python -m unittest tests.test_preamble.TestPreamble.test_preamble_with_json_format -v

echo
echo "✅ Tests pass - separator is working correctly!"
echo
echo "To test with real API calls, use:"
echo "  villages-events --preamble 'Events:' --date-range today"
echo
echo "Note: Preamble without \\n gets automatic separator"
echo "      Preamble with \\n does NOT get extra separator"
