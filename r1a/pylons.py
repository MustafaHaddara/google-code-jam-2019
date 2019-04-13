class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.seen = False

    def __repr__(self):
        return "Cell r:{}, c:{}".format(self.r, self.c)

def find_path(r, c):
    path = [ None ] * (r*c)
    all_cells = []
    for i in range(r):
        for j in range(c):
            all_cells.append(Cell(i,j))

    for starting in all_cells:
        pos = 0
        path[pos] = starting
        possible = get_path_from_start(path, all_cells, starting, pos+1)
        if possible:
            return possible, path
        # clean up after ourselves, this node sucks
        path[pos] = None
    return False, []

def get_path_from_start(path, all_cells, current, position):
    if position == len(path):
        return True

    options = get_options_from(current, path, all_cells)
    if len(options) == 0:
        return False

    for option in options:
        path[position] = option
        possible = get_path_from_start(path, all_cells, option, position+1)
        if possible:
            return possible, path
        # clean up after ourselves, this node sucks
        path[position] = None

def get_free_cells(all_cells):
    return list(filter(lambda cell: not cell.seen, all_cells))

def get_options_from(cell, visited, all_cells):
    options = []
    for c in all_cells:
        if c == cell:
            continue
        if c in visited:
            continue
        if cell.r == c.r or cell.c == c.c:
            continue
        slope = abs((cell.r - c.r) / (cell.c - c.c))
        if slope == 1:
            continue
        options.append(c)
    return options

if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        r,c = [int(i) for i in input().split(" ")]
        possible, path = find_path(r,c)
        print("Case #{}: {}".format(case_num, "POSSIBLE" if possible else "IMPOSSIBLE"))
        if possible:
            for cell in path:
                print("{} {}".format(cell.r+1, cell.c+1))
        case_num += 1