import datetime


def dict_from_entries(keys, values):
    new_dict = {}
    for i in range(len(keys)):
        new_dict[keys[i]] = values[i]
    return new_dict


def safe_input(input_type, message):
    while True:
        value = input(message).strip()
        if value:
            if input_type == 'string':
                return value
            elif input_type == 'int_positive' and value.isnumeric():
                return int(value)
            elif input_type == 'float_positive' and value.replace('.', '').isnumeric():
                return float(value)


def find_by_key(dict_list, key, value):
    for el in dict_list:
        if str(el[key]).upper() == str(value).upper():
            return el


def select_by_id_or_name(dict_list, name):
    while True:
        selected = None
        name_or_id = safe_input('string', 'Name or Id: ')
        print()

        if name_or_id.isdecimal():
            selected = find_by_key(dict_list, 'id', int(name_or_id))
        else:
            selected = find_by_key(dict_list, 'name', name_or_id)

        if selected:
            return selected
        else:
            print("No %s with that criteria." % name)
            print("Try again")


def today():
    date = datetime.datetime.now()
    return date.strftime("%x")

keys = ('pcode', 'pro_name', 'quantity', 'saled', 'price')
def get_products():
    data = []
    file = open('assginment.csv')

  #  search = input('ID or name of the product?: ')
    for line in file:
        spacing = line.split(',')
        product = {
            "pcode": str(spacing[0]),
            "pro_name": int(spacing[1]),
            "quantity": int(spacing[2]),
            "saled": int(spacing[3]),
            "price": int(spacing[4]).replace('\n', '')
        }
        data.append(product)

    file.close()
    return data


def update_products(product_list):
    file = open('assginment.csv', 'w')
    for p in product_list:
        line = dict_to_csv_line(p, keys)
        file.write(line)

    file.close()
get_products()