import csv

# Binary Search Tree Node
from builtins import print


class TreeNode:
    def __init__(self, pcode, pro_name, quantity, saled, price):
        self.pcode = pcode
        self.pro_name = pro_name
        self.quantity = quantity
        self.saled = saled
        self.price = price
        self.left = None
        self.right = None



# # Binary Search Tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # def load_products_from_file(self, filename):
    #     with open(filename, 'r') as file:
    #         csv_reader = csv.reader(file)
    #         next(csv_reader)  # Skip the header row if it exists
    #         for row in csv_reader:
    #             pcode, pro_name, quantity, saled, price = row
    #             self.insert(pcode, pro_name, int(quantity), int(saled), float(price))

    def insert(self, pcode, pro_name, quantity, saled, price):
        node = TreeNode(pcode, pro_name, quantity, saled, price)
        if self.root is None:
            self.root = node
        else:
            self._insert_recursive(self.root, node)

    def _insert_recursive(self, current, node):
        if node.pcode < current.pcode:
            if current.left is None:
                current.left = node
            else:
                self._insert_recursive(current.left, node)
        elif node.pcode > current.pcode:
            if current.right is None:
                current.right = node
            else:
                self._insert_recursive(current.right, node)
        else:
            # Update the node if pcode already exists
            current.pro_name = node.pro_name
            current.quantity = node.quantity
            current.saled = node.saled
            current.price = node.price

    def inorder_traverse(self, node):
        if node is not None:
            self.inorder_traverse(node.left)
            print("Pcode:", node.pcode)
            print("Name:", node.pro_name)
            print("Quantity:", node.quantity)
            print("Saled:", node.saled)
            print("Price:", node.price)
            print()
            self.inorder_traverse(node.right)

    def breadth_first_traverse(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print("Pcode:", current.pcode)
            print("Name:", current.pro_name)
            print("Quantity:", current.quantity)
            print("Saled:", current.saled)
            print("Price:", current.price)
            print()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def inorder_traverse_to_file(self, node, file):
        if node is not None:
            self.inorder_traverse_to_file(node.left, file)
            file.write(f"{node.pcode},{node.pro_name},{node.quantity},{node.saled},{node.price}\n")
            self.inorder_traverse_to_file(node.right, file)

    def search_by_pcode(self, pcode):
        current = self.root
        while current:
            if pcode < current.pcode:
                current = current.left
            elif pcode > current.pcode:
                current = current.right
            else:
                return current
        return None

    def delete_by_pcode(self, pcode):
        self.root = self._delete_recursive(self.root, pcode)

    def _delete_recursive(self, current, pcode):
        if current is None:
            return None

        if pcode < current.pcode:
            current.left = self._delete_recursive(current.left, pcode)
        elif pcode > current.pcode:
            current.right = self._delete_recursive(current.right, pcode)
        else:
            # Case 1: No child or one child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            # Case 2: Two children
            else:
                successor = self._get_min_node(current.right)
                current.pcode = successor.pcode
                current.pro_name = successor.pro_name
                current.quantity = successor.quantity
                current.saled = successor.saled
                current.price = successor.price
                current.right = self._delete_recursive(current.right, successor.pcode)
        return current

    def _get_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def simply_balancing(self):
        nodes = self._extract_nodes_inorder(self.root)
        self.root = self._build_balanced_tree(nodes, 0, len(nodes) - 1)

    def _extract_nodes_inorder(self, node):
        nodes = []
        self._inorder_extract(node, nodes)
        return nodes

    def _inorder_extract(self, node, nodes):
        if node is not None:
            self._inorder_extract(node.left, nodes)
            nodes.append(node)
            self._inorder_extract(node.right, nodes)

    def _build_balanced_tree(self, nodes, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = nodes[mid]

        node.left = self._build_balanced_tree(nodes, start, mid - 1)
        node.right = self._build_balanced_tree(nodes, mid + 1, end)

        return node

    def count_products(self, node):
        if node is None:
            return 0
        return 1 + self.count_products(node.left) + self.count_products(node.right)


# Linked List Node for Customer
class CustomerNode:
    def __init__(self, ccode, cus_name, phone):
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone
        self.next = None


# Linked List for Customer
class CustomerList:
    def __init__(self):
        self.head = None

    def add(self, ccode, cus_name, phone):
        node = CustomerNode(ccode, cus_name, phone)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def display(self):
        current = self.head
        while current:
            print("Ccode:", current.ccode)
            print("Name:", current.cus_name)
            print("Phone:", current.phone)
            print()
            current = current.next

    def search_by_ccode(self, ccode):
        current = self.head
        while current:
            if ccode == current.ccode:
                return current
            current = current.next
        return None

    def delete_by_ccode(self, ccode):
        if self.head is None:
            return
        if self.head.ccode == ccode:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current:
            if current.ccode == ccode:
                prev.next = current.next
                break
            prev = current
            current = current.next


# Linked List Node for Order
class OrderNode:
    def __init__(self, pcode, ccode, quantity):
        self.pcode = pcode
        self.ccode = ccode
        self.quantity = quantity
        self.next = None


# Linked List for Order
class OrderList:
    def __init__(self):
        self.head = None

    def add(self, pcode, ccode, quantity):
        node = OrderNode(pcode, ccode, quantity)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def display(self):
        current = self.head
        while current:
            print("Pcode:", current.pcode)
            print("Ccode:", current.ccode)
            print("Quantity:", current.quantity)
            print()
            current = current.next

    def sort_by_pcode_ccode(self):
        if self.head is None:
            return
        sorted_list = []
        current = self.head
        while current:
            sorted_list.append((current.pcode, current.ccode, current.quantity))
            current = current.next
        sorted_list.sort(key=lambda x: (x[0], x[1]))  # Sort by pcode first, then ccode
        self.head = None
        for item in sorted_list:
            self.add(item[0], item[1], item[2])


def load_products_from_file(filename):
    product_tree = BinarySearchTree()
#     with open(filename, 'r') as file:
#         for line in file:
#             pcode, pro_name, quantity, saled, price = line.strip().split(',')
#             product_tree.insert(pcode, pro_name, int(quantity), int(saled), float(price))
#     return product_tree
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists
        for row in csv_reader:
            pcode, pro_name, quantity, saled, price = row
            product_tree.insert(pcode, pro_name, int(quantity), int(saled), float(price))
    return product_tree



def input_and_insert_product(product_tree):
    pcode = input("Enter the product code: ")
    pro_name = input("Enter the product name: ")
    quantity = int(input("Enter the product quantity: "))
    saled = int(input("Enter the number of products sold: "))
    price = float(input("Enter the product price: "))
    product_tree.insert(pcode, pro_name, quantity, saled, price)
    print("Product inserted successfully!")

def main():
    product_tree = BinarySearchTree()
    customer_list = CustomerList()
    order_list = OrderList()

    while True:
        print("Menu:")
        print("1. Products")
        print("2. Customer list")
        print("3. Order list")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Products:")
            print("1. Load data from file")
            print("2. Input & insert data")
            print("3. In-order traverse")
            print("4. Breadth-first traverse")
            print("5. In-order traverse to file")
            print("6. Search by pcode")
            print("7. Delete by pcode by copying")
            print("8. Simply balancing")
            print("9. Count number of products")

            product_choice = input("Enter your choice: ")

            if product_choice == '1':
                filename = input("Enter the filename: ")
                product_tree = load_products_from_file(filename)
                print("Data loaded successfully!")

            elif product_choice == '2':
                input_and_insert_product(product_tree)

            elif product_choice == '3':
                print("In-order traversal:")
                product_tree.inorder_traverse(product_tree.root)

            elif product_choice == '4':
                print("Breadth-first traversal:")
                product_tree.breadth_first_traverse()

            elif product_choice == '5':
                filename = input("Enter the filename: ")
                with open(filename, 'w') as file:
                    product_tree.inorder_traverse_to_file(product_tree.root, file)
                print("Data written to file successfully!")

            elif product_choice == '6':
                pcode = input("Enter the product code to search: ")
                result = product_tree.search_by_pcode(pcode)
                if result:
                    print("Product found:")
                    print("Pcode:", result.pcode)
                    print("Name:", result.pro_name)
                    print("Quantity:", result.quantity)
                    print("Saled:", result.saled)
                    print("Price:", result.price)
                else:
                    print("Product not found!")

            elif product_choice == '7':
                pcode = input("Enter the product code to delete: ")
                product_tree.delete_by_pcode(pcode)
                print("Product deleted successfully!")

            elif product_choice == '8':
                product_tree.simply_balancing()
                print("Tree balanced successfully!")

            elif product_choice == '9':
                count = product_tree.count_products(product_tree.root)
                print("Number of products:", count)

            else:
                print("Invalid choice. Please try again.")

        elif choice == '2':
            print("Customer list:")
            print("1. Load data from file")
            print("2. Input & add to the end")
            print("3. Display data")
            print("4. Save customer list to file")
            print("5. Search by ccode")
            print("6. Delete by ccode")

            customer_choice = input("Enter your choice: ")

            if customer_choice == '1':
                # Load data from file for customer list
                filename = input("Enter the filename: ")
                with open(filename, 'r') as file:
                    csv_reader = csv.reader(file)
                    next(csv_reader)  # Skip the header row
                    for row in csv_reader:
                        ccode, cus_name, phone = row
                        customer_list.add(ccode, cus_name, phone)
                print("Data loaded successfully.")

            elif customer_choice == '2':
                # Input & add to the end for customer list
                ccode = input("Enter ccode: ")
                cus_name = input("Enter customer name: ")
                phone = input("Enter phone number: ")
                customer_list.add(ccode, cus_name, phone)
                print("Data added successfully.")

            elif customer_choice == '3':
                # Display data for customer list
                print("Customer List:")
                customer_list.display()

            elif customer_choice == '4':
                # Save customer list to file
                filename = input("Enter the filename: ")
                with open(filename, 'w') as file:
                    current = customer_list.head
                    while current:
                        file.write(current.ccode + "," + current.cus_name + "," + current.phone + "\n")
                        current = current.next
                print("Data written to file successfully.")

            elif customer_choice == '5':
                # Search by ccode for customer list
                ccode = input("Enter the ccode to search: ")
                result = customer_list.search_by_ccode(ccode)
                if result:
                    print("Customer found:")
                    print("Ccode:", result.ccode)
                    print("Name:", result.cus_name)
                    print("Phone:", result.phone)
                else:
                    print("Customer not found.")

            elif customer_choice == '6':
                # Delete by ccode for customer list
                ccode = input("Enter the ccode to delete: ")
                customer_list.delete_by_ccode(ccode)
                print("Customer deleted successfully.")

            else:
                print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Order list:")
            print("1. Input data")
            print("2. Display ordering data")
            print("3. Sort by pcode + ccode")
            print("4. Load data from file")

            order_choice = input("Enter your choice: ")

            if order_choice == '1':
                # Input data for order list
                pcode = input("Enter pcode: ")
                ccode = input("Enter ccode: ")
                quantity = int(input("Enter quantity: "))
                order_list.add(pcode, ccode, quantity)
                print("Data added successfully.")

            elif order_choice == '2':
                # Display ordering data for order list
                print("Order List:")
                order_list.display()

            elif order_choice == '3':
                # Sort by pcode + ccode for order list
                order_list.sort_by_pcode_ccode()
                print("Order list sorted successfully.")

            elif order_choice == '4':

                filename = input("Enter the filename: ")
                with open(filename, 'r') as file:
                    csv_reader = csv.reader(file)
                    next(csv_reader)  # Skip the header row
                    for row in csv_reader:
                        try:
                            pcode = row[0]
                            ccode = row[1]
                            quantity = row[2]
                            order_list.add(pcode, ccode, int(quantity))
                            print("Orders loaded successfully!")
                        except:
                            print("Fail")


            else:
                print("Invalid choice. Please try again.")

        elif choice == '0':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
