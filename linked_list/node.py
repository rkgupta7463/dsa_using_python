class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.lenght=0

    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+=' -> '
            temp_node=temp_node.next

        return result

    def preappend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.lenght+=1

    def append(self,value):
        new_node=Node(value=value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.lenght+=1

    def insert(self,idx,value):
        new_node=Node(value)
        temp_node=self.head
        if idx<0 or idx > self.lenght:
            return False
        if self.lenght == 0:
            self.head=new_node
            self.tail=new_node
        elif idx==0:
            new_node.next=self.head
            self.head=new_node
        else:    
            for _ in range(idx-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node

        self.lenght+=1

        return True




new_linked_list=LinkedList()
new_linked_list.append(10)
new_linked_list.append(15)
new_linked_list.append(16)
print(new_linked_list)    
new_linked_list.preappend(22)
print(new_linked_list)    
new_linked_list.insert(3,25)
print(new_linked_list)    
