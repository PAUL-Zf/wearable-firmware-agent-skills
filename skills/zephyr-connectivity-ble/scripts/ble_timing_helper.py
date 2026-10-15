#!/usr/bin/env python3
"""Legacy LE timing conversion; optional latency/timeout combination validation.

Adapted from beriberikix/zephyr-agent-skills. Apache-2.0; see ../LICENSE and ../SOURCE.json.
Does not model subrating or newer short connection interval modes.
"""
import argparse
import math

ADV_STEP_MS = 0.625
CONN_STEP_MS = 1.25

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--adv-ms', type=float)
    parser.add_argument('--conn-ms', type=float, action='append', default=[])
    parser.add_argument('--latency', type=int)
    parser.add_argument('--timeout-ms', type=float)
    args = parser.parse_args()
    if args.adv_ms is None and not args.conn_ms:
        parser.error('provide --adv-ms or --conn-ms')
    if len(args.conn_ms) > 2:
        parser.error('provide at most min/max connection intervals')
    def convert(label, ms, step, low, high):
        if not math.isfinite(ms) or not low <= ms <= high:
            parser.error(f'{label} must be finite and in [{low}, {high}] ms')
        units = round(ms / step)
        if not math.isclose(units * step, ms, abs_tol=1e-7):
            parser.error(f'{label} must be an exact multiple of {step} ms')
        print(f'{label}: {ms:g} ms = {units} units ({step:g} ms)')
    if args.adv_ms is not None:
        convert('legacy advertising interval', args.adv_ms, ADV_STEP_MS, 20, 10240)
    for ms in args.conn_ms:
        convert('connection interval', ms, CONN_STEP_MS, 7.5, 4000)
    if len(args.conn_ms) == 2 and args.conn_ms[0] > args.conn_ms[1]:
        parser.error('minimum connection interval exceeds maximum')
    if args.latency is not None or args.timeout_ms is not None:
        if not args.conn_ms or args.latency is None or args.timeout_ms is None:
            parser.error('combination validation needs connection interval, latency and timeout')
        if not 0 <= args.latency <= 499:
            parser.error('latency must be in [0, 499]')
        convert('supervision timeout', args.timeout_ms, 10, 100, 32000)
        minimum = 2 * (1 + args.latency) * max(args.conn_ms)
        if args.timeout_ms <= minimum:
            parser.error(f'supervision timeout must be strictly greater than {minimum:g} ms')
        print('PASS: conventional LE supervision inequality; confirm accepted parameters on target')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
