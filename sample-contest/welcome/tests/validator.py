#!/usr/bin/env python3
a, b = map(float, input().split())
assert a.is_integer()
assert b.is_integer()
assert 1 <= int(a) <= 100
assert 1 <= int(b) <= 100000
