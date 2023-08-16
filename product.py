import csv
class Product:
    def __init__(self, pcode, pro_name, quantity, saled, price):
        self.pcode = pcode
        self.pro_name = pro_name
        self.quantity = quantity
        self.saled = saled
        self.price = price
class TreeNode:
    def __init__(self, product):
        self.left = None
        self.right = None
        self.product = product


class BinaryTree:
    def __init__(self):
        self.root = None

    # 1.1 Load data from file
    def load_data_from_file(self):
        column_widths = [6, 16, 8, 16, 10]
        column_names = ["pcode |", "| pro_name", "| quantity", "| saled", "| price"]
        for i, name in enumerate(column_names):
            print(name.ljust(column_widths[i]), end="\t")
        print()
        print("-" * (sum(column_widths) + 5 * (len(column_names) - 1)))
        with open("product.txt", "r") as file:
            for line in file:
                pcode, pro_name, quantity, saled, price = line.strip().split('\t')
                print(pcode.ljust(column_widths[0])+'|', end="\t")
                print('|',pro_name.ljust(column_widths[1]), end="\t")
                print('|',quantity.ljust(column_widths[2]), end="\t")
                print('|',saled.ljust(column_widths[3]), end="\t")
                print('|',price.ljust(column_widths[4]))
    # 1.2 Input & insert data
    def input_and_insert(self):
        pcode = str(input("Enter pcode: "))
        pro_name = str(input("Enter product name: "))
        quantity = int(input("Enter quantity: "))
        saled = int(input("Enter saled: "))
        price = int(input("Enter price: "))
        product = Product(pcode, pro_name, quantity, saled, price)
        self.insert(product)
        with open("product.txt", "a") as file:
            file.write(f"{product.pcode}\t{product.pro_name}\t{product.quantity}\t{product.saled}\t{product.price}\n")
        print("product added successfully.")
        self.insert(product)

    def insert(self, product):
        if self.root is None:
            self.root = TreeNode(product)
        else:
            self._insert_helper(product, self.root)

    def _insert_helper(self, product, current_node):
        if product.pcode < current_node.product.pcode:
            if current_node.left is None:
                current_node.left = TreeNode(product)
            else:
                self._insert_helper(product, current_node.left)
        elif product.pcode > current_node.product.pcode:
            if current_node.right is None:
                current_node.right = TreeNode(product)
            else:
                self._insert_helper(product, current_node.right)

    # 1.3 In-order traverse
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.product.pcode, node.product.pro_name, node.product.quantity, node.product.saled, node.product.price)
            self.inorder_traversal(node.right)

    # 1.4 Breadth-first traverse
    def breadth_first_traversal(self):
        if self.root is None:
            return
        q = []
        q.append(self.root)
        while len(q) > 0:
            node = q.pop(0)
            print(node.product.pcode, node.product.pro_name, node.product.quantity, node.product.saled, node.product.price)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    # 1.5 In-order traverse to file
    def inorder_traversal_to_file(self, node, file):
        if node is not None:
            self.inorder_traversal_to_file(node.left, file)
            file.write(f"{node.product.pcode},{node.product.pro_name},{node.product.quantity},{node.product.saled},{node.product.price}\n")
            self.inorder_traversal_to_file(node.right, file)

    # 1.6 Search by pcode
    def search_product_by_pcode(self, pcode):
        return self._search_helper(pcode, self.root)

    def _search_helper(self, pcode, node):
        if node is None:
            return None
        elif node.product.pcode == pcode:
            return node.product
        elif node.product.pcode < pcode:
            return self._search_helper(pcode, node.right)
        else:
            return self._search_helper(pcode, node.left)

    # 1.7 Delete by pcode by copying
    def delete_product(self): 
        with open("product.txt", "r") as file:
            lines = file.readlines()
            
        found = False
        with open("product.txt", "w") as file:
            for line in lines:
                product_data = line.strip().split('\t')
                if product_data[0] != pcode:
                    file.write(line)
                else:
                    found = True

        if found:
            print("product deleted successfully.")
        else:
            print("product not found.")
    def delete_product_by_pcode(self, pcode):
        self.root = self._delete_helper(pcode, self.root)

    def _delete_helper(self, pcode, node):
        if node is None:
            return node
        if pcode < node.product.pcode:
            node.left = self._delete_helper(pcode, node.left)
        elif pcode > node.product.pcode:
            node.right = self._delete_helper(pcode, node.right)
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
            node.product = temp.product
            node.right
    def count_products(self):
        return self._count_helper(self.root)
        

    def _count_helper(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._count_helper(node.left) + self._count_helper(node.right)
# Create a binary tree object
product = BinaryTree()

while True:
    print("--------------PRODUCTS--------------")
    print("1. Load data from file")
    print("2. Input and insert data")
    print("3. In-order traversal")
    print("4. Breadth-first traversal")
    print("5. In-order traversal to file")
    print("6. Search by pcode")
    print("7. Delete by pcode by copying")
    print("8. Simply balancing")
    print("9. Count number of products")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        product.load_data_from_file()
        #product.load_data_from_file()
    elif choice == "2":
        product.input_and_insert()
    elif choice == "3":
        product.inorder_traversal(product.root)
    elif choice == "4":
        product.breadth_first_traversal()
    elif choice == "5":
        filename = input("Enter filename: ")
        with open(filename, "w") as file:
            product.inorder_traversal_to_file(product.root, file)
    elif choice == "6":
        pcode = input("Enter pcode: ")
        product = product.search_product_by_pcode(pcode)
        if product is None:
            print("Product not found!")
        else:
            print(product.pcode, product.pro_name, product.quantity, product.saled, product.price)
    elif choice == "7":
        pcode = input("Enter pcode: ")
        product.delete_product()
    elif choice == "8":
        pass  # Implement simply balancing functionality here
    elif choice == "9":
        count = product.count_products()
        print(f"Number of products: {count}")
    elif choice == "0":
          break

