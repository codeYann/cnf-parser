import Analyzer as checker
import functools

"""
    - Atividade de Lógica para Computação.
    - Autores: Paulo Henrique Diniz de Lima Alencar, Yan Rodrigues e Alysson Lucas Pinheiro.
    - Professor: Alexandre Arruda.
"""


def compoose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


# Obtem os indices dos parenteses das subformulas.
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


# Step 1 - redefinir implicações em termos de disjunção e negação [ok]
def remove_implies(formula: str) -> str:
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


# Step 2 - Realiza a troca dos conectivos # por & e vice-versa
def switch_operatores(formula: str, start: int, end: int) -> str:
    formula = list(formula)
    for i in range(start, end + 1):
        if formula[i] == "#":
            formula[i] = "&"
        elif formula[i] == "&":
            formula[i] = "#"
    return "".join(formula)


# Step 3 - Empurrar as negações para o interior por meio de De Morgan [ok]
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


# Step 4 - Eliminar as duplas negações [ok]
def remove_double_neg(formula: str) -> str:
    return formula.replace("--", "")


# Encontra os indices dos conectivos # e &
def search_connectives_idx(formula: str, order: str) -> tuple:
    if order == "left":
        flag = end = step = -1
    else:
        flag = 1
        end = len(formula)
        step = 1

    for i in range(len(formula)):
        if formula[i] == "#":
            cont = 0
            for j in range(i, end, step):
                if formula[j] == "(":
                    cont += 1
                elif formula[j] == ")":
                    cont -= 1
                elif formula[j] == "&" and cont == flag:
                    return i, j

    return None, None


# Step 5 - Distributividade de disjunção '#' sobre conjunção '&' [ok]
def distributive(formula: str) -> str:

    flag = True

    while flag and ("#(" in formula or ")#" in formula):
        while "#(" in formula:
            dis, conj = search_connectives_idx(formula, "right")
            if not (dis and conj):
                flag = False
                break

            i_dis, f_dis = get_brackets_idx(formula, dis)
            i_conj, f_conj = get_brackets_idx(formula, conj)

            slice1 = formula[:i_dis]
            slice2 = formula[i_dis + 1 : dis]
            slice3 = formula[i_conj + 1 : conj]
            slice4 = slice2
            slice5 = formula[conj + 1 : f_conj]
            slice6 = formula[f_dis + 1 :]

            formula = (
                slice1
                + "(("
                + slice2
                + "#"
                + slice3
                + ")&("
                + slice4
                + "#"
                + slice5
                + "))"
                + slice6
            )

        while ")#" in formula:
            dis, conj = search_connectives_idx(formula, "left")
            if not (dis and conj):
                flag = False
                break

            i_dis, f_dis = get_brackets_idx(formula, dis)
            i_conj, f_conj = get_brackets_idx(formula, conj)

            slice1 = formula[:i_dis]
            slice2 = formula[i_conj + 1 : conj]
            slice3 = formula[dis + 1 : f_dis]
            slice4 = formula[conj + 1 : f_conj]
            slice5 = slice3
            slice6 = formula[f_dis + 1 :]

            formula = (
                slice1
                + "(("
                + slice2
                + "#"
                + slice3
                + ")&("
                + slice4
                + "#"
                + slice5
                + "))"
                + slice6
            )
    return formula


def to_cnf(formula: str) -> str:
    # Step 0: remove blank spaces
    # Step 1: remove_implies
    # Step 2: push_negations
    # Step 3: remove_double_neg
    # Step 4: distributive

    # functions exec orders goes right to left
    updated_formula = compoose(
        distributive, remove_double_neg, push_negations, remove_implies, checker.format
    )
    return updated_formula(formula)
