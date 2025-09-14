#666孟德尔
import random
from collections import Counter
class Test:
    def __init__(self):
        self.dominant_gene = 'A'
        self.recessive_gene = 'a'
    def parents_baby(self, pod1, pod2, babies=1000):
        result = []
        for _ in range(babies):
            A_or_a1 = random.choice(pod1)
            A_or_a2 = random.choice(pod2)
            baby = ''.join(sorted([A_or_a1, A_or_a2]))
            result.append(baby)
        return result

test=Test()
baby_end=test.parents_baby(['A','a'],['A','a'])

counter = Counter(baby_end)
print("基因型结果:", counter)