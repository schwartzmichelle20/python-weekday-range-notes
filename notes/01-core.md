# List weekdays in a date range: implementation

## What the example does

The end date is exclusive and weekends are excluded. This does not account for public holidays; reversed ranges produce no dates.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  "2026-01-01",
  "2026-01-08"
]
```

Expected result:

```json
[
  "2026-01-01",
  "2026-01-02",
  "2026-01-05",
  "2026-01-06",
  "2026-01-07"
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
