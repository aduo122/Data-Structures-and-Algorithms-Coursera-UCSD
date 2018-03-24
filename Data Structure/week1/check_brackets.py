# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    flag = 0
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            temp_brackets = Bracket(next,i)
            opening_brackets_stack.append(temp_brackets)
            pass

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if opening_brackets_stack == []:
                print(i+1)
                flag = 1
                break
            temp_B = opening_brackets_stack.pop()
            if not temp_B.Match(next):
                print(i+1)
                flag = 1
                break
    if flag == 0 and len(opening_brackets_stack) != 0:
        print (opening_brackets_stack[0].position+1)
    elif flag == 0 :
        print('Success')

    # Printing answer, write your code here
