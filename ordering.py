import csv
class Ordering:
    def __init__(self, ccode, cus_name, phone):
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone
class TreeNode:
    def __init__(self, ordering):
        self.left = None
        self.right = None
        self.ordering = ordering
class BinaryTree:
    def __init__(self):
        self.root = None

    # 2.1 Load data from file
    def load_data_from_file(self):
        column_widths = [6, 16, 8]
        column_names = ["ccode |", "| cus_name", "| phone"]
        for i, name in enumerate(column_names):
            print(name.ljust(column_widths[i]), end="\t")
        print()
        print("-" * (sum(column_widths) + 5 * (len(column_names) - 1)))
        with open("ordering.txt", "r") as file:
            for line in file:
                ccode, cus_name, phone= line.strip().split('\t')
                print(ccode.ljust(column_widths[0])+'|', end="\t")
                print('|',cus_name.ljust(column_widths[1]), end="\t")
                print('|',phone.ljust(column_widths[2]))
    # 2.2 Input & insert data
    def Input_add_to_the_end(self):
        ccode = str(input("Enter ccode: "))
        cus_name = str(input("Enter ordering name: "))
        phone = int(input("Enter phone: "))
        ordering = Ordering(ccode, cus_name,phone)
        self.insert(ordering)
        with open("ordering.txt", "a") as file:
            file.write(f"{ordering.ccode}\t{ordering.cus_name}\t{ordering.phone}\n")
        print("ordering added successfully.")
        self.insert(ordering)

    def insert(self, ordering):
        if self.root is None:
            self.root = TreeNode(ordering)
        else:
            self._insert_helper(ordering, self.root)

    def _insert_helper(self, ordering, current_node):
        if ordering.ccode < current_node.ordering.ccode:
            if current_node.left is None:
                current_node.left = TreeNode(ordering)
            else:
                self._insert_helper(ordering, current_node.left)
        elif ordering.ccode > current_node.ordering.ccode:
            if current_node.right is None:
                current_node.right = TreeNode(ordering)
            else:
                self._insert_helper(ordering, current_node.right)
                
    # 2.5 sreach by ccode
    def search_ordering_by_ccode(self, ccode):
        return self._search_helper(ccode, self.root)

    def _search_helper(self, ccode, node):
        if node is None:
            return None
        elif node.ordering.ccode == ccode:
            return node.ordering
        elif node.ordering.ccode < ccode:
            return self._search_helper(ccode, node.right)
        else:
            return self._search_helper(ccode, node.left)

    # 2.6 Delete by ccode by copying
    def delete_ordering(self): 
        with open("ordering.txt", "r") as file:
            lines = file.readlines()
            
        found = False
        with open("ordering.txt", "w") as file:
            for line in lines:
                ordering_data = line.strip().split('\t')
                if ordering_data[0] != ccode:
                    file.write(line)
                else:
                    found = True

        if found:
            print("ordering deleted successfully.")
        else:
            print("ordering not found.")
    def delete_ordering_by_ccode(self, ccode):
        self.root = self._delete_helper(ccode, self.root)

    def _delete_helper(self, ccode, node):
        if node is None:
            return node
        if ccode < node.ordering.ccode:
            node.left = self._delete_helper(ccode, node.left)
        elif ccode > node.ordering.ccode:
            node.right = self._delete_helper(ccode, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._find_min_node(node.right)
            node.ordering = temp.ordering
            node.right

# Create a binary tree object
ordering = BinaryTree()

while True:
    print("--------------ordering--------------")
    print("1. Load data from file")
    print("2. Input & add to the end")
    print("3. Display data")
    print("4. Save ordering list to file")
    print("5. Search by ccode")
    print("6. Delete by ccode")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        ordering.load_data_from_file()
        #ordering.load_data_from_file()
    elif choice == "2":
        ordering.Input_add_to_the_end()
    elif choice == "3":
        ordering.load_data_from_file()
    elif choice == "4":
        ordering.load_data_from_file()
    elif choice == "5":
        ccode = input("Enter ccode: ")
        ordering = ordering.search_ordering_by_ccode(ccode)
        if ordering is None:
            print("ordering not found!")
        else:
            print(ordering.ccode, ordering.cus_name, ordering.phone)
    elif choice == "6":
        ccode = input("Enter ccode: ")
        ordering.delete_ordering()
    elif choice == "0":
          break
    else:
        print('enter again our choice')



