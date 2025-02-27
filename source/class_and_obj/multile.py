class grandmother:
    def cute(self):
        return "she is cute"
    def cooking(self):
        return "she is best chef"
    def anger_mode(self):
        return "never scolds"

class mother(grandmother):
    def cooking(self):
        return super().cooking()
    def anger_mode(self):
        super().anger_mode()
    def loves_shopping(self):
        return "loves to shop"
    def study(self):
        return "good in studies"

class daughter(mother):
    def cooking(self):
        return super().cooking()
    def study(self):
        return super().study()
    def cute(self):
        return super().cute()

obj=daughter()
print(obj.cute())
print(obj.cooking())
print(obj.study())


print(obj.anger_mode())