# Consider telephone book database of N clients. Make use of a hash table implementation
# to quickly look up client‘s telephone number. Make use of two collision handling
# techniques and compare them using number of comparisons required to find a set of
# telephone numbers
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Hashing:
    def __init__(self):
        self.HashTable = [None] * 10

    def hash_function(self, value):
        return value % 10

    def create_node(self, x):
        return Node(x)

    def display(self):
        for i in range(10):
            temp = self.HashTable[i]
            print(f"a[{i}] : ", end="")
            while temp is not None:
                print(f"->{temp.value}", end="")
                temp = temp.next
            print()

    def search_element(self, value):
        flag = False
        hash_val = self.hash_function(value)
        entry = self.HashTable[hash_val]
        print("\nElement found at : ", end="")
        while entry is not None:
            if entry.value == value:
                print(f"{hash_val} : {entry.value}")
                flag = True
            entry = entry.next
        if not flag:
            return -1

    def delete_element(self, value):
        hash_val = self.hash_function(value)
        entry = self.HashTable[hash_val]

        if entry is None:
            print("No Element found")
            return

        if entry.value == value:
            self.HashTable[hash_val] = entry.next
            return

        while entry.next.value != value:
            entry = entry.next

        entry.next = entry.next.next

    def insert_element(self, value):
        hash_val = self.hash_function(value)
        temp = self.HashTable[hash_val]
        head = self.create_node(value)

        if temp is None:
            self.HashTable[hash_val] = head
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = head



h = Hashing()

while True:
    print("\nTelephone : \n1.Insert \n2.Display \n3.Search \n4.Delete \n5.Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        data = int(input("Enter phone no. to be inserted: "))
        h.insert_element(data)
    elif ch == 2:
        h.display()
    elif ch == 3:
        search = int(input("Enter the no to be searched: "))
        if h.search_element(search) == -1:
            print("No element found at key")
    elif ch == 4:
        delete_val = int(input("Enter the phno. to be deleted: "))
        h.delete_element(delete_val)
        print("Phno. Deleted")
    elif ch == 5:
        break
    else:
        print("Invalid choice. Please enter a valid option.")


