from collections import deque


class Solution(object):
    def averageOfLevels(self, root):
        ans = []
        queue = deque([root])
        while queue:
            s = 0
            n = len(queue)
            for _ in range(n):
                top = queue.popleft()
                s += top.val
                if top.left:
                    queue.append(top.left) 
                if top.right:
                    queue.append(top.right)
            ans.append(float(s) / n)
        return ans