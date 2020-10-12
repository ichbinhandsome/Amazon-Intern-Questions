'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n == 0: return ans
        def backtrack(left, right, temp):
            if len(temp) == 2 * n:
                temp = ''.join(temp)
                ans.append(temp)
                return
            if left > right:
                temp.append(')')
                backtrack(left, right+1, temp.copy())
                temp.pop()
            if left < n:
                temp.append('(')
                backtrack(left+1, right, temp.copy())
                temp.pop()
        backtrack(0, 0, [])
        return ans