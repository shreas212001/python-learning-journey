def swap_case(s):
    p = ""

    for i in s:
        if "A" <= i <= "Z":
            p += i.lower()
        else :
            p += i.upper()
    return p


if __name__ == '__main__':
    s = swap_case(input())
    print(s)