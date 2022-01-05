import string

# Alphabet
atoms = list(string.ascii_lowercase)
operatores = ["#", ">", "&", "-"]
delimiters = ["(", ")"]


# Removing blank spaces
def format(formula) -> str:
    return formula.replace(" ", "")


# Looking for minors issues
def lexer_analyzer(formula) -> tuple:
    open_p = close_p = 0

    if len(formula) == 1 and formula[0] in operatores:
        return False
    elif len(formula) == 1 and formula[0] in delimiters:
        return False

    tokens = []
    paranteses_state = True

    for i in formula:
        if i == "(":
            open_p += 1
        if i == ")":
            close_p += 1
        tokens.append(i)

    if open_p != close_p:
        paranteses_state = False
        return False, paranteses_state

    flag = False  # flag is a var to check if there's an atoms in formula
    for token in tokens:
        if token in atoms:
            flag = True

        if not token in atoms and not token in operatores and not token in delimiters:
            return False, paranteses_state
    return flag, paranteses_state


# Check majors issues
def verify(curr, next, prev="-") -> bool:
    if curr == "-":
        if prev in atoms:
            return False

        if not (next in atoms or next == "-" or next == "("):
            return False

    elif curr == "(":
        if not (next in atoms or next == "(" or next == "-"):
            return False
    elif curr in atoms:
        if not (next in operatores or next == ")"):
            return False
    elif curr in operatores:
        if not (next in atoms or next == "(" or next == "-"):
            return False
    else:
        if not (next == ")" or next in operatores):
            return False
    return True


def semantic_analyzer(formula) -> bool:
    formula = format(formula)
    response, paranteses_state = lexer_analyzer(formula)
    state = True

    if response:
        if formula[-1] in operatores:  # if there's an operator in last position
            return False
        if paranteses_state == False:
            if formula[0] == "(":
                if formula[-1] != ")":
                    return False
            else:
                if formula[-1] == ")":
                    return False

        for i in range(0, len(formula) - 1):
            if i == 0:
                state = verify(formula[i], formula[i + 1])
            else:
                state = verify(formula[i], formula[i + 1], formula[i - 1])

            if state == False:
                break
        return state
    else:
        return False


def is_formula(formula) -> bool:
    return semantic_analyzer(formula)
