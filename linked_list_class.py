class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        if self.head == None:
            return '[]'

        pointer = self.head
        if pointer.next == None:
            return '[' + str(pointer.item) + ']'

        list = '['
        while pointer.next:
            list = list + str(pointer.item) + ", "
            pointer = pointer.next
            if not pointer.next:
                list = list + str(pointer.item) + ']'
        return list

    def insert(self, item, index=int):
        if index >= 0 and index <= self.size: #Verifies if the informed index is valid to insert
            new_node = Node(item)
            if self.head:
                if index == 0: #inserting in the begning of the list
                    new_node.next = self.head # if the index to insert is 0, the new_node begins to point to the first item of the list
                    self.head = new_node # the new node becomes the first item of the list
                elif index == self.size: #inserting in the ending of the list
                    pointer = self.head
                    while pointer.next: # finding the last node to insert in its "next", which is the end of the list
                        pointer = pointer.next
                    pointer.next = new_node
                elif index > 0 and index < self.size: #inserting between the begning and the ending of the list
                    counter = 0
                    pointer = self.head
                    while pointer.next:
                        if counter + 1 == index:
                            new_node.next = pointer.next
                            pointer.next = new_node
                            break
                        counter = counter + 1
                        pointer = pointer.next
            else:
                self.head = new_node
            self.size = self.size + 1
        else:
            return False

    def remove(self, index):
        if index >= 0 and index < self.size: #Verifies if the informed index is valid to be removed
            if index == 0:
                self.head = self.head.next
                self.size = self.size - 1
                return True
            elif index == self.size-1:
                counter = 0
                pointer = self.head
                while pointer.next:
                    if counter + 1 == index:
                        pointer.next = None
                        self.size = self.size - 1
                        break
                    counter = counter + 1
                    pointer = pointer.next
                return True
            else:
                counter = 0
                pointer = self.head
                while pointer.next:
                    if counter + 1 == index:
                        indice_anterior = pointer
                    elif counter == index:
                        indice_anterior.next = pointer.next
                        self.size = self.size - 1
                        break
                    pointer = pointer.next
                    counter = counter + 1

                return True
        else:
            return False

    def get_item(self, index):
        if index >= 0 and index < self.size and self.size > 0: #verifies if the index exists
            counter = 0
            pointer = self.head
            while pointer.next: #goes through the nodes and if the informed index is equal to the counter it returns the value of that node
                if counter == index:
                    return pointer.item
                counter = counter + 1
                pointer = pointer.next
            if counter == index: #there is this check outside of the loop cause when the loop stops the last item was not checked yet
                return pointer.item
        else:
            return False

    def get_index(self, item):
        if self.size == 0:
            return False
        else:
            counter = 0
            pointer = self.head
            while pointer.next: # goes through the nodes and if the informed item is equal to the node item, it returns the counter, which is the index in the list
                if item == pointer.item:
                    return counter
                counter = counter + 1
                pointer = pointer.next
            if item == pointer.item: # #there is this check outside of the loop cause when the loop stops the last item was not checked yet
                return counter
            else:
                return False

    def empty(self):
        self.head = None
        self.size = 0
    
    def is_equal(self, list2):
        if self.list_size() != list2.list_size(): # checking if the sizes of the lists are the same
            return False
        elif self.list_size() == 0: # if the size of one list is equal to 0, both lists are empt and they are equal
            return True
        else: # going through both lists and if one list's item is different from the other's list item at the same position it returns False. If not, it returns True.
            pointer_of_list1 = self.head 
            pointer_of_list2 = list2.head
            while pointer_of_list1.next:
                if pointer_of_list1.item != pointer_of_list2.item:
                    return False
                pointer_of_list1 = pointer_of_list1.next
                pointer_of_list2 = pointer_of_list2.next
            if pointer_of_list1.item != pointer_of_list2.item: # this checkig is happening outside the loop cause when the loop breaks the last item is left unchecked
                return False
            else:
                return True

    def reverse_list(self):
        counter = 1 # the value between the counter and the list's size is the amount of iteration that needs to be done to get the item from the list that should be inserted in the reversed list
        where_to_begin = 1 #keeps track of where the counter should start after each iteration
        reversed_list = List()
        for i in range(0, self.list_size()):
            pointer = self.head
            while counter < self.list_size():
                pointer = pointer.next
                counter = counter + 1
            reversed_list.insert(pointer.item, reversed_list.list_size()) # list items are inserted in another list in reverse order
            where_to_begin = where_to_begin + 1
            counter = where_to_begin
        return reversed_list

    def list_size(self): # returns the variable that keeps track of the amount of items in the list
        return self.size

