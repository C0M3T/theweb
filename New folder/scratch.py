


class Taco():
    def __init__ (self , meat , toppings ):
        self.meat= meat
        self.toppings= toppings


    def eatingTaco(self):
        print("collecting items from the freezer")
        print("your" +" "+ self.meat + " "+ self.toppings + " " + "Taco is ready.")

meat=  input("what kind of meat do you prefer?")
toppings =input("What kind of topping do you prefer?")

myTaco = Taco(meat,toppings)
print(myTaco.meat)
print(myTaco.toppings)
myTaco.eatingTaco()





