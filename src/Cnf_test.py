import Cnf as cnf_parser

# formulas para testes:
formulas = [
    "((p#q)>-(q#r))",
    "(-(p&q))",
    "(((p>q)>p)>p)",
    "((p&s)#(q&r))",
    "(p#(q&r))",
    "((q&r)#p)",
    "(- (p & q))",
]

count = 1
for forms in formulas:
    print(f"{count}. Fomula.......:")
    print(f"Old formula......: {forms}")
    print(f"New formula (cnf): {cnf_parser.to_cnf(forms)}\n\n")
    count += 1
