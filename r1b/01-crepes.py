from enum import Enum

class Direction(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

class Person():
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.dir = d

def cart_sink(num_people, grid_size):
    grid = [ [ 0 for i in range(grid_size) ] for i in range(grid_size) ]
    for i in range(num_people):
        p = read_person()
        increment_grid(p, grid, grid_size)

    biggest_num_people = -1
    targets = []
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[y][x] > biggest_num_people:
                biggest_num_people = grid[y][x]
                targets = []

            if grid[y][x] == biggest_num_people:
                targets.append( (x,y) )

    if len(targets) > 1:
        targets.sort()

    return targets[0]

def read_person():
    [xs,ys,ds] = input().split(" ")
    x = int(xs)
    y = int(ys)
    d = Direction(ds)
    return Person(x,y,d)

def increment_grid(person, grid, max_coord):
    if person.dir == Direction.NORTH:
        startx = 0
        endx = max_coord
        starty = person.y + 1
        endy = max_coord
    elif person.dir == Direction.SOUTH:
        startx = 0
        endx = max_coord
        starty = 0
        endy = person.y
    elif person.dir == Direction.EAST:
        startx = person.x + 1
        endx = max_coord
        starty = 0
        endy = max_coord
    elif person.dir == Direction.WEST:
        startx = 0
        endx = person.x
        starty = 0
        endy = max_coord

    for y in range(starty, endy):
        for x in range(startx, endx):
            grid[y][x] += 1


if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        people,size = [int(i) for i in input().split(" ")]
        x,y = cart_sink(people, size+1)
        print("Case #{}: {} {}".format(case_num, x, y))
        case_num += 1