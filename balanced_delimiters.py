# HackerRank problem Balanced Delimiters:
# https://www.hackerrank.com/contests/programming-interview-questions/challenges/balanced-delimiters
# Solution modified to return "True"/"False" instead of printing.

def is_matched(bracket_set):
    stack = []
    matches = {"(":")", "[":"]", "{":"}"}
    for delim in bracket_set:
        if delim in matches:
            stack.append(delim)
        elif delim in matches.values():
            if stack and matches[stack[-1]] == delim:
                stack.pop()
            else:
                return "False"
    else:
        return "True" if not stack else "False"