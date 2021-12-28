from Analyzer import Analyzer

formula = "((p>(p#q))&r)"

check = Analyzer(formula)
print(check.isFormula())



