# non stack solution

class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        cur = prev = res = 0
        cur_operation = "+"

        while i < len(s):
            cur_char = s[i]

            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1

                if cur_operation == "+":
                    res += cur
                    prev = cur

                elif cur_operation == "-":
                    res -= cur
                    prev = -cur

                elif cur_operation == "*":
                    res -= prev
                    res += prev * cur
                    prev = prev * cur

                else:
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)
                
                cur = 0

            elif cur_char != " ":
                cur_operation = cur_char

            i += 1

        return res
    
# stack solution

class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        op = "+"

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if (not ch.isdigit() and ch != ' ') or i >= len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    t = stack.pop()
                    stack.append(int(t/num))
                op = ch
                num = 0

        return sum(stack)