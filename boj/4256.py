import sys

class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

t = int(sys.stdin.readline())

def solve(inorder):
    if inorder:
        idx = inorder.index(pre_order.pop(0))

        node = TreeNode(inorder[idx])
        node.left = solve(inorder[:idx])
        node.right = solve(inorder[idx+1:])

        return node

def post_order(root):
    if root.left:
        post_order(root.left)
    if root.right:
        post_order(root.right)

    print(root.val, end=' ')

for _ in range(t):
    n = int(sys.stdin.readline())
    pre_order = list(map(int, sys.stdin.readline().split()))
    in_order = list(map(int, sys.stdin.readline().split()))

    r = solve(in_order)
    post_order(r)

    print()