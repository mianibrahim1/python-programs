# Implemented a linked list in python.
class Node:
    value =  None
    next = None
    def __init__(self, val):
        self.value = val
class Linked_List:
    def __init__(self, head_node):
        self.head = head_node
    def push_back(self, new_node):
        self.temp = self.head
        if self.head == None:
            self.head = new_node
            return
        while self.temp.next != None:
            self.temp = self.temp.next
        self.temp.next = new_node
    def remove(self):
        self.temp = self.head
        if self.temp == None:
            print "Empty Linked List"
            return
        elif self.temp.next == None:
            self.head = None
            return
        while self.temp.next.next != None:
            self.temp = self.temp.next
        self.temp.next = None
    def print_linkedlist(self):
        self.temp = self.head
        print "Starting Linked List"
        while self.temp != None:
            print self.temp.value
            self.temp = self.temp.next
        print "Ending Linked List"

first_node = Node(1)
Second_node = Node(2)
Third_node = Node(3)
fourth_node = Node(4)
my_linkedlist = Linked_List(first_node)
my_linkedlist.push_back(Second_node)
my_linkedlist.push_back(Third_node)
my_linkedlist.push_back(fourth_node)
my_linkedlist.print_linkedlist()
my_linkedlist.remove()
my_linkedlist.print_linkedlist()
my_linkedlist.remove()
my_linkedlist.print_linkedlist()
my_linkedlist.remove()
my_linkedlist.print_linkedlist()
my_linkedlist.remove()
my_linkedlist.print_linkedlist()
my_linkedlist.remove()
my_linkedlist.print_linkedlist()
my_linkedlist.remove()
my_linkedlist.print_linkedlist()
my_linkedlist = Linked_List(first_node)
my_linkedlist.push_back(Second_node)
my_linkedlist.push_back(Third_node)
my_linkedlist.push_back(fourth_node)
my_linkedlist.print_linkedlist()
