class TreeNode(object):
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None
        self.parent = None


# 1.构造二叉树
def construct(preorder_list, inorder_list):
    """
    输入二叉树的前序遍历和中序遍历的结果，重建该二叉树
    假设二叉树数中不含重复的值
    返回根节点
    :param preorder_list: 前序遍历结果列表
    :param inorder_list: 中序遍历结果列表
    :return: 根节点
    """
    pre_length = len(preorder_list)
    in_length = len(inorder_list)
    if pre_length == 0 or in_length == 0 or pre_length != in_length:
        print('invalid input.')
        return

    pre_start = in_start = 0
    pre_end = in_end = pre_length-1
    root = TreeNode()
    root_value = preorder_list[0]
    root.value = root_value

    if pre_length == 1:
        if root_value == inorder_list[0]:
            return root
        else:
            print('invalid input.')
            return

    # 寻找根节点在中序序列中的索引
    root_index = -1
    for index, value in enumerate(inorder_list):
        if value == root_value:
            root_index = index
            break
    if root_index == -1:
        print('root value dose not found in inorder_list, invalid input.')
        return

    left_pre_length = root_index - pre_start  # 左子树大小（结点的个数）
    left_pre_end = pre_start + left_pre_length  # 左子树最后一个结点在前序序列中的索引位置

    # 构建左子树
    if left_pre_length > 0:
        root.left = construct(preorder_list[pre_start+1: left_pre_end+1],
                              inorder_list[in_start:root_index])
    # 构建右子树
    if left_pre_length < pre_end - pre_start:
        root.right = construct(preorder_list[left_pre_end+1:],
                               inorder_list[root_index+1: in_end+1])
    return root


# 2.找出二叉树的下一个结点
def get_next(node):
    """
    给定二叉树中的一个结点，找出中序遍历序列的下一个结点
    :param node:
    :return:
    """
    if node is None:
        return

    p_next = None
    if node.right is not None:  # 如果含有右子树
        p_right = node.right
        while p_right.left is not None:  # 找出右子树中的最左子结点
            p_right = p_right.left
        p_next = p_right
    elif node.parent is not None:
        p_current = node
        p_parent = node.parent
        while p_parent is not None and p_parent.left != p_current:
            p_current = p_parent
            p_parent = p_parent.parent
        p_next = p_parent
    return p_next


# 3.前序遍历打印
def print_preorder(root):
    if root:
        print(root.value)
        print_preorder(root.left)
        print_preorder(root.right)


# 4.输入两颗二叉树A和B，判断B是不是A的子结构
def has_subtree(root1, root2):
    result = False
    if root1 and root2:
        if root1.value == root2.value:
            result = find_subtree(root1, root2)
        if not result:
            result = has_subtree(root1.left, root2)
        if not result:
            result = has_subtree(root1.right, root2)
    return result


def find_subtree(root1, root2):
    if root2 is None:
        return True

    if root1 is None:
        return False

    if root1.value != root2.value:
        return False

    return find_subtree(root1.left, root2.left) and \
        find_subtree(root1.right, root2.right)


# 5.求二叉树镜像
def reverse_bintree(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        return

    root.left, root.right = root.right, root.left

    if root.left:
        reverse_bintree(root.left)
    if root.right:
        reverse_bintree(root.right)

    return root


# 求二叉树的深度
def tree_depth(root):
    if root is None:
        return 0

    left_depth = tree_depth(root.left)
    right_depth = tree_depth(root.right)

    return left_depth+1 if left_depth > right_depth else right_depth+1



if __name__ == '__main__':
    pre_lst = []
    in_lst = []
    rootnode = construct(pre_lst, in_lst)
    print_preorder(rootnode)
