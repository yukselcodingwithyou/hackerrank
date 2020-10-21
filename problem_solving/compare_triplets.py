

def compare_triplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] < b[i]:
            bob += 1
        elif a[i] > b[i]:
            alice += 1
    return [alice, bob]


if __name__ == "__main__":
    compare_triplets([1, 2, 3], [4, 3, 2])