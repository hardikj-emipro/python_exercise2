class InventoryManagement:
    def __init__(self, product):
        self.finished_item = product
        self.finished_item_qty = 0

    def purchase(self):
        self.finished_item_qty += int(input('Enter quantity to purchase: '))

    def display_product_stock(self):
        print('Stock of ', self.finished_item, 'is: ', self.finished_item_qty)

    def sales(self):
        tmp = int(input('Enter quantity to sales: '))
        if tmp > self.finished_item_qty:
            print('Not enough product quantities to sell, available quantity is ', self.finished_item_qty)
        else:
            self.finished_item_qty -= tmp
            print('Available quantity after sales: ', self.finished_item_qty)

obj = InventoryManagement('Pencil')

while True:
    print('1. Purchase Product')
    print('2. Sales Product')
    print('3. View Available Product Quantities')
    print('4. Exit')
    a = int(input('Enter your choice: '))
    if a == 1:
        obj.purchase()
    elif a == 2:
        obj.sales()
    elif a == 3:
        obj.display_product_stock()
    elif a == 4:
        exit(0)
    else:
        print('Invalid input...')
