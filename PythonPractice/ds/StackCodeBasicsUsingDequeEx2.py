#Implement Stack class using a deque
#video link: https://www.youtube.com/watch?v=zwb3GmNAtFk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=8
from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


s1=Stack()
print(s1.is_empty())
s1.push("one")
s1.push("two")
print(s1.container)
print(s1.is_empty())
print(s1.peek())
print(s1.pop())
print(s1.container)
print(s1.container.__dir__())

#exercise: Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))

#Exercise2: Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
#is_balanced("({a+b})")     --> True
#is_balanced("))((a+b}{")   --> False
#is_balanced("((a+b))")     --> True
#is_balanced("))")          --> False
#is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))