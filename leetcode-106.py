class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        
        root_val = postorder[-1]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        return root

# Optimized Solution - O(n) -> Uses a hashmap for indexing and uses boundaries instead of slicing
class Solution:
    def buildTree(self, inorder, postorder):
        # Map each value to its index in inorder for O(1) lookup
        inorderIdx = {v: i for i, v in enumerate(inorder)}

        def helper(l, r):
            # Base case: no elements to construct the subtree
            if l > r:
                return None

            # Last element in postorder is the root of current subtree
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Split inorder into left and right parts using root index
            idx = inorderIdx[root_val]

            # Build right first because we are consuming postorder from the end
            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)

            return root

        return helper(0, len(inorder) - 1)
