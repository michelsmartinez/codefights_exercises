
"""
You have a string s that consists of English letters, 
punctuation marks, whitespace characters, and brackets.
It is guaranteed that the parentheses in s form a regular bracket sequence.
Your task is to reverse the strings contained in each pair 
of matching parentheses, starting from the innermost pair.
The results string should not contain any parentheses.

Example

For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".
"""

def invertparent(s):
    buffer = ""
    i = 0
    while s[i] != ')':
        i += 1
    j = i
    while s[j] != '(':
        j -= 1

    buffer += s[:j]
    buffer += s[i-1:j:-1]
    buffer += s[i+1:]
    return buffer


def reverseParentheses(s):
    while '(' in s or ')' in s:
        s = invertparent(s)

    return s
