class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def display(self):
        return f"{self.value}" 

new_node_1=Node(5)
new_node_2=Node(10)
new_node_1.next=new_node_1
print(new_node_2.display())    
