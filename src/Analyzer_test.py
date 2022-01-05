from Analyzer import Analyzer

a = Analyzer()

formulas = [
   "--p",
    "(p>(q>(r>s)))",
    "-(((p>-q)&q)#-s)",
    "((p.r)^(p>q))",
    "(p-q)",
    "p%q",
    "t&r",
    "(p>q>r",
    "p>q>r)",
    "(p&>q)",
    "(pp#q)",
    "(a)",
    "(-p)",
    "((p#q)>p))",
    "(>(p#q)>r)",
    "()(p>q)",
    ")p#q(",
    "(p>q(",
    "--(",
    "----p#",
    "----p---f",
    "(p#q)-",
    "((((()))))",
    "-p",
    "(p>-)",
    "p>q<q",
    "p>q>r>c>a>i>j",
    "((p>q)>((r#a)>(t>x>(b#a))))",
    "-(-p#r) > -(p>h)",
    "(p>q>r>a#p))",
    "(p > q) > (((p>q) > p) & ((p#q) > q))",
    "((p>p)>p)>p",
    "--p > (p>e)",
    "--p > -p",
    "---p > -p",
    "((--p#q)>q)",
    "-(-p) > (-p) # q",
]

print("[T/F] | Formula\n--------|---------")

for i in formulas:
    print(f'{a.isFormula(i)}\t| {i}')
