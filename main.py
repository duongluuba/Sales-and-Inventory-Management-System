while True:
    print("main")
    print("1. Products ")
    print("2. Customer list ")
    print("3. Order list ")
    print("0. Exit ")
    choice = input("Enter your choice: ")
    if choice == "1":
        from product import product
    elif choice == "2":
        from customer import customer
    elif choice == "3":
        from ordering import ordering
    elif choice == "0":
          break