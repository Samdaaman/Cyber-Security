from typing import List, Tuple
from pwn import *


# class Astar:

#     def __init__(self, matrix):
#         self.mat = self.prepare_matrix(matrix)

#     class Node:
#         def __init__(self, x, y, weight=0):
#             self.x = x
#             self.y = y
#             self.weight = weight
#             self.heuristic = 0
#             self.parent = None

#         def __repr__(self):
#             return str(self.weight)

#     def print(self):
#         for y in self.mat:
#             print(y)

#     def prepare_matrix(self, mat):
#         matrix_for_astar = []
#         for y, line in enumerate(mat):
#             tmp_line = []
#             for x, weight in enumerate(line):
#                 tmp_line.append(self.Node(x, y, weight=weight))
#             matrix_for_astar.append(tmp_line)
#         return matrix_for_astar

#     def equal(self, current, end):
#         return current.x == end.x and current.y == end.y

#     def heuristic(self, current, other):
#         return abs(current.x - other.x) + abs(current.y - other.y)

#     def neighbours(self, matrix, current):
#         neighbours_list = []
#         # if current.x - 1 >= 0 and current.y - 1 >= 0 and matrix[current.y - 1][current.x - 1].weight is not None:
#         #     neighbours_list.append(matrix[current.y - 1][current.x - 1])
#         if current.x - 1 >= 0 and matrix[current.y][current.x - 1].weight is not None:
#             neighbours_list.append(matrix[current.y][current.x - 1])
#         # if current.x - 1 >= 0 and current.y + 1 < len(matrix) and matrix[current.y + 1][current.x - 1].weight is not None:
#         #     neighbours_list.append(matrix[current.y + 1][current.x - 1])
#         if current.y - 1 >= 0 and matrix[current.y - 1][current.x].weight is not None:
#             neighbours_list.append(matrix[current.y - 1][current.x])
#         if current.y + 1 < len(matrix) and matrix[current.y + 1][current.x].weight is not None:
#             neighbours_list.append(matrix[current.y + 1][current.x])
#         # if current.x + 1 < len(matrix[0]) and current.y - 1 >= 0 and matrix[current.y - 1][current.x + 1].weight is not None:
#         #     neighbours_list.append(matrix[current.y - 1][current.x + 1])
#         if current.x + 1 < len(matrix[0]) and matrix[current.y][current.x + 1].weight is not None:
#             neighbours_list.append(matrix[current.y][current.x + 1])
#         # if current.x + 1 < len(matrix[0]) and current.y + 1 < len(matrix) and matrix[current.y + 1][current.x + 1].weight is not None:
#         #     neighbours_list.append(matrix[current.y + 1][current.x + 1])
#         return neighbours_list

#     def build(self, end):
#         node_tmp = end
#         path = []
#         while (node_tmp):
#             path.append([node_tmp.x, node_tmp.y])
#             node_tmp = node_tmp.parent
#         return list(reversed(path))

#     def run(self, point_start, point_end):
#         matrix = self.mat
#         start = self.Node(point_start[0], point_start[1])
#         end = self.Node(point_end[0], point_end[1])
#         closed_list = []
#         open_list = [start]

#         while open_list:
#             current_node = open_list.pop()

#             for node in open_list:
#                 if node.heuristic < current_node.heuristic:
#                     current_node = node

#             if self.equal(current_node, end):
#                 return self.build(current_node)

#             for node in open_list:
#                 if self.equal(current_node, node):
#                     open_list.remove(node)
#                     break

#             closed_list.append(current_node)

#             for neighbour in self.neighbours(matrix, current_node):
#                 if neighbour in closed_list:
#                     continue
#                 if neighbour.heuristic < current_node.heuristic or neighbour not in open_list:
#                     neighbour.heuristic = neighbour.weight + self.heuristic(neighbour, end)
#                     neighbour.parent = current_node
#                 if neighbour not in open_list:
#                     open_list.append(neighbour)

#         return None


class Astar:
    def __init__(self, mat):
        self.mat = mat

    def run(self, start: Tuple[int, int], end: Tuple[int, int]):
        s_x, s_y = start
        e_x, e_y = end
        
        return self.step(s_x, s_y, -1, -1, e_x, e_y, [start])

            

    def step(self, i_x, i_y, p_x, p_y, e_x, e_y, route: List[Tuple[int, int]]):
        neighbours = [
            (i_x+1, i_y),
            (i_x-1, i_y),
            (i_x, i_y+1),
            (i_x, i_y-1)
        ]

        for n_x, n_y in neighbours:
            if (n_x != p_x or n_y != p_y) and n_x >= 0 and n_x < len(self.mat[0]) and n_y >= 0 and n_y < len(self.mat) and self.mat[n_y][n_x] is not None:
                route_test = route.copy()
                route_test.append((n_x, n_y))
                if n_x == e_x and n_y == e_y:
                    return route_test
                test = self.step(n_x, n_y, i_x, i_y, e_x, e_y, route_test)
                if test is not None:
                    return test

r = remote('167.172.57.255', 30585)

r.recvuntil(b'>')
r.sendline(b'2')


while True:
    board = r.recvuntil(b'>')[2:-4]

    rows = board.replace(b' \n', b'\n').split(b'\n')

    mat = [row.replace(b'  ', b' ').split(b' ') for row in rows]

    mat = [
        [
            'f' if c == b'\xf0\x9f\x94\xa5'
            else 'N' if c == b'\xe2\x98\xa0\xef\xb8\x8f'
            else 'd' if c == b'\xf0\x9f\x92\x8e'
            else 'b' if c == b'\xf0\x9f\x94\xa9'
            else 'X'
            for c in row]
            for row in mat
    ]

    mat = [row[1:-1] for row in mat[1:-1]]

# mat = [
#     ['N', 'N', 'N', 'X', 'N', 'N', 'N', 'N', 'N', 'N'],
#     ['b', 'b', 'b', 'b', 'N', 'N', 'N', 'N', 'N', 'N'],
#     ['N', 'N', 'b', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
#     ['N', 'b', 'b', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
#     ['b', 'b', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
#     ['N', 'b', 'b', 'b', 'b', 'b', 'N', 'N', 'N', 'N'],
#     ['N', 'N', 'N', 'N', 'b', 'N', 'N', 'N', 'N', 'N'],
#     ['N', 'N', 'b', 'b', 'b', 'b', 'N', 'N', 'N', 'N'],
#     ['b', 'b', 'b', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
#     ['N', 'd', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
# ]

    debug = mat

    start = None
    end = None
    for y, row in enumerate(mat):
        for x, c in enumerate(row):
            if c == 'X':
                start = (x, y)
            elif c == 'd':
                end = (x, y)

    # for row in mat:
    #     print(row)

    mat = [[None if c == 'N' else 0 for c in row] for row in mat]

    astar = Astar(mat)

    points = astar.run(start, end)
    # print(points)
    if points is None:
        for row in debug:
            print(row)

        print('-' * 30)
        for row in mat:
            print(['N' if c is None else '0' for c in row])
        print((start, end))

    commands = ''
    for i in range(1, len(points)):
        if points[i][0] > points[i-1][0]:
            commands += 'R'
        elif points[i][0] < points[i-1][0]:
            commands += 'L'
        else:
            commands += 'D'

    # print(commands)
    r.sendline(commands)
    score = r.recvline()
    print(score)
    print(r.recvline())

    if b'500' in score:
        r.interactive()
        break
