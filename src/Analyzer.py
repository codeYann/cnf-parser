import re as RegExp

class Analyzer:
    def __init__(self, formula: str):
        self.formula = formula
    
    def isFormula(self) -> bool:
        if not (RegExp.search(r"[\(\)]", self.formula)):
            return False
        else:
            match = RegExp.search(r"[^a-z\(\)#&>-]", self.formula)
            if match:
                return False
            return True

