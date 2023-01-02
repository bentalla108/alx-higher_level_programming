class Humain:

    def __init__(self, nom , age):
        print("Creation Humain........")
        self.nom = nom
        self.__age = age
        
    def _getage(self):
        return self.__age

    def _setage(self , new_age):
        self.age = new_age
        return self.__age
        
    age=property(_getage , _setage)


h1 = Humain("Jason" , 23)

print(h1.age)

h1.age= 20
print(h1.age)
