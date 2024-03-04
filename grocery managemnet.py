class product:
    def __init__(self,name,category,price):
        self.name=name
        self.category=category
        self.price=price
        
        
    def display_info(self):
        print(f"name={self.name} category={self.category} price={self.price}")


    
    
class grocery_store():
    def __init__(self):
        self.grocery =[]
    
        
    
    def addproduct(self):
        grocery_store.append(product)
        print(f"the{self.name} {self.category} {self.price} is added successfully")
    
    
    
    def deleteproduct(self):
        grocery_store.remove(product)
        print(f"the{self.name} {self.category} {self.price} is removed successfully")
        
        
        
     
           
product1= product(name= input("enter the name:"),
                        price = float(input("enter the price:")),
                        category = input("enter the category:"))


product1.display_info()
product1.addproduct()
product1.deleteproduct()
    