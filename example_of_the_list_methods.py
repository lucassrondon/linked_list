from linked_list_class import *

list1 = List()

for i in range(10, -1, -1):
    list1.insert(i, 0)
print("LIST AFTER THE INSERTION OF ITEMS:", list1)
print("LIST SIZE METHOD:", list1.list_size())
list1.insert("IN THE MIDDLE", 6)
print("INSERTION IS POSSIBLE IN ANY VALID INDEX:", list1)
print("GETTING AN INDEX THROUGH A VALUE:", list1.get_index("IN THE MIDDLE"))
print("GETTING A VALUE THROUGH ITS INDEX:", list1.get_item(6))
list1.remove(6)
print("LIST AFTER REMOVING THE ITEM IN INDEX 6:", list1)
list1 = list1.reverse_list()
print("LIST AFTER THE REVERSE METHOD:", list1)
