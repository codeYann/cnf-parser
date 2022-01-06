import Analyzer as linter


def add_brackets(formula: str) -> str:
    if formula[0] != "(":
        return "(" + formula + ")"
    elif formula[0] == "(":
        if formula[-1] != ")":
            return "(" + formula + ")"
    return formula


def remove_implications(formula: str):
    formula = add_brackets(linter.format(formula))
    print(formula)
    formula = list(formula)

    fnc = formula
    i = 0

    while ">" in formula:
        if formula[i] == ">":
            if formula[i - 1] in linter.atoms:
                fnc[i] = "#"
                fnc.insert(i - 1, "-")
            else:
                pass
        i += 1
    return fnc


formula = "p>q"
formula = remove_implications(formula)
print(formula)
