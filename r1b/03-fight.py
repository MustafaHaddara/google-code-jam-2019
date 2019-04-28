def find_fair(c_skills, d_skills, e):
    max_len = len(c_skills)
    start = 0
    end = 0

    num_fair = 0

    c_max = c_skills[start]
    d_max = d_skills[start]
    while start < max_len:
        c_next = c_skills[end]
        d_next = d_skills[end]

        if c_next>c_max:
            c_max = c_next
        if d_next>d_max:
            d_max = d_next

        if abs(c_max-d_max) <= e:
            num_fair += 1
        
        end += 1
        if end >= max_len:
            start += 1
            if start == max_len:
                break
            end = start
            if end == max_len:
                end = start
            c_max = c_skills[start]
            d_max = d_skills[start]

    return num_fair

if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        num_swords,e = [int(i) for i in input().split(" ")]
        c_skills = [int(i) for i in input().split(" ")]
        d_skills = [int(i) for i in input().split(" ")]
        num_fair_fights = find_fair(c_skills, d_skills, e)
        print("Case #{}: {}".format(case_num, num_fair_fights))
        case_num += 1