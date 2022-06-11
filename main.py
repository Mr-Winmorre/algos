# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Any

from adjacency_list import AdjList
from adjacency_matrix import AdjacencyMatrix
from collections import deque

from bellman_ford import BellmanFordGraph
from bst import BstAlgo
from dfs import Dfs


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def fizz_buzz(a: list):
    fb = []
    for i in a:
        if i % 3 == 0 and i % 5 == 0:
            fb.append(f'fizz buzz {i}')
        elif i % 3 == 0:
            fb.append(f'fizz {i}')
        elif i % 5 == 0:
            fb.append(f'buzz {i}')

    return fb


def dfs(visited: set, graph: dict, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def bfs(gr: dict, root):
    v = set()
    q = deque([root])
    v.add(root)
    while q:
        # deque a vertex from queue
        vertex = q.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # equeue it
        for neighbour in gr[vertex]:
            if neighbour not in v:
                v.add(neighbour)
                q.append(neighbour)


def bubble_sort(a: list):
    l = len(a)
    for i in range(l):
        for j in range(0, l - i - 1):
            # compare two adjacent elements
            if a[j] > a[j + 1]:
                # swap the positions of these two elements
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return a


def selection_sort(a: list, s: int):
    for step in range(s):
        min_idx = step
        for i in range(step + 1, s):
            if a[i] < a[min_idx]:
                min_idx = i
        # put min at the correct position
        (a[step], a[min_idx]) = (a[min_idx], a[step])

    return a


def insertion_sort(a: list):
    for step in range(1, len(a)):
        key = a[step]
        j = step - 1

        # compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        # place key at after the element just smaller than it
        a[j + 1] = key


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # print(fizz_buzz([i for i in range(1, 16, 1)]))
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]

    # bst = BstAlgo(data=0)
    # for num in nums:
    #     bst.insert(num)
    # print("Preorder ::::")
    # print(bst.preorder([]))
    # print("####")
    #
    # print("postorder::: ")
    # print(bst.postorder([]))
    #
    # print("inorder::::")
    # print(bst.inorder([]))
    # print("*****")
    #
    # print(bst.get_min())
    # print(bst.get_max())

    g = AdjacencyMatrix(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    # g.print_matrix()

    # g.print_rows()
    # print("###############")
    # print(g.show_data())

    # Adjacency List
    v = 5
    # graph = AdjList(5)
    # graph.add_edge(0, 1)
    # graph.add_edge(0, 2)
    # graph.add_edge(0, 3)
    # graph.add_edge(1, 2)
    #
    # graph.print_agraph()
    # dfs
    visited = set()
    graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0', '5']),
             '3': set(['1']),
             '4': set(['2', '3']),
             '5': set([])}
    # dfs(visited, graph, '0')
    # print(visited)
    bfs(graph, '1')

    bg = BellmanFordGraph(5)
    bg.add_edge(0, 1, 5)
    bg.add_edge(0, 2, 4)
    bg.add_edge(1, 3, 3)
    bg.add_edge(2, 1, 6)
    bg.add_edge(3, 2, 2)

    # bg.bellman_ford(0)

    data = [-2, 45, 0, 11, -9]
    ss = len(data)
    print(selection_sort(data, ss))
    # print(bubble_sort(data))
