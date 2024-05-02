class Tech(): 
    def __init__(self, item): 
        self.item = item
        self.description = []

    @property
    def item(self): 
        return self._item 
    
    @item.setter
    def item(self, value): 
        self._item = value
        return value

    @property
    def description(self): 
        return self._description
    
    @description.setter
    def description(self, value): 
        self._description = value
    
    # This function allows for the interest and description to be coded together and put into an item_catagory.
    def add_item(self, item, desc): 
        self._description[item] = desc
        
    
    def __str__(self): 
        n = len(self._interest)
        u = "List of interests: \n"
        u+= f"{self._item}:\n\n"
        for i in range(0, n): 
                u+= f"{self._interest[i]}: {self._description[i]}\n"
        return u
    

