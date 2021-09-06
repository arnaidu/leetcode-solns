from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [["()"]]
        while len(ans) < n:
            next_ans = set()
            for string in ans[len(ans) - 1]:
                for j in range(len(string)):
                    next_ans.add(string[0:j+1] + "()" + string[j + 1:])
            ans.append(list(next_ans))
        return sorted(ans[n - 1])

if __name__ == "__main__":
    soln = Solution()
    n = 4
    output = soln.generateParenthesis(n)
    expected = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    assert(output == expected)
