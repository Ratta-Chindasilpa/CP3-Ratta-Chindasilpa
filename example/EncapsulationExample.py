class Animal():
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    name = ""
    def setName(self, text): # Setter- ฟังก์ชันในการกำหนดค่า
        self.name = text
        print("Setting New Cat Name = ", self.name)
    def eat(self):
        print("Meoww !!", self.name)

cat1 = Cat()
cat1.setName(input("Enter your cat name: "))
cat1.eat()
