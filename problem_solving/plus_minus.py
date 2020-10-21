
def plus_minus(arr):
    negatives = list(filter(lambda a: a < 0, arr))
    positives = list(filter(lambda a: a > 0, arr))
    zeroes = list(filter(lambda a: a == 0, arr))
    print("{:.6f}".format(len(positives)/len(arr)))
    print("{:.6f}".format(len(negatives)/len(arr)))
    print("{:.6f}".format(len(zeroes)/len(arr)))


if __name__ == "__main__":
    plus_minus([4, 3, 9, 0, 1])