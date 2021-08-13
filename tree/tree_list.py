# this is simple implementation of tree using python list
class tree:
    def __init__(self,data,child=[]):
        self.data=data
        self.child=child

    # this function is used to print tree in a better format
    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.child:
            ret += child.__str__(level + 1)
        return ret

    def addNode(self,data):
        self.child.append(data)
    
drink=tree("Drink",[])   #here we create a node of drink which is also our root node     
hot=tree("hot",[])        
cold=tree("cold",[])        
tea=tree("tea",[])        
coffee=tree("coffee",[])        
fanta=tree("fanta",[])        
maja=tree("maja",[]) 
drink.addNode(hot)      #here we are creating a link between root and its child node 
drink.addNode(cold)
hot.addNode(tea)       
hot.addNode(coffee)
cold.addNode(fanta)       
cold.addNode(maja)
print(drink)       