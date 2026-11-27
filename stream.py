"""Process JSON Lines sequentially, emitting one envelope per input line."""
import json
import sys
from solution import solve

LIMIT = 1024 * 1024

def main():
    failures = False
    line_number = 0
    while True:
        raw = sys.stdin.buffer.readline(LIMIT + 1)
        if not raw:
            break
        line_number += 1
        if len(raw) > LIMIT:
            while raw and not raw.endswith(b'\n'):
                raw = sys.stdin.buffer.readline(LIMIT + 1)
            envelope = {'line': line_number, 'ok': False, 'error': 'LineTooLong'}
            failures = True
        else:
            try:
                result = solve(json.loads(raw))
                json.dumps(result, allow_nan=False)
                envelope = {'line': line_number, 'ok': True, 'result': result}
            except (ValueError, TypeError, KeyError, IndexError, ArithmeticError, AttributeError) as error:
                envelope = {'line': line_number, 'ok': False, 'error': type(error).__name__}
                failures = True
        print(json.dumps(envelope, ensure_ascii=False, allow_nan=False), flush=True)
    return 1 if failures else 0

if __name__ == '__main__':
    raise SystemExit(main())
