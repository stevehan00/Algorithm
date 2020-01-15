'''
Breath First Search(너비 우선 탐색)
같은 level에 있는 node들을 먼저 순회하는 방식
'''


def b_f_s(graph, start_node):
    visit = [] #방문했던 node
    queue = [] #방문할 node

    queue.append(start_node)

    while queue:
        node = queue.pop(0) #같은 level의 node부터 순회하기 위해
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


'''
Depth First Search (깊이 우선 탐색)
한 노드의 sub node끝까지 순회한 다음에 다시 돌아와서 다른 node의 sub node 끝까지 탐색하는 구조이다.
'''


def d_f_s(graph, start_node):
    visit = [] #방문했던 node
    stack = [] #방문할 node

    stack.append(start_node)

    while stack:
        node = stack.pop() #sub node부터 순회하기 위해
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit