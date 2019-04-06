def find_unique_path(lydia):
    path = ""
    for dir in lydia:
        if dir == "S":
            path += "E"
        else:
            path += "S"
    return path

if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        n = input()
        lydia = input()
        path = find_unique_path(lydia)
        print("Case #{}: {}".format(case_num, path))
        case_num += 1