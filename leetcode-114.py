class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None

            leftTrail = dfs(root.left)
            rightTrail = dfs(root.right)

            if root.left:
                leftTrail.right = root.right
                root.right = root.left
                root.left = None

            last = rightTrail or leftTrail or root

            return last

        dfs(root)

# Morse Traveral - O(1) space

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                pred = cur.left

                while pred.right:
                    pred = pred.right

                pred.right = cur.right
                cur.right = cur.left
                cur.left = None

            cur = cur.right