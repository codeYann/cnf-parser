from Analyzer import Analyzer

formula = "(p>(p#q))"

check = Analyzer(formula)
print(check.isFormula())



