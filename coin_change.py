"""Find the fewest coins needed for exact change.

Use positive integer coins and a nonnegative integer amount.
Each coin can be used as many times as needed. An impossible amount
returns float("inf"). Use a fresh memo dictionary for a new set of coins.
"""

from time import perf_counter


def coin_change_recursive(coins, amount):
    """Try every possible next coin using recursion."""
    if amount == 0:
        return 0

    best = float("inf")
    for coin in coins:
        if coin <= amount:
            best = min(best, 1 + coin_change_recursive(coins, amount - coin))
    return best


def coin_change_memoized(coins, amount, memo):
    """Save each answer so the same amount is only solved once."""
    if amount == 0:
        return 0
    if amount in memo:
        return memo[amount]

    best = float("inf")
    for coin in coins:
        if coin <= amount:
            best = min(
                best, 1 + coin_change_memoized(coins, amount - coin, memo)
            )
    memo[amount] = best
    return best


def coin_change_dp(coins, amount):
    """Build answers from zero up to the target amount."""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for current in range(1, amount + 1):
        for coin in coins:
            if coin <= current:
                dp[current] = min(dp[current], dp[current - coin] + 1)
    return dp[amount]


def compare_performance():
    """Print average run times in milliseconds for five runs per amount."""
    coins = [1, 2, 5]
    repeats = 5
    print("| Amount | Minimum coins | Recursive (ms) | Memoized (ms) | Bottom-up (ms) |")
    print("| --- | --- | --- | --- | --- |")

    for amount in [5, 11, 15, 20, 25]:
        times = []
        answers = []
        for method in [coin_change_recursive, coin_change_memoized, coin_change_dp]:
            start = perf_counter()
            for _ in range(repeats):
                if method is coin_change_memoized:
                    answer = method(coins, amount, {})
                else:
                    answer = method(coins, amount)
            times.append((perf_counter() - start) * 1000 / repeats)
            answers.append(answer)

        assert answers[0] == answers[1] == answers[2]
        print(
            f"| {amount} | {answers[0]} | {times[0]:.4f} | "
            f"{times[1]:.4f} | {times[2]:.4f} |"
        )


if __name__ == "__main__":
    compare_performance()
