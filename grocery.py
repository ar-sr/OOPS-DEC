class grocery_item:
    def __init__(self,name,category,price,is_purchased):
        self.name=name
        self.category=category
        self.price=price
        self.is_purchased=False
        
        
    def purchase(self):
        if not self.is_purchased:
           print(f"The {self.name},{self.category},{self.price}is purchased successfully!")
           self.is_purchased=True 
        else:
            print("cant be purchased")
            
                      
            
    def return_item(self):
        if not self.return_item:
            print(f"the {self.name},{self.category},{self.price},{self.is_purchased} should be returned")
            self.purchase=False
        else:
            print("item cant be returned")
            
            
            
item1=grocery_item(
        name=input("enter name of the item:"),
        price=input("enter the price of item:"),
        category=input("enter the category:"),
        is_purchased=input("enter the date:"))
    
    
item1.purchase()
item1.return_item()