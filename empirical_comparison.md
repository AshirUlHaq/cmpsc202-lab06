# Coin Change Performance Comparison

I tested all three methods with coins `[1, 2, 5]` and amounts 5, 11, 15, 20, and 25 using Python 3. Each time below is the average of five runs, measured with `time.perf_counter()`. Each memoized run started with an empty dictionary so it had to calculate its answers again. All three methods gave the same minimum number of coins. Run `python3 coin_change.py` to repeat the comparison; times will vary between runs and computers.

| Amount | Minimum coins | Recursive (ms) | Memoized (ms) | Bottom-up (ms) |
| --- | --- | --- | --- | --- |
| 5 | 1 | 0.0057 | 0.0031 | 0.0024 |
| 11 | 3 | 0.1094 | 0.0065 | 0.0039 |
| 15 | 3 | 0.9430 | 0.0106 | 0.0058 |
| 20 | 4 | 13.3734 | 0.0142 | 0.0079 |
| 25 | 5 | 187.6570 | 0.0182 | 0.0097 |

The recursive method slowed down quickly as the amount grew because it kept solving the same smaller amounts. It still solved amount 11 in much less than a second. Memoization was much faster because it saved those answers. Bottom-up was the fastest in these tests because it filled a list without making recursive calls. With a fixed set of coins, both dynamic programming methods do work that grows roughly in proportion to the amount, while the plain recursive method grows much faster.
