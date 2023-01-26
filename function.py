def read_data_from_file(name):
    rawdata_list = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            rawdata_list.append(line.strip('\n').split(','))
        return rawdata_list

def save_data_to_file(name, rawdata_list):
    with open(name, 'w', encoding='utf8') as datafile:
        for rawdata in rawdata_list:
            datafile.write(','.join(rawdata) +'\n') 

def print_bus():
    bus = read_data_from_file('bus.txt')
    for name, number in bus:
        print('{},{}'.format(name, number))


def add_bus():
    name, number = input('Номер автобуса -> Bus_**:'), input("Госномер: ")
    add_item_to_file('bus.txt', [name, number])
    # save_data_to_file('bus.txt', input("Введите параметры автобуса: "))


def print_driver():
    drivers = read_data_from_file('driver.txt')
    for firstname, lastname in drivers:
        print('{},{}'.format(firstname, lastname))


def add_driver():
    firstname = input('Номер водителя -> driver№№:')
    lastname = input("Фамилия: ")
    add_item_to_file('driver.txt', [firstname, lastname])
    # save_data_to_file('driver.txt', input("Введите нового водителя: "))

def print_route():
    routes = read_data_from_file('route.txt')
    buses = read_data_from_file('bus.txt')
    drivers = read_data_from_file('driver.txt')
    for r_name,r_number,r_bus,r_driver in routes:
        bus_number = get_item_by_id(r_bus,buses)
        driver_name = get_item_by_id(r_driver,drivers)
        print('{},{},{},{}'.format(r_name,r_number,driver_name,bus_number))    

def get_item_by_id(id,records):
    for id_record,item_record in records:
        if id==id_record:
            return item_record
            break
    return None

def add_route():
    save_data_to_file('route.txt', input("Введите новый маршрут: "))

def add_item_to_file(name, rawdata):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(','.join(rawdata)+'\n')