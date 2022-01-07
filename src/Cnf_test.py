import Cnf as cnf

# Arquivo para testes:

formulas = [
    "((p#q)>-(q#r))",
    "(-(p&q))",
    "(((p>q)>p)>p)",
    "((p&s)#(q&r))",
    "(p#(q&r))",
    "((q&r)#p)",
]

c = 1
for i in formulas:
    print(f"{c}. Fomula.......:")
    print(f"Old formula......: {i}")
    print(f"New formula (cnf): {cnf.to_cnf(i)}\n\n")
    c += 1
