import itertools as it
import numpy as np

answerBoardMatrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


class StateNode:
    def __init__(self, boardMatrix, parentStateNode=None):
        self.boardMatrix = boardMatrix
        self.parentStateNode = parentStateNode

    def __eq__(self, rhs):
        if type(rhs) is StateNode:
            return self.boardMatrix.tolist() == rhs.boardMatrix.tolist()
        elif type(rhs) is tuple:
            return self.boardMatrix.tolist() == rhs[1].boardMatrix.tolist()
        else:
            raise RuntimeError

    def __lt__(self, other):
        return True


def generate_possible_moves(boardMatrix):
    x, y = np.where(boardMatrix == 0)

    available_x = [x]
    available_y = [y]

    x_width, y_width = np.shape(boardMatrix)

    if x + 1 <= x_width - 1:
        available_x.append(x + 1)
    if x - 1 >= 0:
        available_x.append(x - 1)
    if y + 1 <= y_width - 1:
        available_y.append(y + 1)
    if y - 1 >= 0:
        available_y.append(y - 1)

    moves = filter(lambda m: (abs(m[0] - x) + abs(m[1] - y)) == 1, (it.product(available_x, available_y)))
    return list(moves)


def generate_next_state_nodes(stateNode):
    for move in generate_possible_moves(stateNode.boardMatrix):
        x = stateNode.boardMatrix.copy()
        x[x == 0], x[move] = x[move], x[x == 0]
        yield StateNode(x, stateNode)  # child nodes.


def did_reach_goal(stateNode):
    boardMatrix = stateNode.boardMatrix
    return all(boardMatrix.flatten() == list(range(0, 9))) or all(boardMatrix.flatten() == list(range(1, 9)) + [0])


def generate_random_puzzle():
    n = np.arange(9)
    np.random.shuffle(n)

    return np.reshape(n, [3, 3])

if __name__ == "__main__":
    x = generate_random_puzzle()
    print(x)