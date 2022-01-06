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


def switch_operatores(formula: str, start: int, end: int) -> str:
    formula = list(formula)
    for i in range(start, end + 1):
        if formula[i] == "#":
            formula[i] = "&"
        elif formula[i] == "&":
            formula[i] = "#"
    return "".join(formula)


def push_negations(formula: str) -> str:
    k = 0
    while "-(" in formula:
        if formula[k] == "#" or formula[k] == "&":
            idx_i, idx_f = get_subformula(formula, k)
            formula = switch_operatores(formula, idx_i, idx_f)

            if formula[idx_i - 1] == "-":
                print(formula)
                formula = (
                    formula[0 : idx_i - 1]
                    + formula[idx_i]
                    + "-"
                    + formula[idx_i + 1 : k + 1]
                    + "-"
                    + formula[k + 1 :]
                )
                k = 0
        k += 1

    return formula


def remove_double_neg(formula: str) -> str:
    while "--" in formula:
        formula = formula.replace("--", "")
    return formula


print("(((p>q)>p)>p)")
print(remove_double_neg(push_negations(remove_implies("(((p>q)>p)>p)"))))
