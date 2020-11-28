class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = []


def subtreeMaxAvg(root: TreeNode) -> TreeNode:
    if root is None:
        return 0

    averages = {}
    queue = [root]

    while queue:
        temp = queue.pop(0)
        count = 0
        running_sum = 0
        running_q = [temp]

        while running_q:
            count += 1
            temp_node = running_q.pop(0)
            running_sum += temp_node.val
            if temp_node.children:
                running_q.extend(temp_node.children)
                queue.extend(temp_node.children)

        averages[temp.val] = running_sum / count

    averages_list = list(averages.items())
    averages_list.sort(reverse=True, key=lambda x: x[1])

    return averages_list[0][0]


tree1 = TreeNode(1)
tree1.children.extend([TreeNode(-5), TreeNode(21), TreeNode(5), TreeNode(-1)])

tree2 = TreeNode(1)
subtree21 = TreeNode(-5)
subtree21.children.extend([TreeNode(1), TreeNode(2)])
subtree22 = TreeNode(13)
subtree22.children.extend([TreeNode(4), TreeNode(-2)])
tree2.children.extend([subtree21, subtree22, TreeNode(4)])

print(subtreeMaxAvg(tree1))  # 21
print(subtreeMaxAvg(tree2))  # 13
