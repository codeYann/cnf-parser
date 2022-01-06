import Analyzer as linter


def add_brackets(formula: str) -> str:
    if formula[0] != "(":
        return "(" + formula + ")"
    elif formula[0] == "(":
        if formula[-1] != ")":
            return "(" + formula + ")"
    return formula


def get_brackets_idx(formula: str, k: int) -> tuple:
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


def external_idx_operator(formula: str) -> int:
    count = 0
    i = 0
    for k in range(len(formula)):
        if formula[k] == "(":
            count += 1
        elif formula[k] == ")":
            count -= 1
        elif count == 1 and (
            formula[k] == ">" or formula[k] == "#" or formula[k] == "&"
        ):
            return i
        i += 1
    return None


# redefinir implicações em termos de disjunção e negação [ok]
def remove_implies(formula: str) -> str:
    formula = linter.format(add_brackets(formula))
    k = 0
    while ">" in formula:
        if formula[k] == ">":
            idx_i, idx_f = get_brackets_idx(formula, k)
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


# Empurrar as negações para o interior por meio de De Morgan [ok]
def push_negations(formula: str) -> str:
    k = 0
    while "-(" in formula:
        if formula[k] == "#" or formula[k] == "&":
            idx_i, idx_f = get_brackets_idx(formula, k)

            if formula[idx_i - 1] == "-":
                formula = switch_operatores(formula, idx_i, idx_f)
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


# Eliminar as duplas negações [ok]
def remove_double_neg(formula: str) -> str:
    while "--" in formula:
        formula = formula.replace("--", "")
    return formula


# Distributividade de disjunção sobre conjunção []
def distributive(formula: str) -> str:
    while "#(" in formula or ")#" in formula:
        idx = external_idx_operator(formula)
        flag = False
        if formula[idx] == "#":
            slice = formula[idx + 1 : -1]
            slice_idx = external_idx_operator(slice)
            if slice_idx:
                if slice[slice_idx] == "&":
                    f1 = f3 = formula[1:idx]
                    f2 = slice[1:slice_idx]
                    f4 = slice[slice_idx + 1 : -1]
                    flag = True

            if not flag:
                slice = formula[1:idx]
                slice_idx = external_idx_operator(slice)
                if slice_idx:
                    if slice[slice_idx] == "&":
                        f1 = slice[1:slice_idx]
                        f2 = f4 = formula[idx + 1 : -1]
                        f3 = slice[slice_idx + 1 : -1]
                        flag = True
        if flag:
            formula = "((" + f1 + "#" + f2 + ")&(" + f3 + "#" + f4 + "))"
            idx = external_idx_operator(formula)

    return formula
