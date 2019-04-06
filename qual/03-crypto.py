import math
import statistics 

def crack(nl, cipher):
    n,l = [int(i) for i in nl.split(" ")]
    nums = map(lambda i: int(i), cipher.split(" "))
    all_prime_factors = set()
    options = []
    firstfactors = None
    i = 0
    for num in nums:
        factors = prime_factors(num)
        lfactors = list(factors)
        if firstfactors is None:
            firstfactors = lfactors
        if i > 0:
            if len(lfactors) == 1:
                # options = [lfactors]
                options[i-1] = lfactors
            else:
                options[i-1] += lfactors
        options.append(list(lfactors))
        i+=1
        all_prime_factors = all_prime_factors | factors
    options = [firstfactors] + options

    ## build alphabet
    ordered = list(all_prime_factors)
    ordered.sort()

    letter = ord('A')
    alphabet = {}
    for prime in ordered:
        alphabet[prime] = chr(letter)
        letter += 1

    while not_done(options):
        idx = -1

        for option in options:
            idx += 1
            if len(option) == 1:
                continue

            foundOne = False
            for o in option:
                unique = True
                if idx-1 >= 0:
                    left = options[idx-1]
                    if o in left:
                        unique = False
                if idx+1 < len(options):
                    right = options[idx+1]
                    if o in right:
                        unique = False
                if unique:
                    options[idx] = [o]
                    foundOne = True
                    break
            if foundOne:
                continue

            try:
                m = statistics.mode(option)
            except statistics.StatisticsError:
                ## nothing to do
                continue

            if idx-1 >= 0:
                if m in options[idx-1] and len(options[idx-1]) > 1:
                    options[idx-1].remove(m)

            if idx+1 < len(options):
                if m in options[idx+1] and len(options[idx+1]) > 1:
                    options[idx+1].remove(m)

            options[idx] = [m]

    result = ""
    for num in options:
        result += alphabet[num[0]]
    return result


def not_done(options):
    for o in options:
        if len(o) > 1:
            return True
    return False


# thanks https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
def prime_factors(n):
    results = set()
    while n % 2 == 0: 
        results.add(2)
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            results.add(i)
            n = int(n / i)
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        results.add(int(n))

    return results


if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        nl = input()
        cipher = input()
        clear = crack(nl, cipher)
        print("Case #{}: {}".format(case_num, clear))
        case_num += 1