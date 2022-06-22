#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # Greedy Algo:
        # 从下往上安装摄像头：跳过leaves这样安装数量最少，局部最优 -> 全局最优
        # 先给leaves的父节点安装，然后每隔两层节点安装一个摄像头，直到Head
        # 0: 该节点未覆盖
        # 1: 该节点有摄像头
        # 2: 该节点有覆盖
        
        result = 0
        # 从下往上遍历：后序（左右中）
        def traversal(curr: TreeNode) -> int:
            nonlocal result
            
            if not curr: return 2
            left = traversal(curr.left)
            right = traversal(curr.right)

            # Case 1:
            # 左右节点都有覆盖，该节点就当作新的叶节点
            if left == 2 and right == 2: 
                return 0

            # Case 2:存在有一个节点没被覆盖
                # left == 0 && right == 0 左右节点无覆盖
                # left == 1 && right == 0 左节点有摄像头，右节点无覆盖
                # left == 0 && right == 1 左节点有无覆盖，右节点摄像头
                # left == 0 && right == 2 左节点无覆盖，右节点覆盖
                # left == 2 && right == 0 左节点覆盖，右节点无覆盖
            elif left == 0 or right == 0: 
                result += 1
                return 1

            # Case 3:左右有一个节点有摄像头
                # left == 1 && right == 2 左节点有摄像头，右节点有覆盖
                # left == 2 && right == 1 左节点有覆盖，右节点有摄像头
                # left == 1 && right == 1 左右节点都有摄像头
            elif left == 1 or right == 1:
                return 2
            
            # 其他情况前段代码均已覆盖
            # 不必担心有一个子节点没覆盖，灵另一个子节点有摄像头的情况，
            # 因为先判断了有无覆盖，所以父节点会放摄像头头而不是被覆盖

        if traversal(root) == 0:
            # 有可能最后根节点没有覆盖，例如左右都是有覆盖的情况
            result += 1
            
        return result
# @lc code=end

'''
不要放在叶子节点，否则会浪费，也不放入根节点也会浪费
从下往上，，局部最优：让叶子节点的父节点安摄像头，
所用摄像头最少，整体最优：全部摄像头数量所用最少！

'''