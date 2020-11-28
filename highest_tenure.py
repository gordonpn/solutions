class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = []


def highest_tenure(president: TreeNode):
    if president is None:
        return None

    queue = [president]
    avg_tenure = {}

    while queue:
        node = queue.pop(0)
        team_count = 0
        tenure_sum = 0
        curr_avg_queue = [node]

        while curr_avg_queue:
            temp_node = curr_avg_queue.pop(0)
            team_count += 1
            tenure_sum += temp_node.val

            if temp_node.children:
                curr_avg_queue.extend(temp_node.children)
                queue.extend(temp_node.children)

        if team_count > 1:
            avg_tenure[node.val] = tenure_sum / team_count

    avg_tenure_list = list(avg_tenure.items())
    avg_tenure_list.sort(key=lambda x: x[1], reverse=True)
    return avg_tenure_list[0][0]


tree2 = TreeNode(20)
subtree21 = TreeNode(12)
subtree21.children.extend([TreeNode(11), TreeNode(2), TreeNode(3)])
subtree22 = TreeNode(18)
subtree22.children.extend([TreeNode(15), TreeNode(8)])
tree2.children.extend([subtree21, subtree22])

print(highest_tenure(tree2))  # 18
