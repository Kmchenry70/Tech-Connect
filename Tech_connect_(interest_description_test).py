class Tech(): 
    def __init__(self, item): 
        self.item = item
        self.interest = []
        self.description = []

    @property
    def item(self): 
        return self._item 
    
    @item.setter
    def item(self, value): 
        self._item = value
        return value

    @property
    def interest(self): 
        return self._interest
    
    @interest.setter
    def interest(self, value): 
        self._interest = value
        return value
    
    @property
    def description(self): 
        return self._description
    
    @description.setter
    def description(self, value): 
        self._description = value
        return value
    
    # This function allows for the interest and description to be coded together and put into an item_catagory.
    def add_item(self, interest, description): 
        self.interest.append(interest)
        self.description.append(description)
    
    def __str__(self): 
        n = len(self._interest)
        u = "Interest catagory: \n"
        u+= f"{self._item}:\n\n"
        for i in range(0, n): 
                u+= f"{self._interest[i]}: {self._description[i]}\n"
        return u
    
item1 = Tech("Sports")

item1.add_item("football", "Game where students throw ball and catch while running to the other side of the field")

item1.add_item("basketball", "students dribble ball to other court while passing the ball and shooting the ball into the goal")
item1.add_item("baseball", "students hit incoming balls that are pitched to them at high speeds with a bat in hopes of running around the field to earn points")


print(item1)