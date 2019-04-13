import sys
import random
def determine_gophers(nights, max_gophers):
    # base = [ 18 ] * 17

    # # not allowed to have all of them be the same
    # # also not allowed to throw out the same thing each time
    # a = [ 17 ] + base
    # b = base + [ 17 ]
    # current = a

    all_possibilities = None
    num_requests = 0
    while num_requests < nights:
        num_requests += 1
        current = [random.randint(2, 18) for i in range(18)]
        print(" ".join((str(i) for i in current)))

        response = [int(i) for i in input().split(" ")]

        bases = {}
        for i in range(len(current)):
            blades = current[i]
            inc = response[i]
            # if inc == 0:
            #     ## assume there was no looping around
            #     continue
            if blades not in bases:
                bases[blades] = set()
            bases[blades].add(inc)

        minimum_guess = sum(response)
        if all_possibilities is not None:
            all_possibilities = set(filter( lambda p: p>=minimum_guess, all_possibilities))

        possibilities = gen_possibilities(minimum_guess, bases, max_gophers)
        print("new possibilities: {}".format(possibilities))
        if all_possibilities is None:
            all_possibilities = possibilities 
        else:
            all_possibilities = all_possibilities & possibilities
        print("total possibilities: {}".format(all_possibilities))
        if len(all_possibilities) == 1:
            print(list(all_possibilities)[0])
            response = int(input())
            if response == -1:
                sys.exit(1)
            return

    # silly fallback case
    return list(all_possibilities)[0]

def gen_possibilities(minimum_guess, bases, maximum):
    result = set()
    result.add(minimum_guess)
    for k in bases:
        result = result | _gen_possibilities_inner(k, bases, maximum, result)
    return result


def _gen_possibilities_inner(k, bases, maximum, guesses):
    new_guesses = set()
    for guess in guesses:
        num = k + guess
        while num < maximum:
            new_guesses.add(num)
            num += k
    return new_guesses

if __name__ == "__main__":
    num_cases, nights, max_gophers = [int(i) for i in input().split(" ")]
    case_num = 1
    while case_num <= num_cases:
        determine_gophers(nights, max_gophers)
        case_num += 1