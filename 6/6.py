import csv

fields = []
csv_file_data = {}
file_name = 'demo.csv'

with open(file_name, 'r') as csv_data:
    reader = csv.reader(csv_data)
    fields = next(reader)
    countries = {'USA': 'United States of America', 'AU': 'Australia', 'DE': 'Germany', 'ES': 'Spain',
                 'UK': 'United Kingdom', 'IT': 'Italy'}
    for row in reader:
        if not csv_file_data.get(row[0]):
            csv_file_data.update({
                row[0]: {
                    'customer': {
                        'name': row[1],
                        'address1': row[5],
                        'address2': row[6],
                        'city': row[8],
                        'country': countries[row[9]],
                        'zipcode': row[7]
                    },
                    'orderlines': []
                }
            })
        csv_file_data[row[0]]['orderlines'].append({'sku': row[2], 'price': row[4], 'qty': row[3]})
    csv_data.close()

    print(csv_file_data)
