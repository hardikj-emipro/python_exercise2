class Manufacturing:
    def __init__(self, raw_material_product, finished_product, raw_material_ratio_quantity):
        self.raw_material_item = raw_material_product
        self.finished_item = finished_product
        self.raw_material_ratio_qty = raw_material_ratio_quantity
        self.raw_material_qty = 0
        self.finished_item_qty = 0

    def purchase_raw_material(self):
        self.raw_material_qty += int(input('Enter raw material quantity: '))

    def produce(self):
        a = int(input('Enter order quantity: '))
        if a*2 > self.raw_material_qty:
            print('Not enough raw material available to produce the product, please purchase, '
                  'Available raw material is: ', self.raw_material_qty)
        else:
            self.raw_material_qty -= (a*2)
            self.finished_item_qty += a

    def display_raw_material_stock(self):
        print('Stock of ', self.raw_material_item, 'is: ', self.raw_material_qty)

    def display_final_product_stock(self):
        print('Stock of ', self.finished_item, 'is: ', self.finished_item_qty)

obj = Manufacturing('Wheel', 'Bicycal', 2)

while True:
    print('1. Purchase Raw Material Product')
    print('2. Manufacture Finish Product')
    print('3. Show Raw Material Quantity')
    print('4. Show Actual Product Quantity')
    print('5. Exit')
    a = int(input('Enter your choice: '))
    if a == 1:
        obj.purchase_raw_material()
    elif a == 2:
        obj.produce()
    elif a == 3:
        obj.display_raw_material_stock()
    elif a == 4:
        obj.display_final_product_stock()
    elif a == 5:
        exit(0)
    else:
        print('Invalid input...')
