

class Poly:
    def __init__(self, coef):
        self.coefficient=coef
    
    def degree(self):
        return len(self.coefficient) - 1
    
    def __str__(self):
        coefs=self.coefficient
        term=[]
        if coefs[0]:
            term.append(str(coefs[0]))
        if self.degree()>0 and coefs[1]:
            term.append(f"{coefs[1]}x")
        
        term += [f"{'' if c==1 else c}x^{d}"for d,c in enumerate(coefs[2:], start=2) if c]

        return "+".join(reversed(term)) or "0"