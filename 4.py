class InventoryManagement:
    def __init__(self, product):
        self.product = {}
        self.current_index = 2
        for k in range(len(product)):
            product[k]['subtotal'] = product[k]['price'] * product[k]['quantity']
            self.product[k + 1] = product[k]
        self.total_product_quantity = sum([value['quantity'] for key, value in self.product.items()])
        print(self.product)

    def purchase(self, product):
        self.current_index += 1
        product['subtotal'] = product['price'] * product['quantity']
        self.product[self.current_index] = product
        self.total_product_quantity = sum([y['quantity'] for x, y in self.product.items()])
        print(self.product)

    def sales(self, no_of_product):
        delete_key_list = []
        total_quantity = sum([y['quantity'] for x, y in self.product.items()])
        if total_quantity >= no_of_product:
            for k in self.product.keys():
                first_product = self.product.get(k)
                if no_of_product > 0:
                    if no_of_product >= first_product['quantity']:
                        no_of_product -= first_product['quantity']
                        first_product['quantity'] = 0
                    elif first_product['quantity'] >= no_of_product:
                        tmp = no_of_product
                        first_product['quantity'] -= no_of_product
                        no_of_product -= tmp
                        first_product['subtotal'] = first_product['price'] * first_product['quantity']
                    if first_product['quantity'] == 0:
                        delete_key_list.append(k)
        else:
            print("Not enough product quantities to sell!")

        for val in delete_key_list:
            self.product.pop(val)
        print(self.product)

    def display_product(self):
        print("Total available products in the Inventory")
        print(self.product)
        print("\n\nProduct Price          qty")
        print("________________________________")
        for no, product_details in self.product.items():
            print("{:<18}{:<18}".format(product_details['price'], product_details['quantity']))

    def product_valuation(self):
        sub_total = 0
        for key, value in self.product.items():
            sub_total += value['subtotal']
        valuation = sub_total / self.total_product_quantity
        print("Valuation :  ", valuation)


inventory_management = InventoryManagement([
    {"price": 400, "quantity": 10},
    {"price": 350, "quantity": 30}
])
while True:
    print("""
        1. Purchase Product
        2. Sale Product
        3. View Available Product Quantities
        4. Show Valuation
        5. Exit
    """)
    option = int(input("Choose the option:  "))

    if option == 1:
        price = int(input("price: "))
        quantity = int(input("quantity: "))
        inventory_management.purchase({'price': price, 'quantity': quantity})

    elif option == 2:
        sale_no_of_product = int(input("Enter no. of product you want to sale: "))
        inventory_management.sales(sale_no_of_product)

    elif option == 3:
        inventory_management.display_product()

    elif option == 4:
        inventory_management.product_valuation()

    elif option == 5:
        exit(0)
    else:
        print("Please select right option!")
