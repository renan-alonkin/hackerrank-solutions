#!/bin/python3

def birthdayCakeCandles(candles):
    # Write your code here
    highest_candle = max(candles)
    candle_count = candles.count(highest_candle)
    return candle_count

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    # I had to change a little bit here to test on my computer :)
    print(result)