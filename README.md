# tiny-chess-engine-v3

[![Rank](https://make.fun/badge/tiny-chess-01/0xberuuu/tiny-chess-engine-v3/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![Reward](https://make.fun/badge/tiny-chess-01/0xberuuu/tiny-chess-engine-v3/reward.svg)](https://make.fun/bounty/tiny-chess-01)
[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)

A tiny chess engine in 4 KB of Python for the [make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01) ("Build the strongest chess engine in 4 KB of Python").

`main.py` (4,093 bytes, Python 3 stdlib only) is a complete engine: 0x88 board, negamax with alpha-beta and iterative deepening, quiescence search (captures and promotions, with check evasions), MVV-LVA move ordering, piece-square tables, and a fixed 20,000-node budget per move (about 2-4 seconds per move, under the 10-second limit). It plays legal chess over the make.fun env HTTP protocol and is fully deterministic.

## Run

```sh
python3 main.py
```

The engine connects to the env server at `MAKEFUN_ENV_URL` (default `http://127.0.0.1:18080`) and plays games until the trial is done.

## Verify

Perft passes on all six standard test positions (depths 1-4). Measured local 6-game gauntlet vs the house engines (practice trial-0): 0.5/6 (0 wins, 1 draw vs nodes-100k, 5 losses), worst move 5.9 s.
