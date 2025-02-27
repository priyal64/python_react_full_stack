class papa:
    
    def nose(self):
        return "having small nose"
    def eyes(self):
        return "having brown eyes"
    def math(self):
        return "good in maths"
class mumma:
    # def nose(self):
    #     return "having biggggg nose"
    # def eyes(self):
    #     return "having black eyes"
  
    def science(self):
        return "good in science"
    def cooking(self):
        return "cooks delicious food"
    def artist(self):
        return"is a good artist" 
    def dance(self):
        return "don't know how to dance"
    def sports(self):
        return "weak in sports"
class child(papa,mumma):
    # pass
    # or 
    
        
    def sports(self):
        return " is good in sports"

baby=child()
print(baby.dance())
print(baby.math())
print(baby.science())
print(baby.nose())
print(baby.eyes())
print("-----------------")
b=mumma()
b=baby
print(b.sports())