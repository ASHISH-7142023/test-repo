"""Mathematical expression parser and evaluator using the Shunting-Yard algorithm."""

import re
from typing import List


PRECEDENCE = {
    "+": 1, "-": 1,
    "*": 2, "/": 2,
    "^": 3,
}

RIGHT_ASSOCIATIVE = {"^"}


def tokenize_expression(expr: str) -> List[str]:
    """Tokenize a math expression into numbers, operators, and parentheses."""
    tokens = []
    pattern = re.compile(r"\d+(?:\.\d+)?|[+\-*/^()]")
    for match in pattern.finditer(expr):
        tokens.append(match.group())
    return tokens


def shunting_yard(tokens: List[str]) -> List[str]:
    """Convert infix tokens to postfix (Reverse Polish Notation)."""
    output: List[str] = []
    operators: List[str] = []

    for token in tokens:
        if re.match(r"^\d+(?:\.\d+)?$", token):
            output.append(token)
        elif token in PRECEDENCE:
            while operators and operators[-1] in PRECEDENCE:
                top = operators[-1]
                if (token not in RIGHT_ASSOCIATIVE and PRECEDENCE[token] <= PRECEDENCE[top]) or (
                    token in RIGHT_ASSOCIATIVE and PRECEDENCE[token] < PRECEDENCE[top]
                ):
                    output.append(operators.pop())
                else:
                    break
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            if not operators:
                raise ValueError("Mismatched parentheses in expression.")
            operators.pop()
        else:
            raise ValueError(f"Unknown token: {token}")

    while operators:
        top = operators.pop()
        if top in ("(", ")"):
            raise ValueError("Mismatched parentheses in expression.")
        output.append(top)

    return output


def evaluate_rpn(rpn_tokens: List[str]) -> float:
    """Evaluate Reverse Polish Notation tokens."""
    stack: List[float] = []
    for token in rpn_tokens:
        if token in PRECEDENCE:
            if len(stack) < 2:
                raise ValueError("Invalid expression format.")
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero in expression.")
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)
        else:
            stack.append(float(token))

    if len(stack) != 1:
        raise ValueError("Invalid expression evaluation.")
    return stack[0]


def evaluate_expression(expr: str) -> float:
    """Parse and evaluate infix mathematical expression."""
    tokens = tokenize_expression(expr)
    rpn = shunting_yard(tokens)
    return evaluate_rpn(rpn)
