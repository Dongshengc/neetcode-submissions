class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ["+", "-", "*", "/"]

        operands = []

        for char in tokens:

            if char not in operators:
                operands.append(int(char))
                # print(operands)
                continue
            else:
                right_operand = operands.pop()
                left_operand = operands.pop()

                # print(right_operand, left_operand)
             
                if char == "+":
                    result = left_operand + right_operand 
                elif char == "-":
                    result = left_operand - right_operand 
                elif char == "*":
                    result = left_operand * right_operand 
                elif char == "/":
                    result = int(left_operand / right_operand) 

                operands.append(result)
                # print(operands)
        
        return operands.pop()
