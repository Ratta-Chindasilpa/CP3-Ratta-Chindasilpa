class Custumer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to ",self.name,self.lastName,"'s cart")

customer1 = Custumer()
customer1.name = "Ratta"
customer1.lastName = "Chindasilpa"
customer1.age = 23
customer1.addCart()

customer2 = Custumer()
customer2.name = "Leonardo"
customer2.lastName = "DiCaprio"
customer2.age = 43
customer2.addCart()

customer3 = Custumer()
customer3.name = "Chris"
customer3.lastName = "Hemsworth"
customer3.age = 35
customer3.addCart()

customer4 = Custumer()
customer4.name = "Vin"
customer4.lastName = "Diesel"
customer4.age = 51
customer4.addCart()