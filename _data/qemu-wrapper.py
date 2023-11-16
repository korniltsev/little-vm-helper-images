#!/usr/bin/env python3
import sys
import os


logf = open('log.txt', 'a')
print(sys.argv, file=logf)
logf.close()

o='/usr/bin/qemu-system-aarch64-orig'
args = [o] + sys.argv[1:]

if 'virt,gic-version=host,accel=kvm:tcg' in args:
    args[args.index('virt,gic-version=host,accel=kvm:tcg')] = 'virt'

if 'host' in args:
    args[args.index('host')] = 'cortex-a57'

if 'driftfix=slew' in args:
    args[args.index('driftfix=slew')] = 'base=utc,clock=host'

logf = open('log.txt', 'a')
print(args, file=logf)
logf.close()


os.execv(o, args)