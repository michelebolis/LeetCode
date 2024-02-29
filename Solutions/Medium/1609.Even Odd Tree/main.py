from solution import Solution
from solution import TreeNode

def from_list(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node

def test(list) :
    root = from_list(list)
    print(Solution.isEvenOddTree(null, root))

null = None
test([1,10,4,3,null,7,9,12,8,6,null,null,2])
test([5,4,2,3,3,7])
test([5,9,1,3,5,7])