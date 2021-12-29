import re as RegExp

class Analyzer:
    def __init__(self, formula: str):
        self.formula = formula
    
    def isFormula(self) -> bool:
        match = RegExp.search(r"[^a-z\(\) #&>-]", self.formula)
        if match:
            return False
        return True

