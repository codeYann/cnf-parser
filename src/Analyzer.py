import re as RegExp

class Analyzer:
    def __init__(self, formula: str):
        self.formula = formula
        self.formula = self.Formatting()
    
    def Formatting(self) -> str:
        self.formula = self.formula.replace(" ", "")
        if len(self.formula) % 2 == 1:
            self.formula = ''.join((self.formula, ')'))
        return self.formula

    def isFormula(self):
        print(self.CheckFormula(self.formula))
        if len(self.formula % 2 == 1):
            self.formula = self.formula[0:len(self.formula)] 

    def Cases(self, string: str, state: list): 
        for i in range(len(string)):
            if RegExp.search(r"[a-z]", string[i]): # case i -> atom
                if RegExp.search(r"[\)#&>-", string[i+1]):
                    print(1)
                    state[0] = True
                else:
                    state[0] = False
            elif string[i] == '(': 
                if RegExp.search(r"[a-z]", string[i+1]) or RegExp.search(r"[\(]", string[i+1]):
                    state[0] = True
                else:
                    state[0] = False
            elif string[i] == ')':
                print(3)
                if RegExp.search(r"[#&>-]", string[i+1]) or RegExp.search(r"[\)]", string[i+1]):
                    state[0] = True
                else:
                    state[0] = False
            else:
                print(4)
                if RegExp.search(r"[a-z]", string[i+1]) or RegExp.search(r"[\(]", string[i+1]):
                    state[0] = True
                else:
                    state[0] = False
         

    def CheckAtoms(self, left: str, right: str):
        left_state = right_state = [False]
        
        for _ in range(len(left)):
            self.Cases(left, left_state)

        for _ in range(len(right)):
            self.Cases(right, right_state)

        return left_state[0] and right_state[0]

    def CheckFormula(self, formula: str):
        if len(formula) == 2:
            return formula
        
        mid = int(len(formula)/2)
        left = self.CheckFormula(formula[:mid])
        right = self.CheckFormula(formula[mid:])

        return self.CheckAtoms(left, right)

