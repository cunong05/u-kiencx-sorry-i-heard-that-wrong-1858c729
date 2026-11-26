# Sorry, I Heard That Wrong

The funniest one-line apology a smart speaker gives after mishearing its owner — an entry for the [make.fun bounty "Sorry, I Heard That Wrong"](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729).

[![make.fun](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![Rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/cunong05/u-kiencx-sorry-i-heard-that-wrong-1858c729/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![Reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/cunong05/u-kiencx-sorry-i-heard-that-wrong-1858c729/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)

> "Sorry, I heard 'play jazz' as 'order twelve pizzas.' They're on their way, and frankly, they sound better than jazz."

## How it works

`main.py` holds the entry as a fixed string, checks it before writing (1–140 characters, a single line), creates `/output` if needed, writes the text to `/output/entry.txt` with no trailing newline, and prints it. The program is fully deterministic — it always writes the same text.

## Running it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
