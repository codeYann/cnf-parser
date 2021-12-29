from Analyzer import Analyzer

checkers = [
    "((p > q) > r)",
    "p#q",
    "(p&q > r # q)",
    "p > 2",
    "a > 1 > 3"
]

for check in checkers:
    formula = Analyzer(check)
    print(check, formula.isFormula())



