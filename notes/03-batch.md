# Ordered batch processing for List weekdays in a date range

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
[
  "2026-01-01",
  "2026-01-08"
]
```

Result:
```json
[
  "2026-01-01",
  "2026-01-02",
  "2026-01-05",
  "2026-01-06",
  "2026-01-07"
]
```

## Case 2

Input:
```json
[
  "2026-01-03",
  "2026-01-05"
]
```

Result:
```json
[]
```

## Case 3

Input:
```json
[
  "2026-01-02",
  "2026-01-02"
]
```

Result:
```json
[]
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

The end date is exclusive and weekends are excluded. This does not account for public holidays; reversed ranges produce no dates.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
