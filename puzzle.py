import state as state
import numpy as np
import time

from state import StateNode
from collections import deque
from heapq import heappush, heappop
from pprint import pprint


def solution(solutionNode, rootNode):
    states = []
    n = solutionNode

    while n is not rootNode:
        states.append(n.boardMatrix)
        n = n.parentStateNode


    return {"SOLUTION":list(reversed(states)),
            "PATH COST": str(len(states))}


def breadth_first_search(boardMatrix):
    root = StateNode(boardMatrix)
    frontier = deque()
    frontier.append(root)
    visited = list()
    start = time.time()
    if state.did_reach_goal(root):
        return solution(root, root)
    depth = list()
    maxdepth = 0
    while len(frontier) > 0:
        cur = frontier.popleft()
        if cur not in visited:
            visited.append(cur)
        for n in state.generate_next_state_nodes(cur):
            depth.append(n)
            if len(depth) > maxdepth:
                maxdepth = len(depth)
            if state.did_reach_goal(n):
                print(f'Running Time: {"{:.4f}".format(time.time() - start)} seconds')
                print(f'Expanded Nodes Count: {len(visited)}')
                print(f'depth: {maxdepth}')

                return solution(n, root)
            if n not in frontier and n not in visited:
                frontier.append(n)
    return None


def depth_first_search(boardMatrix):
    root = StateNode(boardMatrix)
    frontier = list()
    visited = list()
    start_time = time.time()
    if state.did_reach_goal(root):
        return solution(root, root)
    frontier.append(root)
    depthList = list()
    maxDepth = 0

    while len(frontier) > 0:
        cur = frontier.pop()
        if cur not in visited:
            visited.append(cur)
        for n in state.generate_next_state_nodes(cur):
            depthList.append(n)
            if len(depthList) > maxDepth:
                maxDepth = len(depthList)

            if state.did_reach_goal(n):
                print(f'Running Time: {"{:.4f}".format(time.time() - start_time)} seconds')
                print(f'Expanded Nodes Count: {len(visited)}')
                print(f'depth: {maxDepth}')

                return solution(n, root)
            if n not in frontier and n not in visited:
                frontier.append(n)

    return None




def astar_search(boardMatrix, heuritic_function):
    start_time = time.time()
    root = StateNode(boardMatrix)
    visited = list()
    frontier = []
    if state.did_reach_goal(root):
        return solution(root, root)

    def _heappush(node):
        heappush(frontier, (len(solution(node, root)) + heuritic_function(node.boardMatrix), node))

    _heappush(root)
    depthList=list()
    maxdepth=0
    while len(frontier) > 0:
        cur = heappop(frontier)
        cur = cur[1]
        if state.did_reach_goal(cur):
            print(f'Running Time: {"{:.4f}".format(time.time() - start_time)} seconds')
            print(f'Expanded Nodes Count: {len(visited)}')
            print(f'depth: {maxdepth}')


            return solution(cur, root)
        visited.append(cur)
        for n in state.generate_next_state_nodes(cur):
            depthList.append(n)
            if len(depthList) > maxdepth:
                maxdepth = len(depthList)


            if n not in visited and n not in frontier:
                _heappush(n)
            elif n in frontier:
                frontier.remove(n)
                n.parentStateNode = cur
                _heappush(n)
   # print(f'depth: {maxdepth}')


def manhattan_distance(boardMatrix):
    dist = 0
    for (x, y), value in np.ndenumerate(boardMatrix):
        xsolution, ysolution = np.where(state.answerBoardMatrix == value)
        dist += abs(x - xsolution) + abs(y - ysolution)

    return dist / 2


def euclidian_distance(boardMatrix):
    dist = 0
    for (x, y), value in np.ndenumerate(boardMatrix):
        xsolution, ysolution = np.where(state.answerBoardMatrix == value)
        dist += (x - xsolution) ** 2 + (y - ysolution) ** 2
        dist = np.sqrt(dist)

    return dist


if __name__ == "__main__":
    #problem = np.reshape([0, 8, 7, 6, 5, 4, 3, 2, 1], [3, 3])
    #problem = np.reshape([3, 1, 2, 0, 4, 5, 6, 7, 8], [3, 3])
    problem = np.reshape([1, 2, 5, 3, 4, 0, 6, 7, 8], [3, 3])
    ans = True
    while ans:
        print("""
        1.BFS
        2.DFS
        3.A* Manhatten Distane
        4.A* Euclidean Distance 
        5.Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            print("BFS\n")
            pprint(breadth_first_search(problem))
            print("\n\n---------------------------------")
        elif ans == "2":
            print("DFS\n")
            pprint(depth_first_search(problem))
            print("\n\n---------------------------------")

        elif ans == "3":
            print("A* MANHATTAN\n")
            pprint(astar_search(problem, manhattan_distance))
            print("\n\n---------------------------------")

        elif  ans == "4":
            print("A* EUCLIDIAN\n")
            pprint(astar_search(problem, euclidian_distance))
        elif ans == "5":
            print("\n Goodbye")
            ans = None
        else:
            print("\n Not Valid Choice Try again")

    """print("DFS\n")
    pprint(depth_first_search(np.reshape([1, 2, 3, 4, 5, 6, 7, 0, 8], [3, 3])))
    print("\n\n---------------------------------")"""




