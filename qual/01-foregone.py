def no_4_digit(n):
    a = int(n)
    b = 0

    mult = 1
    for i in n[::-1]:
        if i == '4':
            b += mult
            a -= mult
        mult *= 10
    return a,b

if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        n = input()
        a,b = no_4_digit(n)
        print("Case #{}: {} {}".format(case_num, a,b))
        case_num += 1