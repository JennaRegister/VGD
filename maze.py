import random
import pygame

def make_2d_array_of(rows,cols,value):
    """creates and returns a 2d array filled with 'value' that can be indexed with [r][c].

    Typically rows correspond to the "y" direction and cols to the "x" direction. be careful with indexes.
    """
    return [[value for i in range(cols)] for j in range(rows)]

class Maze(object):

    def __init__(self, rows, columns, start=(0,0)):
        self.rows = rows
        self.cols = columns
        self.start = start
        self.fill_all_walls()

    def fill_all_walls(self):
        """creates self.vwalls and self.hwalls arrays, and fills them all with True
        """
        # vwalls[r][c] is a wall between [r][c] and [r][c+1]
        # hwalls[r][c] is a wall between [r][c] and [r+1][c]
        self.vwalls = make_2d_array_of(self.rows, self.cols-1, True)
        self.hwalls = make_2d_array_of(self.rows-1, self.cols, True)

    def set_wall_between(self, posA, posB, value, verbose=False):
        """if posA and posB are adjacent (cardinal directions), then sets the wall between them to value
        """

        # dr is difference-in-rows
        dr = posB[0] - posA[0]
        # dc is difference-in-cols
        dc = posB[1] - posA[1]

        # posA and posB are adjacent if-and-only-if the difference in rows is 1 OR the difference in columns is 1 but
        # not both. So, the difference in rows *plus* the difference in columns must be exactly 1
        if abs(dr) + abs(dc) is not 1:
            if verbose:
                print("can't remove wall between", posA, "and", posB)
            return # stops the function (coordinates are invalid)

        # if they are separated vertically (by a row)
        if abs(dr) == 1:
            # fill_all_walls() says "hwalls[r][c] is a wall between [r][c] and [r+1][c]"
            # so, the wall between posA and posB is hwalls[min row between the two][c] (they have the same c)
            minr = min(posB[0], posA[0])
            self.hwalls[minr][posA[1]] = value
        # analogous for horizontal separation
        elif abs(dc) == 1:
            minc = min(posB[1], posA[1])
            self.vwalls[posA[0]][minc] = value

    def can_move(self, posA, posB):
        """you can move from posA to posB if-and-only-if they are adjacent AND there is no wall between them
        """
        # dr is difference-in-rows
        dr = posB[0] - posA[0]
        # dc is difference-in-cols
        dc = posB[1] - posA[1]

        # posA and posB are adjacent if-and-only-if the difference in rows is 1 OR the difference in columns is 1 but
        # not both. So, the difference in rows *plus* the difference in columns must be exactly 1
        if abs(dr) + abs(dc) is not 1:
            # not adjacent, hence can't move.
            return False

        # see comments in set_wall_between for how minr and minc work
        if abs(dr) == 1:
            minr = min(posB[0], posA[0])
            # can move if wall is false
            return not self.hwalls[minr][posA[1]]
        elif abs(dc) == 1:
            minc = min(posB[1], posA[1])
            return not self.vwalls[posA[0]][minc]

    def generate(self, start=None, end=None):
        """GENERATES THE MAZE

        It works by 'walking' from the start in a random direction every step. It never walks back onto places it has
            already visited. Sometimes it will get stuck with no remaining options, in which case it looks back at
            everywhere it has been and randomly picks a place to restart from *only if that place has some yet-unexplored
            neighbors*.
        If 'end' is specified, it will never walk 'past' the end nor choose 'end' and a place to restart from. This
            guarantees that 'end' is at some dead-end of a path rather than in the middle. You don't need to specify an end.
        """

        # (optionally) override where self.start is
        if start is not None:
            self.start = start

        # initially set all walls to True
        self.fill_all_walls()

        # visited_cells[r][c] will be set to True when 'walk' reaches them
        visited_cells = make_2d_array_of(self.rows, self.cols, False)

        # we need to keep track of how many unvisited neighbors each cell has, so that when picking a new place to start
        # from we can say "find somewhere already visited but with more than zero unvisited neighbors"
        num_unvisited_neighbors = make_2d_array_of(self.rows, self.cols, 4)
        # edges have 1 fewer neighbor
        for r in range(self.rows):
            num_unvisited_neighbors[r][0] = 3
            num_unvisited_neighbors[r][self.cols-1] = 3
        for c in range(self.cols):
            num_unvisited_neighbors[0][c] = 3
            num_unvisited_neighbors[self.rows-1][c] = 3
        # corners have only 2 neighbors
        num_unvisited_neighbors[0][0] = 2
        num_unvisited_neighbors[self.rows-1][self.cols-1] = 2
        num_unvisited_neighbors[self.rows-1][0] = 2
        num_unvisited_neighbors[0][self.cols-1] = 2

        # return a list of (r,c) positions
        def get_unvisited_neighbors(pos):
            """given pos (which itself is some (r,c)), return neighbors around it that haven't been visited. This
            function also makes sure not to return things outside the boundaries of the maze
            """
            ns = []
            r,c = pos
            if r > 0 and not visited_cells[r-1][c]:
                ns.append((r-1, c))
            if r < self.cols-1 and not visited_cells[r+1][c]:
                ns.append((r+1, c))
            if c > 0 and not visited_cells[r][c-1]:
                ns.append((r, c-1))
            if c < self.rows-1 and not visited_cells[r][c+1]:
                ns.append((r, c+1))
            return ns

        def get_all_neighbors(pos):
            ns = []
            r,c = pos
            if r > 0:
                ns.append((r-1, c))
            if r < self.cols-1:
                ns.append((r+1, c))
            if c > 0:
                ns.append((r, c-1))
            if c < self.rows-1:
                ns.append((r, c+1))
            return ns

        def random_position_at_least_1_unvisited():
            valid_indices = []

            for r in range(self.rows):
                for c in range(self.cols):
                    if (r,c) is not end and visited_cells[r][c] and num_unvisited_neighbors[r][c] > 0:
                        valid_indices.append((r,c))
            return random.choice(valid_indices)

        def visit(pos):
            if not visited_cells[pos[0]][pos[1]]:
                visited_cells[pos[0]][pos[1]] = True
                for n in get_all_neighbors(pos):
                    num_unvisited_neighbors[n[0]][n[1]] -= 1
                return True
            return False

        # begin a random walk at 'start'
        total_visited_cells = 0
        walk = self.start

        # we check total_visited_cells because it's faster to do this than check (every step) whether all cells are visited yet
        while total_visited_cells < self.rows * self.cols:
            if visit(walk):
                total_visited_cells += 1

            # get neighbors that have a different id (either unvisited or some other blob)
            neighbors = get_unvisited_neighbors(walk)

            # pick one at random if available
            if walk != end and len(neighbors) > 0:
                next_walk = random.choice(neighbors)
                # remove wall between current location and next one
                self.set_wall_between(walk, next_walk, False)
                walk = next_walk

            # got stuck on self.. may as well move on to the next part
            elif total_visited_cells < self.rows * self.cols:
                walk = random_position_at_least_1_unvisited()

    def draw(self, surf, color, hsize=10, vsize=10):
        # draw outside border
        pygame.draw.rect(surf, (0,200,0), [self.start[1]*vsize, self.start[0]*hsize, hsize, vsize])
        pygame.draw.rect(surf, color, [0,0,hsize*self.cols,vsize*self.rows], 1)
        for r in range(self.rows):
            for c in range(self.cols):
                if r < self.rows-1 and self.hwalls[r][c]:
                    x1,y1 = c * hsize, (r+1) * vsize
                    x2,y2 = (c+1) * hsize, (r+1) * vsize
                    pygame.draw.line(surf, color, (x1,y1), (x2,y2))
                if c < self.cols-1 and self.vwalls[r][c]:
                    x1,y1 = (c+1) * hsize, r * vsize
                    x2,y2 = (c+1) * hsize, (r+1) * vsize
                    pygame.draw.line(surf, color, (x1,y1), (x2,y2))

if __name__ == '__main__':
    pygame.init()
    import pygame.locals as pl

    s = (random.randint(0,19), random.randint(0,19))
    m = Maze(20,20, s)

    m.generate()

    main_surface = pygame.display.set_mode((400,400))

    exit = False
    while not exit:
        for evt in pygame.event.get():
            if evt.type == pl.QUIT:
                exit = True
            if evt.type == pl.MOUSEBUTTONUP:
                s = (random.randint(0,19), random.randint(0,19))
                m.generate(s)

        main_surface.fill((0,0,0))
        m.draw(main_surface, (255,255,255), 20, 20)
        pygame.display.update()
