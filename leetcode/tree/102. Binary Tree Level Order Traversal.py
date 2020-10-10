from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iterative method
class Solution:
    def levelOrder(self, root):
        q = deque()
        result = []
        level = []
        if root:
            q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
            level = []
        return result


# # test case
# # Node4 = TreeNode(17, None, None)
# # Node3 = TreeNode(15, None, None)
# # Node2 = TreeNode(20, Node3, Node4)
# # Node1 = TreeNode(9, None, None)
# # root = TreeNode(3, Node1, Node2)
# #
# # lst = [root, Node1, Node2,]
# # solve = Solution()
# # print(solve.levelOrder(root))


# def __init__(self):
#     self.lst = []
#
# def levelOrder(self, root: TreeNode) -> List[List[int]]:
#     if root:
#         cur_level_lst = [root]
#     self.lst.append(root.val)
#     while len(cur_level_lst) != 0:
#         next_level_lst = self.helper(cur_level_lst)
#         cur_level_lst = next_level_lst
#         cur_level_lst_val = []
#         if cur_level_lst is None:
#             break
#         for item in cur_level_lst:
#             cur_level_lst_val.append(item.val)
#         self.lst.append(cur_level_lst_val)
#     return self.lst
#
#
# def helper(self, array):
#     next_level_lst = []
#     for item in array:
#         if item.left is not None:
#             next_level_lst.append(item.left)
#         if item.right is not None:
#             next_level_lst.append(item.right)
#     if len(next_level_lst) == 0:
#         return None
#     else:
#         return next_level_lst
