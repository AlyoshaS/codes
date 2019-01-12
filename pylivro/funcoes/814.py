#!/usr/bin/python
# coding: latin-1
#
#
#

def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

print("MDC 100 e 50: %d" % mdc(100,50))
print("MDC 32 e 24: %d" % mdc(32,24))
print("MDC 15 e 5: %d" % mdc(15,5))
