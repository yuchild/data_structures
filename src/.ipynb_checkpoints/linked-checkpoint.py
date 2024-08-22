#!usr/bin/env python3

class node: # subclass of the linked list
    def __init__(self,data=None):
        self.data=data # store past data point
        self.next=None # store pointer to next node

class linked_list: # wrapper to access the node class
    def __init__(self):
        self.head = node() # does not contain data or index, user will not be able to access this, basic placeholder

    def append(self,data): # add to the last element
        new_node = node(data)
        current = self.head
        while current.next!=None:
            current = current.next
        current.next = new_node

    def length(self): # calculates the lengh of list
        current = self.head
        total = 0
        while current.next!=None:
            total+=1
            current = current.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        return elems

    def get(self,index):
        # check index user wants is within bounds
        if index>=self.length():
            print("Error: 'Get' Index out of range!")
            return None

if __name__ == "__main__":
    ...