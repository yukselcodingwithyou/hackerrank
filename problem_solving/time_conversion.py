def time_conversion(s):
    am_or_pm = s[-2:]
    if am_or_pm == "PM":
        if s[:2] == "12":
            return s[:8]
        else:
            a = int(s[:2]) + 12
            print("a", a)
            if a % 10 == a:
                c = "0" + str(a)
            else:
                c = str(a)
            return c + s[2:8]
    else:
        if s[:2] == "12":
            return "00" + s[2:8]
        else:
            return s[:8]


if __name__ == '__main__':
    st = input()
    result = time_conversion(st)
    print(result)
