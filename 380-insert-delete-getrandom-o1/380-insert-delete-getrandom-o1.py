import random
class RandomizedSet:
    

    def __init__(self):
        self.d = set()
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        else:
            self.d.add(val)
            self.len+=1
            return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            self.d.remove(val)
            self.len-=1
            return True
        
        else:
            return False

    def getRandom(self) -> int:
        return list(self.d)[random.randint(0,self.len-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()