#
#  A famous ancient question in this context is:
#  "How many distinct arrangements of n pairs of left-right parentheses are there all of which close?"
#  The answer to this question is called the n-th Catalan number, C(n).
#  Here are the first few answers:
#   * C(1)=1         ( )
#   * C(2)=2         ()() and (())
#   * C(3)=5         ()()(), ()(()), (())(), (()()) and ((()))
#
#
# Generating all combinations of well formed parentheses is a typical example of catalan numbers.
# You can use the links at the bottom here if you are not aware of the catalan numbers since they
# are at the heart of the exercise.
# Let time complexity for the generating all combinations of well-formed parentheses is f(n),
# then,
# f(n) = g(n) * h(n) where g(n) is the time complexity for calculating nth catalan number,
# and h(n) is the time required to copy this combination to result array.
#
# Therefore, f(n) = catalan(n) * O(n) which is O((4^n/n^1.5)*(n)).
# Broadly saying just remember that this is a typical example of catalan number
# and it's time complexity is similar to how catalan(n) is got.
# Further readings in to catalan numbers:
#
# https://en.wikipedia.org/wiki/Catalan_number
# https://www.youtube.com/watch?v=GlI17WaMrtw
# https://www.youtube.com/watch?v=eoofvKI_Okg
#
#

# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)

# iterative solution
class Solution(object):
    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     result, curr = [], []
    #     stk = [(1, (n, n))]
    #     while stk:
    #         step, args = stk.pop()
    #         if step == 1:
    #             left, right = args
    #             if left == 0 and right == 0:
    #                 result.append("".join(curr))
    #             if left < right:
    #                 stk.append((3, tuple()))
    #                 stk.append((1, (left, right-1)))
    #                 stk.append((2, (')')))
    #             if left > 0:
    #                 stk.append((3, tuple()))
    #                 stk.append((1, (left-1, right)))
    #                 stk.append((2, ('(')))
    #         elif step == 2:
    #             curr.append(args[0])
    #         elif step == 3:
    #             curr.pop()
    #     return result


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack, result = [('', 0, 0)], []
        while stack:
            # current parentheses combination, number of left/right parentheses used
            parentheses, numLeft, numRight = stack.pop()
            if numRight == n:
                # done, add to result
                result.append(parentheses)
            else:
                if numLeft < n:
                    stack.append((parentheses + '(', numLeft+1, numRight))
                if numRight < numLeft:
                    # only add right parentheses if more left parentheses have been used
                    stack.append((parentheses + ')', numLeft, numRight+1))
        return result

# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)
# recursive solution
class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generateParenthesisRecu(left, right, curr, result):
            if left == 0 and right == 0:
                result.append("".join(curr))
            if left > 0:
                curr.append('(')
                generateParenthesisRecu(left-1, right, curr, result)
                curr.pop()
            if left < right:
                curr.append(')')
                generateParenthesisRecu(left, right-1, curr, result)
                curr.pop()

        result = []
        generateParenthesisRecu(n, n, [], result)
        return result
