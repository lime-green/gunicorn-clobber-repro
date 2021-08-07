#!/usr/bin/env python

import requests

MAX_BODY_SIZE_KB = 20


def _do_one_round(host, port, read_body, body_size):
    successes, errors, fails = 0, 0, 0

    for _ in range(0, 100):
        try:
            resp = requests.post(
                f"http://{host}:{port}?read_body={read_body}",
                data="a" * body_size * 1024,
            )
        except requests.exceptions.ChunkedEncodingError as e:
            errors += 1
        else:
            if int(resp.headers["Content-Length"]) != len(resp.content):
                fails += 1
            else:
                successes += 1

    print(f"{'request size':>10} {'successes':>10} {'fails':>10} {'errors':>10}")
    print(f"{str(body_size) + 'KB':<10} {successes:>10} {fails:>10} {errors:>10}")


print("*"*10)
print("Direct Gunicorn")
print("*"*10)

print("Without reading body:")
for i in range(MAX_BODY_SIZE_KB + 1):
    _do_one_round("app", 8000, read_body=0, body_size=i)

print("\n\nWith reading body:")
_do_one_round("app", 8000, read_body=1, body_size=MAX_BODY_SIZE_KB)


print("\n")
print("*"*10)
print("Nginx proxy")
print("*"*10)

print("Without reading body:")
for i in range(MAX_BODY_SIZE_KB + 1):
    _do_one_round("nginx", 8001, read_body=0, body_size=i)

print("\n\nWith reading body:")
_do_one_round("nginx", 8001, read_body=1, body_size=MAX_BODY_SIZE_KB)

