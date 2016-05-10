# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Check out this video for further explanation https://www.youtube.com/watch?v=qT65HltK2uE

# But here are the key steps
# initialize two stacks ( one of them is just for processing , other stack is the output stack)

class Solution(object):
    def postorderTraversal(self, root):
        stack_1 , stack_2 = [],[]
        if root == None:
            return []
        else:
            # Seed the processing stack with the root element
            stack_1.append(root)
            while len(stack_1) > 0:
            # While the processing stack is not empty, pop the top element from the processing stack,push it to the result stack
            # And add it child nodes to the processing stack
            # Continue the above two steps and return the result stack in Inverted order at the end.
                temp_node = stack_1.pop()
                stack_2.append(temp_node.val)
                if temp_node.left:
                    stack_1.append(temp_node.left)
                if temp_node.right:
                    stack_1.append(temp_node.right)
            return stack_2[::-1]
