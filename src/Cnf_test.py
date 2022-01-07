import Cnf as cnf

# Arquivo para testes:

formulas = [
    '((a&b)#(c&d))',
    '(a>(b>c))',
    '((a>b)>c)',
    '((a>b)>(c>d))',
    '-(a>-(b>c))',
    '((a#b)>c)',

    '(((p>q)>p)>p)', 
    '((p#q)>-(q#r))', 
    '(-(p&q))',
    '((p&s)#(q&r))',
    '(p#(q&r))',
    '((q&r)#p)',
]

c = 1
for i in formulas:
    print(f'{c}. Fomula.......:')
    print(f'Old formula......: {i}')
    print(f'New formula (cnf): {cnf.to_cnf(i)}\n\n')
    c += 1
