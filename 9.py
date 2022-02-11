from datetime import date


class Order_Management:
    def __init__(self):
        # product master data start:
        self.product_current_index = 1
        self.product_details = {}
        self.product_stock_details = {}
        # product master data end:

        # customer master data start:
        self.customer_current_index = 1
        self.customer_details = {}
        self.customer_address_details = {}
        # customer master data end:

        # sales order data start:
        self.order_current_index = 1
        self.sales_order_detail = {}
        # sales order data end:

    def manage_product(self):
        product_vals = self.prepare_product()
        self.create_product(product_vals)

    def prepare_product(self):
        product_name = input('Enter Product Name: ')
        product_unit_price = float(input('Enter Product Unit Price: '))
        product_cost_price = float(input('Enter Product Cost Price: '))
        product_type = input('Enter Product Type: ')
        product_stock = float(input('Enter initial stock: '))
        return {'name': product_name, 'product_unit_price': product_unit_price,
                'product_cost_price': product_cost_price,
                'product_type': 'Stockable', 'stock': product_stock}

    def create_product(self, product_vals):
        product_key = 'PRD' + str(self.product_current_index)
        self.product_details.update({product_key: {'name': product_vals['name'],
                                                   'product_unit_price': product_vals['product_unit_price'],
                                                   'product_cost_price': product_vals['product_cost_price'],
                                                   'product_type': product_vals['product_type']}})
        self.product_stock_details.update({product_key: product_vals['stock']})
        self.product_current_index += 1
        return product_key

    def display_product_data(self):
        if self.product_details:
            print('|{:<20}|{:>10}|{:>10}|{:<10}|{:>10}|'.format('SKU', 'Unit Price', 'Cost Price', 'Type', 'Stock'))
            for k in self.product_details.keys():
                print('|{:<20}|{:>10}|{:>10}|{:<10}|{:>10}|'.format('[' + k + ']' + self.product_details[k]['name'],
                                                                    str(self.product_details[k]['product_unit_price']),
                                                                    str(self.product_details[k]['product_cost_price']),
                                                                    self.product_details[k]['product_type'],
                                                                    str(self.product_stock_details[k])))
        else:
            print('Product not available...')

    def update_product_stock(self):
        self.display_product_data()
        product_key = input('Enter SKU code: ')
        if product_key not in self.product_stock_details:
            print('Product not found...')
        else:
            quantity = float(input('Enter quantity to update: '))
            self.product_stock_details[product_key] += quantity

    def manage_customer(self):
        customer_vals = self.prepare_customer()
        self.create_customer(customer_vals)

    def prepare_customer(self):
        customer_name = input('Enter customer name: ')
        customer_email = input('Enter e-mail id: ')
        customer_phone = input('Enter phone number: ')
        customer_address_1 = input('Enter address detail 1: ')
        customer_address_2 = input('Enter address detail 2: ')
        customer_city = input('Enter city name: ')
        customer_state = input('Enter state name: ')
        customer_country = input('Enter country name: ')
        customer_zip_code = input('Enter zip code: ')
        return {'name': customer_name, 'email': customer_email, 'phone': customer_phone, 'address1': customer_address_1,
                'address2': customer_address_2, 'city': customer_city, 'state': customer_state,
                'country': customer_country,
                'zipcode': customer_zip_code}

    def create_customer(self, customer_vals):
        customer_key = 'CUS_' + str(self.customer_current_index)
        self.customer_details.update({customer_key: {'name': customer_vals['name'],
                                                     'email': customer_vals['email'],
                                                     'phone': customer_vals['phone']}})
        self.customer_address_details.update({customer_key: {'address1': customer_vals['address1'],
                                                             'address2': customer_vals['address2'],
                                                             'city': customer_vals['city'],
                                                             'state': customer_vals['state'],
                                                             'country': customer_vals['country'],
                                                             'zipcode': customer_vals['zipcode']}})
        self.customer_current_index += 1
        return customer_key

    def display_customer_data(self):
        if self.customer_details:
            print('{:<20}'.format('Customer Name'))
            for k in self.customer_details.keys():
                print('{:<20}'.format('[' + k + ']' + self.customer_details[k]['name']))
        else:
            print('Customer data not found...')

    def generate_sales_order(self):
        order_vals = self.prepare_sales_order()
        if order_vals:
            self.create_sales_order(order_vals)

    def get_customer_for_sales_order(self):
        while True:
            self.display_customer_data()
            customer_id = input('Enter customer code: ')
            if customer_id not in self.customer_details:
                user_choice = int(input('Customer data not found, \n Press 1 for re-try \n Press 2 for exit'))
                if user_choice == 2:
                    customer_id = ''
                    break
                else:
                    continue
            else:
                break
        return customer_id

    def get_product_for_sales_order(self):
        while True:
            self.display_product_data()
            product_id = input('Enter product code: ')
            if product_id not in self.product_details:
                user_choice = int(input('Product data not found, \n Press 1 for re-try \n Press 2 for exit'))
                if user_choice == 2:
                    product_id = ''
                    break
                else:
                    continue
            else:
                break
        return product_id

    def prepare_sales_order(self):
        customer_id = self.get_customer_for_sales_order()
        if len(customer_id) == 0:
            print('Sales order cannot be created without customer data...')
        else:
            order_data = {}
            tmp_product_details = []
            order_total_amount = 0
            state = 'Draft'
            while True:
                product_id = self.get_product_for_sales_order()
                if len(product_id) == 0:
                    print('Sales order cannot be created without product data...')
                    break
                else:
                    quantity = float(input('Enter quantity: '))
                    unit_price = self.product_details[product_id]['product_unit_price']
                    tmp_list = [x['product_sku'] for x in tmp_product_details]
                    if product_id in tmp_list:
                        for x in tmp_product_details:
                            if x['product_sku'] == product_id:
                                x['quantity'] += quantity
                                sub_total = x['quantity'] * unit_price
                                x['sub_total'] = sub_total
                    else:
                        sub_total = quantity * unit_price
                        tmp_product_details.append({'product_sku': product_id, 'unit_price': unit_price,
                                                    'quantity': quantity,
                                                    'sub_total': sub_total, 'state': state})
                    for x in tmp_product_details:
                        order_total_amount += x['sub_total']
                    user_choice = int(input('Press 1 to add more product or Press 2 to exit: '))
                    if user_choice == 2:
                        order_data = {'customer': customer_id, 'order_lines': tmp_product_details,
                                      'order_date': date.today(),
                                      'state': state, 'order_total_amount': order_total_amount}
                        break
            return order_data

    def create_sales_order(self, order_vals):
        order_key = 'SO' + str(self.order_current_index)
        self.sales_order_detail = {order_key: order_vals}
        self.order_current_index += 1
        print(self.sales_order_detail)
        return order_key

    def display_sales_order(self):
        if self.sales_order_detail:
            for key, val in self.sales_order_detail.items():
                print('------------------------------------------------------------------')
                print('Customer Name: ', self.customer_details[val['customer']]['name'])
                print('Order Number: ', key)
                print('------------------------------------------------------------------')
                print('{:<20}|{:<10}|{:<10}|{:<10}|{:<15}|'.format('product_sku', 'unit_price',
                                                                   'quantity', 'sub_total',
                                                                   'state'))
                for order in val.get('order_lines'):
                    print('{:<20}|{:<10}|{:<10}|{:<10}|{:<15}|'.format(
                        order['product_sku'] + self.product_details[order['product_sku']]['name'], order['unit_price'],
                        order['quantity'], order['sub_total'],
                        order['state']))
                print('{:<20}|{:<10}|{:<10}|{:<10}|{:>15}|'.format('', '',
                                                                   '', 'Total',
                                                                   val.get('order_total_amount')))
        else:
            print('Order data not found...')

    def get_order_data(self):
        while True:
            self.display_sales_order()
            order_id = input('Enter Order Number to change state: ')
            if order_id not in self.sales_order_detail:
                user_choice = int(input('Order data not found, \n Press 1 for re-try \n Press 2 for exit'))
                if user_choice == 2:
                    order_id = ''
                    break
                else:
                    continue
            else:
                break
        return order_id

    def change_order_state(self):
        order_id = self.get_order_data()
        if len(order_id) > 0:
            print('1. Confirm Order')
            print('2. Cancel Order')
            print('3. Set to Draft')
            print('4. Set to Done')
            print('5. Move to Previous level')
            user_choice = int(input('Enter option: '))
            if user_choice == 1:
                for k in self.sales_order_detail.keys():
                    if k == order_id and self.sales_order_detail[k]['state'] == 'Confirm':
                        print('This order is already confirmed')
                    elif k == order_id and self.sales_order_detail[k]['state'] == 'Draft':
                        order_list = self.sales_order_detail[k]['order_lines']
                        for item in order_list:
                            item['state'] = 'Confirm'
                        self.sales_order_detail[k]['state'] = 'Confirm'
                        break
                    else:
                        print('This order cannot be confirmed...')
                        break
            elif user_choice == 2:
                for k in self.sales_order_detail.keys():
                    if k == order_id and self.sales_order_detail[k]['state'] == 'Cancel':
                        print('This order is already canceled')
                    elif k == order_id and self.sales_order_detail[k]['state'] != 'Done' and \
                            (self.sales_order_detail[k]['state'] == 'Draft' or
                             self.sales_order_detail[k]['state'] == 'Confirm'):
                        order_list = self.sales_order_detail[k]['order_lines']
                        for item in order_list:
                            item['state'] = 'Cancel'
                        self.sales_order_detail[k]['state'] = 'Cancel'
                        break
                    else:
                        print('This order cannot be cancel...')
                        break

            elif user_choice == 3:
                for k in self.sales_order_detail.keys():
                    if k == order_id and self.sales_order_detail[k]['state'] == 'Draft':
                        print('This order is already in draft')
                    elif k == order_id and self.sales_order_detail[k]['state'] == 'Cancel':
                        order_list = self.sales_order_detail[k]['order_lines']
                        for item in order_list:
                            item['state'] = 'Draft'
                        self.sales_order_detail[k]['state'] = 'Draft'
                        break
                    else:
                        print('This order cannot be draft...')
                        break

            elif user_choice == 4:
                for k in self.sales_order_detail.keys():
                    if k == order_id and self.sales_order_detail[k]['state'] == 'Done':
                        print('This order is already in done')
                    elif k == order_id and self.sales_order_detail[k]['state'] == 'Confirm' and \
                            self.sales_order_detail[k]['state'] != 'Cancel':
                        order_list = self.sales_order_detail[k]['order_lines']
                        for item in order_list:
                            item['state'] = 'Done'
                            self.product_stock_details[item['product_sku']] -= item['quantity']
                        self.sales_order_detail[k]['state'] = 'Done'
                        break
                    else:
                        print('This order cannot be done...')
                        break

        self.display_sales_order()

    def print_sales_order(self):
        if self.sales_order_detail:
            order_id = input('Enter order number to print: ')
            if order_id in self.sales_order_detail:
                for key, val in self.sales_order_detail.items():
                    print('Order Number: ', order_id, '                                Order Date: ',
                          self.sales_order_detail[key]['order_date'])
                    print('Order Status:', self.sales_order_detail[key]['state'])
                    print('Customer : ', order_id + ',' + self.customer_details[val['customer']]['name'])
                    print('Phone :', self.customer_details[val['customer']]['phone'])
                    print('E-Mail :', self.customer_details[val['customer']]['email'])
                    print('                             ', self.customer_address_details[val['customer']]['address1'])
                    print('                             ', self.customer_address_details[val['customer']]['address2'])
                    print('                             ', self.customer_address_details[val['customer']]['city'])
                    print('                             ', self.customer_address_details[val['customer']]['state'])
                    print('                             ', self.customer_address_details[val['customer']]['country'])
                    print('                             ', self.customer_address_details[val['customer']]['zipcode'])

                    print('{:<20}|{:<10}|{:<10}|{:<10}|{:<15}|'.format('product_sku', 'unit_price',
                                                                       'quantity', 'sub_total',
                                                                       'state'))
                    for order in val.get('order_lines'):
                        print('{:<20}|{:<10}|{:<10}|{:<10}|{:<15}|'.format(
                            order['product_sku'] + self.product_details[order['product_sku']]['name'],
                            order['unit_price'],
                            order['quantity'], order['sub_total'],
                            order['state']))
                    print('{:<20}|{:<10}|{:<10}|{:<10}|{:>15}|'.format('', '',
                                                                       '', 'Total',
                                                                       val.get('order_total_amount')))
            else:
                print('Order data not found...')
        else:
            print('Order records not fount...')

sales_order_management = Order_Management()
while True:
    print('1. Add Product')
    print('2. Display Product')
    print('3. Update Product Stock')
    print('4. Add Customer')
    print('5. Display Customer')
    print('6. Create Sales Order')
    print('7. Display Sales order list')
    print('8. Change Sales order state')
    print('9. Print Sales Order')
    print('10. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        sales_order_management.manage_product()
    elif choice == 2:
        sales_order_management.display_product_data()
    elif choice == 3:
        sales_order_management.update_product_stock()
    elif choice == 4:
        sales_order_management.manage_customer()
    elif choice == 5:
        sales_order_management.display_customer_data()
    elif choice == 6:
        sales_order_management.generate_sales_order()
    elif choice == 7:
        sales_order_management.display_sales_order()
    elif choice == 8:
        sales_order_management.change_order_state()
    elif choice == 9:
        sales_order_management.print_sales_order()
    else:
        exit(0)
