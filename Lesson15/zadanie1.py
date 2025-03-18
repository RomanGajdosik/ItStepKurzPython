class integers():
    def __init__(self, mnozina):
        self.mnozina = mnozina
        
    def sum(self):
        return sum(self.mnozina)
    def max(self):
        return max(self.mnozina)
    def min(self):
        return min(self.mnozina)
    def avrg(self):
        return sum(self.mnozina)/len(self.mnozina)
    
# mnozina = integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(mnozina.sum())
# print(mnozina.max())
# print(mnozina.min())
# print(mnozina.avrg())