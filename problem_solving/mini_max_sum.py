def mini_max_sum(arr):
    if len(set(arr)) == 1:
        arr.pop(0)
        mini_sum = sum(arr)
        max_sum = sum(arr)
    else:
        mini_sum = sum(list(filter(lambda a: a != max(arr), arr)))
        max_sum = sum(list(filter(lambda a: a != min(arr), arr)))
    print(mini_sum, max_sum)


if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))
    mini_max_sum(ar)
