import Analyzer as linter


def add_brackets(formula: str) -> str:
    if formula[0] != "(":
        return "(" + formula + ")"
    elif formula[0] == "(":
        if formula[-1] != ")":
            return "(" + formula + ")"
    return formula


def get_subformula(formula: str, k: int) -> tuple:
    cont = 0
    i = k
    while cont != 1:
        i += 1
        if formula[i] == ")":
            cont += 1
        elif formula[i] == "(":
            cont -= 1
    idx_f = i

    i = k
    cont = 0
    while cont != -1:
        i -= 1
        if formula[i] == ")":
            cont += 1
        elif formula[i] == "(":
            cont -= 1
    idx_i = i

    return idx_i, idx_f


def remove_implies(formula: str) -> str:
    formula = linter.format(add_brackets(formula))
    k = 0
    while ">" in formula:
        if formula[k] == ">":
            idx_i, idx_f = get_subformula(formula, k)
            formula = (
                formula[:idx_i]
                + "(-"
                + formula[idx_i + 1 : k]
                + "#"
                + formula[k + 1 : idx_f + 1]
                + formula[idx_f + 1 :]
            )
        k += 1

    return formula
