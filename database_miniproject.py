import pymysql
import os
from dotenv import load_dotenv

def load_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT product_id, product_name, price FROM products')
        rows = cursor.fetchall()
        data = ''
        for row in rows:
            print(f'id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
            data += (f'id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    cursor.close()
    connection.close()
    return data


def insert_into_products():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    
    product_name = input('What would you like to add? (enter name): ').capitalize()
    price = float(input('Set the price: '))
    sql = "INSERT INTO products (product_name, price) VALUES (%s, %s)"
    val = (product_name , price)
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'{product_name} has been added. Priced at: {price}')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)
    
    cursor.close()
    connection.close()


def update_product_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    
    try:
        cursor.execute('SELECT product_id, product_name, price FROM products')
        rows = cursor.fetchall()
        data = ''
        for row in rows:
            print(f'id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
            data += (f'id: {str(row[0])}, name: {row[1]}, price: {row[2]}-')
    except Exception as e:
        print('Exception : ' + str(e))
    
    try:
        product_id = int(input('Enter product_id to update: '))
    except Exception as e:
        print('\nMake sure you choose a valid integer\n')
        return update_product_database()
    
    product_name = input('What would you like to add? (enter name): ').capitalize()
    price = (input('Set the price: '))
    
    if product_name == '':
        sql = "UPDATE products SET price = %s WHERE product_id = %s"
        val = (price, product_id)
    elif price == '':
        sql = "UPDATE products SET product_name = %s WHERE product_id = %s"
        val = (product_name, product_id)
    else:
        sql = "UPDATE products SET product_name = %s, price = %s WHERE product_id = %s"
        val = (product_name, price, product_id)
    
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'product_id: {product_id} has been updated.')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)
        print('Make sure price input are integers or floats or that you chose a valid product id.')
    



def delete_product_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    
    try:
        cursor.execute('SELECT product_id, product_name, price FROM products')
        rows = cursor.fetchall()
        data = ''
        for row in rows:
            print(f'id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
            data += (f'id: {str(row[0])}, name: {row[1]}, price: {row[2]}-')
    except Exception as e:
        print('Exception : ' + str(e))
    
    try:
        product_id = int(input('Enter product_id to delete: '))
    except Exception as e:
        print('\nMake sure you choose a valid integer\n')
        return delete_product_database()
    
    sql = "DELETE FROM products WHERE product_id = %s"
    val = product_id
    
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'product_id: {product_id} has been DELETED.')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)
    



def load_courier_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT courier_id, courier_name, phone FROM couriers')
        rows = cursor.fetchall()
        data = ''
        for row in rows:
            print(f'id: {str(row[0])}, name: {row[1]}, phone: {row[2]}')
            data += (f'id: {str(row[0])}, name: {row[1]}, phone: {row[2]}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    cursor.close()
    connection.close()
    



def insert_into_couriers():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    
    courier_name = input('What name you like to add? (enter name): ').capitalize()
    phone = (input('Enter phone number: '))
    sql = "INSERT INTO couriers (courier_name, phone) VALUES (%s, %s)"
    val = (courier_name , phone)
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'{courier_name} has been added. Phone: {phone}')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)
    
    cursor.close()
    connection.close()



def update_existing_courier_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    
    try:
        cursor.execute('SELECT courier_id, courier_name, phone FROM couriers')
        rows = cursor.fetchall()
        data = ''
        for row in rows:
            print(f'id: {str(row[0])}, name: {row[1]}, phone: {row[2]}')
            data += (f'id: {str(row[0])}, name: {row[1]}, phone: {row[2]}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    try:
        courier_id = int(input('Enter courier_id to update: '))
    except Exception as e:
        print('\nMake sure you choose a valid integer\n')
        return update_existing_courier_database()
    
    courier_name = input('What name you like to add? (enter name) (Leave empty to skip): ').capitalize()
    phone = (input('Enter phone number(Leave empty to skip): '))
    
    #while courier_name and phone == '':
    if courier_name == '' and phone == '':
        print('No input has been provided in any field')
        #     break
    elif courier_name == '':
        sql = "UPDATE couriers SET phone = %s WHERE courier_id = %s"
        val = (phone, courier_id)
        #break
    elif phone == '':
        sql = "UPDATE couriers SET courier_name = %s WHERE courier_id = %s"
        val = (courier_name, courier_id)
        #break
    else:
        sql = "UPDATE couriers SET courier_name = %s, phone = %s WHERE courier_id = %s"
        val = (courier_name, phone, courier_id)
        #break
    
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'courier_id: {courier_id} has been updated.')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)
        print('Make sure input is not empty and that you chose a valid courier id.')



def delete_courier_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT courier_id, courier_name, phone FROM couriers')
        rows = cursor.fetchall()
        data = ''
        for row in rows:
            print(f'id: {str(row[0])}, name: {row[1]}, phone: {row[2]}')
            data += (f'id: {str(row[0])}, name: {row[1]}, phone: {row[2]}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    
    try:
        courier_id = int(input('Enter courier_id to delete: '))
    except Exception as e:
        print('\nMake sure you choose a valid integer\n')
        return delete_product_database()
    
    sql = "DELETE FROM couriers WHERE courier_id = %s"
    val = courier_id
    
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'courier_id: {courier_id} has been DELETED.')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)


def load_orders_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, courier_id, the_status, product_id FROM orders')
        rows = cursor.fetchall()
        data = ''
        for row in rows:
            print(f'order id: {str(row[0])}, customer name: {row[1]}, customer_address: {row[2]}, customer_phone: {str(row[3])}, courier_id: {str(row[4])}, status: {row[5]}, product_id: {str(row[6])}')
            data += (f'order id: {str(row[0])}, customer name: {row[1]}, customer_address: {row[2]}, customer_phone: {str(row[3])}, courier_id: {str(row[4])}, status: {row[5]}, product_id: {str(row[6])}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    cursor.close()
    connection.close()



def create_order_database():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    
    connection = pymysql.connect(
    host,
    user,
    password,
    database
    )
    
    cursor = connection.cursor()
    
    customer_name = input('What name you like to add? (enter name): ').capitalize()
    customer_address = input('Add Full Address: ').capitalize()
    customer_phone = (input('Enter phone number: '))
    
    
    try:
        cursor.execute('SELECT product_id, product_name, price FROM products')
        rows = cursor.fetchall()
        data = ''
        for row in rows:
            print(f'id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
            data += (f'id: {str(row[0])}, name: {row[1]}, price: {row[2]}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    product_id = input('Choose product (enter product id): ')
    
    
    try:
        cursor.execute('SELECT courier_id, courier_name, phone FROM couriers')
        rows = cursor.fetchall()
        data = ''
        for row in rows:
            print(f'id: {str(row[0])}, name: {row[1]}, phone: {row[2]}')
            data += (f'id: {str(row[0])}, name: {row[1]}, phone: {row[2]}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    courier_input = input('Please choose courier (enter courier_id): ')
    
    order_status = ['No Order', 'PREPARING', 'With Courier', 'Delivered']
    status = order_status[1]
    
    sql = "INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, the_status, product_id) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (customer_name , customer_address, customer_phone, courier_input, status, product_id)
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'order has been added')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)
    
    cursor.close()
    connection.close()




def create_new(products : list):
    name = input('product name: ').capitalize()
    price = float(input('enter price: '))
    
    new_dict = {}
    new_dict['name'] = name
    new_dict['price'] = price
    
    products.append(new_dict)
    print(f'{new_dict} has been added to {products}')
    return products

def update_dict_for_list(a_list):
    for i, name in enumerate(a_list):
        print(i, name)
    
    index = int(input('What would you like to update? (enter number): '))
    try:
        if index > i:
            print('index out of range or incorrect')
            return update_dict_for_list(a_list)
    except ValueError as e:
        print('index out of range or input incorrect')
        return update_dict_for_list(a_list)
    
    for dictionary in a_list:
        if a_list[index] is dictionary:
            update_order = dictionary
        
        updated_temp_dictionary = {}
    for key ,value in update_order.items():
        print(key + ':', value)
        update_input = input('Type to update (leave blank to keep previous data): ' + key + ': ')
        updated_temp_dictionary[key] = update_input
        
        
        print(updated_temp_dictionary)
        
        for k, v in updated_temp_dictionary.items():
            if updated_temp_dictionary[k] == '':
                pass
            else:
                update_order[k] = v
        print(update_order)
    return a_list 


def delete_dict_from_list(a_list):
    for i, name in enumerate(a_list):
        print(i, name)
    
    index = int(input('What would you like to delete? (enter number): '))
    try:
        if index > i:
            print('index out of range or incorrect')
            return delete_dict_from_list(a_list)
    except ValueError as e:
        print('index out of range or input incorrect')
        return delete_dict_from_list(a_list)
    
    print(a_list[index], ' has been deleted')
    del a_list[index]
    print(a_list)
    return a_list

def create_new_courier(courier : list):
    name = input('courier name: ').capitalize()
    phone = input('enter number: ')
    
    new_dict = {}
    new_dict['name'] = name
    new_dict['phone'] = phone
    
    courier.append(new_dict)
    print(f'{new_dict} has been added to {courier}')
    return courier


def input_for_order_dict_to_list(products:list, couriers:list, order_status:list, orders:list):
    cust_dict = {}
    customer_name =  input('Add name: ')
    customer_address = input('Add address: ')
    customer_phone_number = input('Please enter mobile number: ')
    
    cust_dict["customer_name"] = customer_name.capitalize()  
    cust_dict["customer_address"] = customer_address.upper()
    cust_dict["customer_phone"] = customer_phone_number
    print(cust_dict)
    
    items_index = []
    add_product = True
    while add_product:
        for i, name in enumerate(products):
            print(i, name)
        product_index = int(input('Which product would you like? (enter number): '))
        try:
            if product_index > i:
                print('index out of range or incorrect')
                return input_for_order_dict_to_list(products, couriers, order_status, orders)
        except ValueError as e:
            print('index out of range or input incorrect')
            return input_for_order_dict_to_list(products, couriers, order_status, orders)
        
        items_index.append(product_index)
        
        add_more = input('Do you want to add another product?(yes or no):\n ').lower()
        if add_more == 'no':
            add_product = False
        
    cust_dict['items'] = items_index
    
    
    for i, name in enumerate(couriers):
        print(i, name)
    
    select_index = int(input('Which courier would you like? (enter number): '))
    if select_index > i:
        print('index out of range or incorrect')
        main_menu()
    elif select_index <= i:
        print(f'The order status is {order_status[1]}')
        cust_dict["courier"] = select_index
        cust_dict["status"] = order_status[1]
    
    orders.append(cust_dict)
    


def update_existing_order_status(orders:list, order_status:list):
    for i, name in enumerate(orders):
        print(i, name)
    order_index = int(input('Which order status would you like to change? (enter number): '))
    try:
        if order_index > i:
            print('index out of range or incorrect')
            return update_existing_order_status(orders)
    except ValueError as e:
        print('index out of range or input incorrect')
        return update_existing_order_status(orders)

    for status in orders:
        if orders[order_index] is status:
            dict_status = status
        #print(type(status))

    for integer, status in enumerate(order_status):
        print(integer, status)

    if dict_status:
        new_order_status = int(input('select new order status (enter number): '))
        dict_status['status'] =  order_status[new_order_status]
        
    print(dict_status)
    print(f'Order status is updated.')



def update_existing_order(orders:list):
    for i, name in enumerate(orders):
            print(i, name)
    order_index = int(input('Which order would you like to change? (enter number): '))
    try:
        if order_index > i:
            print('index out of range or incorrect')
            return update_existing_order_status(orders)
    except ValueError as e:
        print('index out of range or input incorrect')
        return update_existing_order_status(orders)
        
    for dictionary in orders:
        if orders[order_index] is dictionary:
            update_order = dictionary
    
    updated_temp_dictionary = {}
    for key ,value in update_order.items():
        print(key + ':', value)
        update_input = input('Type to update (leave blank to keep previous data): ' + key + ': ')
        updated_temp_dictionary[key] = update_input
        
        
        print(updated_temp_dictionary)
    
    for k, v in updated_temp_dictionary.items():
        if updated_temp_dictionary[k] == '':
            pass
        else:
            update_order[k] = v
    print(update_order)


def delete_courier_from_order(orders:list):
    for i, name in enumerate(orders):
        print(i, name)
    order_index = int(input('\nWhich order would you like to DELETE? (enter number): '))
    try:
        if order_index > i:
            print('index out of range or incorrect')
            return delete_courier_from_order(orders)
    except ValueError as e:
        print('index out of range or input incorrect')
        return delete_courier_from_order(orders)
    
    print(f'\nDELETED: {orders[order_index]} has been deleted.')
    del orders[order_index]
    print(f'\nThe current order list is {orders}\n')


def main_menu():
    print('\nMain Menu\n')
    #initalise products, couriers and orders list
    import csv

    # products = []
    # #read csv
    # try:
    #     with open('product.csv', 'r') as productfile:
    #         csv_dict_reader = csv.DictReader(productfile)
    #         for row in csv_dict_reader:
    #             price = float(row['price'])
    #             products.append({
    #                 'name' : row['name'],
    #                 'price' : price
    #             })
    # except FileNotFoundError as e:
    #     print('An error has occurred: ' + str(e))


    # couriers = []

    # try:
    #     with open('couriers.csv', 'r') as courierfile:
    #         csv_dict_reader = csv.DictReader(courierfile)
    #         for row in csv_dict_reader:
    #             couriers.append({
    #                 'name' : row['name'],
    #                 'phone' : row['phone']
    #             })
    # except FileNotFoundError as e:
    #     print('An error has occurred: ' + str(e))


    # orders = []

    # try:
    #     with open('orders.csv', 'r') as ordersfile:
    #         csv_dict_reader = csv.DictReader(ordersfile)
    #         for row in csv_dict_reader:
    #             orders.append({
    #                 "customer_name": row["customer_name"],
    #                 "customer_address": row["customer_address"],
    #                 "customer_phone" : row["customer_phone"],
    #                 "courier" : int(row["courier"]),
    #                 "status" : row["status"],
    #                 "items" : row["items"]
    #             })
    # except FileNotFoundError as e:
    #     print('An error has occurred: ' + str(e))

    # #convert 'items' str values into int and list 
    # for i in range(len(orders)):
    #     test = orders[i]['items']
    #     orders[i]['items'] = list(map(int,test.split()))
    
    
    # Main menu and product menu dictionaries

    main_menu_options = {0: 'Exit',
                        1 : 'Lunch options',
                        2 : 'Courier option',
                        3 : 'Orders menu'}


    print(main_menu_options)

    user_input = int(input('\nPlease enter a number for options: ' ))
    
    if user_input == 0:
        try:
            with open('product.csv', 'w', newline= '') as productfile:
                fieldnames = ['name', 'price']
                csv_dict_writer = csv.DictWriter(productfile, fieldnames= fieldnames)
                csv_dict_writer.writeheader()
                for product in products:
                    csv_dict_writer.writerow(product)
        except FileNotFoundError as e:
            print('product.csv not saved. An error has occurred: ' + str(e))
        
        try:
            with open('couriers.csv', 'w', newline= '') as courierfile:
                fieldnames = ['name', 'phone']
                csv_dict_writer = csv.DictWriter(courierfile, fieldnames= fieldnames)
                csv_dict_writer.writeheader()
                for courier in couriers:
                    csv_dict_writer.writerow(courier)
        except FileNotFoundError as e:
            print('couriers.csv not saved. An error has occurred: ' + str(e))
        
        
        try:
            for i in range(len(orders)):
                test = orders[i]['items']
                numbers = ""
                for num in test:
                    numbers += " "+(str(num))
                orders[i]['items'] = numbers
            
            with open('orders.csv', 'w', newline= '') as ordersfile:
                fieldnames = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]
                csv_dict_writer = csv.DictWriter(ordersfile, fieldnames= fieldnames)
                csv_dict_writer.writeheader()
                for order in orders:
                    csv_dict_writer.writerow(order)
        except FileNotFoundError as e:
            print('orders.csv not saved. An error has occurred: ' + str(e))
    
        print('Exit')
        exit()
    
    
    product_menu = { 0 : 'Go back to main menu', 
                    1 : 'Product List', 
                    2 : 'Create/Add New Product', 
                    3 : 'Update your Product list',
                    4 : 'Delete Product' }
    
    if user_input == 1:
        print('\n')
        print(product_menu)
        product_menu_input = int(input('Please choose which option you would like(type number): '))
        
        if product_menu_input == 0:
            main_menu()
        
        elif product_menu_input == 1:
            load_database()
            
            # print(products)
        
        elif product_menu_input == 2:
            insert_into_products()
            #create_new(products)
        
        elif product_menu_input == 3:
            update_product_database()
        
        elif product_menu_input == 4:
            delete_product_database()
    
    
    courier_menu = { 0 : 'Return to Main Menu',
                1 : 'See Couriers',
                2 : 'Add Courier',
                3 : 'Update Courier Name',
                4 : 'Delete Courier'}
    
    
    if user_input == 2:
        print(courier_menu)
        courier_menu_input = int(input('Please choose from the options(number): '))
        
        if courier_menu_input == 0:
            main_menu()
        
        elif courier_menu_input == 1:
            print('couriers should print')
            load_courier_database()
        
        elif courier_menu_input == 2:
            print('couriers should be added/created')
            insert_into_couriers()
        
        elif courier_menu_input == 3:
            print('couriers should print update option')
            update_existing_courier_database()
        
        elif courier_menu_input == 4:
            print('couriers should print DELETE option')
            delete_courier_database()
    
    order_menu = {0 : 'Back to main menu', 
                1 : 'Order details',
                2 : 'Enter customer details',
                3: 'Update order status',
                4: 'Update existing order',
                5: 'Delete Order'}
    
    order_status = ['No Order', 'PREPARING', 'With Courier', 'Delivered']
    
    if user_input == 3:
        print(order_menu)
        order_menu_input = int(input('Please choose from options given (enter number): '))
        
        if order_menu_input == 0:
            main_menu()
        
        elif order_menu_input == 1:
            load_orders_database()
            
        elif order_menu_input == 2:
            #input_for_order_dict_to_list(products,couriers,order_status,orders)
            create_order_database()
        
        elif order_menu_input == 3:
            update_existing_order_status(orders, order_status)
        
        elif order_menu_input == 4:
            update_existing_order(orders)
        
        elif order_menu_input == 5:
            delete_courier_from_order(orders)
    
    
    # try:
    #     with open('product.csv', 'w', newline= '') as productfile:
    #         fieldnames = ['name', 'price']
    #         csv_dict_writer = csv.DictWriter(productfile, fieldnames= fieldnames)
    #         csv_dict_writer.writeheader()
    #         for product in products:
    #             csv_dict_writer.writerow(product)
    # except FileNotFoundError as e:
    #     print('product.csv not saved. An error has occurred: ' + str(e))
        
    # try:
    #     with open('couriers.csv', 'w', newline= '') as courierfile:
    #         fieldnames = ['name', 'phone']
    #         csv_dict_writer = csv.DictWriter(courierfile, fieldnames= fieldnames)
    #         csv_dict_writer.writeheader()
    #         for courier in couriers:
    #             csv_dict_writer.writerow(courier)
    # except FileNotFoundError as e:
    #     print('couriers.csv not saved. An error has occurred: ' + str(e))
        
        
    # try:
    #     for i in range(len(orders)):
    #         test = orders[i]['items']
    #         numbers = ""
    #         for num in test:
    #             numbers += " "+(str(num))
    #         orders[i]['items'] = numbers
        
    #     with open('orders.csv', 'w', newline= '') as ordersfile:
    #         fieldnames = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]
    #         csv_dict_writer = csv.DictWriter(ordersfile, fieldnames= fieldnames)
    #         csv_dict_writer.writeheader()
    #         for order in orders:
    #             csv_dict_writer.writerow(order)
    # except FileNotFoundError as e:
    #     print('orders.csv not saved. An error has occurred: ' + str(e))
    
    

main_menu()