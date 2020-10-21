def birthday_cake_candles(candles):
    return candles.count(max(candles))


if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthday_cake_candles(candles)