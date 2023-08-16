import csv
class Customer:
    def __init__(self, ccode, cus_name, phone):
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone
class TreeNode:
    def __init__(self, customer):
        self.left = None
        self.right = None
        self.customer = customer
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
        with open("customer.txt", "r") as file:
            for line in file:
                ccode, cus_name, phone= line.strip().split('\t')
                print(ccode.ljust(column_widths[0])+'|', end="\t")
                print('|',cus_name.ljust(column_widths[1]), end="\t")
                print('|',phone.ljust(column_widths[2]))
                
    # 2.2 Input & insert data
    def Input_add_to_the_end(self):
        ccode = str(input("Enter ccode: "))
        cus_name = str(input("Enter customer name: "))
        phone = int(input("Enter phone: "))
        customer = Customer(ccode, cus_name,phone)
        self.insert(customer)
        with open("customer.txt", "a") as file:
            file.write(f"{customer.ccode}\t{customer.cus_name}\t{customer.phone}\n")
        print("customer added successfully.")
        self.insert(customer)

    def insert(self, customer):
        if self.root is None:
            self.root = TreeNode(customer)
        else:
            self._insert_helper(customer, self.root)

    def _insert_helper(self, customer, current_node):
        if customer.ccode < current_node.customer.ccode:
            if current_node.left is None:
                current_node.left = TreeNode(customer)
            else:
                self._insert_helper(customer, current_node.left)
        elif customer.ccode > current_node.customer.ccode:
            if current_node.right is None:
                current_node.right = TreeNode(customer)
            else:
                self._insert_helper(customer, current_node.right)
                
    # 2.5 sreach by ccode
    def search_customer_by_ccode(self, ccode):
        return self._search_helper(ccode, self.root)

    def _search_helper(self, ccode, node):
        if node is None:
            return None
        elif node.customer.ccode == ccode:
            return node.customer
        elif node.customer.ccode < ccode:
            return self._search_helper(ccode, node.right)
        else:
            return self._search_helper(ccode, node.left)

    # 2.6 Delete by ccode by copying
    def delete_customer(self): 
        with open("customer.txt", "r") as file:
            lines = file.readlines()
            
        found = False
        with open("customer.txt", "w") as file:
            for line in lines:
                customer_data = line.strip().split('\t')
                if customer_data[0] != ccode:
                    file.write(line)
                else:
                    found = True

        if found:
            print("customer deleted successfully.")
        else:
            print("customer not found.")
    def delete_customer_by_ccode(self, ccode):
        self.root = self._delete_helper(ccode, self.root)

    def _delete_helper(self, ccode, node):
        if node is None:
            return node
        if ccode < node.customer.ccode:
            node.left = self._delete_helper(ccode, node.left)
        elif ccode > node.customer.ccode:
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
            node.customer = temp.customer
            node.right

# Create a binary tree object
customer = BinaryTree()

while True:
    print("--------------customer--------------")
    print("1. Load data from file")
    print("2. Input & add to the end")
    print("3. Display data")
    print("4. Save customer list to file")
    print("5. Search by ccode")
    print("6. Delete by ccode")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        customer.load_data_from_file()
        #customer.load_data_from_file()
    elif choice == "2":
        customer.Input_add_to_the_end()
    elif choice == "3":
        customer.load_data_from_file()
    elif choice == "4":
        customer.load_data_from_file()
    elif choice == "5":
        ccode = input("Enter ccode: ")
        customer = customer.search_customer_by_ccode(ccode)
        if customer is None:
            print("customer not found!")
        else:
            print(customer.ccode, customer.cus_name, customer.phone)
    elif choice == "6":
        ccode = input("Enter ccode: ")
        customer.delete_customer()
    elif choice == "0":
          break
    else:
        print('enter again our choice')


