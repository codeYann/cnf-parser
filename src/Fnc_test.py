import Fnc as fnc

formulas = ["(((-p#q)>p)>p)", "((p#q)>-(q#r))", "(-(p&q))", "(p> ((p>r)#(a>b)))"]

print("Formula original | Formula normal conjuntiva\n")

for i in formulas:
    print(f"{i} <-> {fnc.remove_double_neg(fnc.push_negations(fnc.remove_implies(i)))}")
