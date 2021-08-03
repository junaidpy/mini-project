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
    
    if product_name == '' and price == '':
        print('No input provided')
    elif product_name == '':
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
    
    if courier_name == '' and phone == '':
        print('No input has been provided in any field')
    
    elif courier_name == '':
        sql = "UPDATE couriers SET phone = %s WHERE courier_id = %s"
        val = (phone, courier_id)
    
    elif phone == '':
        sql = "UPDATE couriers SET courier_name = %s WHERE courier_id = %s"
        val = (courier_name, courier_id)
    
    else:
        sql = "UPDATE couriers SET courier_name = %s, phone = %s WHERE courier_id = %s"
        val = (courier_name, phone, courier_id)
    
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



def update_order_database():
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
            print(f'\norder id: {str(row[0])}, customer name: {row[1]}, customer_address: {row[2]}, customer_phone: {str(row[3])}, courier_id: {str(row[4])}, status: {row[5]}, product_id: {str(row[6])}')
            data += (f'order id: {str(row[0])}, customer name: {row[1]}, customer_address: {row[2]}, customer_phone: {str(row[3])}, courier_id: {str(row[4])}, status: {row[5]}, product_id: {str(row[6])}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    order_id = int(input('Choose order id (enter number): '))
    
    order_status = ['No Order', 'PREPARING', 'With Courier', 'Delivered']
    print(f'Order Status - 0 : {order_status[0]}, 1 : {order_status[1]}, 2 : {order_status[2]}, 3 : {order_status[3]}')
    update_status = int(input('Choose number for status: '))
    
    sql = "UPDATE orders SET the_status = %s WHERE order_id = %s"
    val = (order_status[update_status], order_id)
    
    
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'{order_status[update_status]} has been updated to order_id status: {order_id}.')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)
        print('Make sure input is not empty and that you chose a valid order id.')
    




def update_existing_order_database():
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
            print(f'\norder id: {str(row[0])}, customer name: {row[1]}, customer_address: {row[2]}, customer_phone: {str(row[3])}, courier_id: {str(row[4])}, status: {row[5]}, product_id: {str(row[6])}')
            data += (f'order id: {str(row[0])}, customer name: {row[1]}, customer_address: {row[2]}, customer_phone: {str(row[3])}, courier_id: {str(row[4])}, status: {row[5]}, product_id: {str(row[6])}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    order_id = input('Choose order id (enter number): ')
    
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
    
    sql = "UPDATE orders SET customer_name= %s, customer_address= %s, customer_phone= %s, courier_id= %s, product_id= %s WHERE order_id = %s"
    val = (customer_name, customer_address, customer_phone, courier_input, product_id, order_id)
    
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'Order has been updated. order_id: {order_id}.')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)
        print('Make sure input is not empty and that you chose a valid order id.')




def delete_order_database():
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
            print(f'\norder id: {str(row[0])}, customer name: {row[1]}, customer_address: {row[2]}, customer_phone: {str(row[3])}, courier_id: {str(row[4])}, status: {row[5]}, product_id: {str(row[6])}')
            data += (f'order id: {str(row[0])}, customer name: {row[1]}, customer_address: {row[2]}, customer_phone: {str(row[3])}, courier_id: {str(row[4])}, status: {row[5]}, product_id: {str(row[6])}')
    except Exception as e:
        print('Exception : ' + str(e))
    
    try:
        order_id = int(input('Choose order id (enter number): '))
    except Exception as e:
        print('\nMake sure you choose a valid integer\n')
        return delete_order_database()
    
    sql = "DELETE FROM orders WHERE order_id = %s"
    val = order_id
    
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(f'order_id: {order_id} has been DELETED.')
    except Exception as e:
        connection.rollback()
        print('Exception occurred : ', e)



def main_menu():
    print('\nMain Menu\n')
    
    import csv

    main_menu_options = {0: 'Exit',
                        1 : 'Lunch options',
                        2 : 'Courier option',
                        3 : 'Orders menu'}


    print(main_menu_options)

    user_input = int(input('\nPlease enter a number for options: ' ))
    while user_input !=0:
    
        if user_input == 0:
            try:
                with open('productdb.csv', 'w', newline= '') as productfile:
                    fieldnames = ['name', 'price']
                    csv_dict_writer = csv.DictWriter(productfile, fieldnames= fieldnames)
                    csv_dict_writer.writeheader()
                    for product in products:
                        csv_dict_writer.writerow(product)
            except FileNotFoundError as e:
                print('product.csv not saved. An error has occurred: ' + str(e))
            
            try:
                with open('couriersdb.csv', 'w', newline= '') as courierfile:
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
                
                with open('ordersdb.csv', 'w', newline= '') as ordersfile:
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
            
            elif product_menu_input == 2:
                insert_into_products()
            
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
        
        
        
        if user_input == 3:
            print(order_menu)
            order_menu_input = int(input('Please choose from options given (enter number): '))
            
            if order_menu_input == 0:
                main_menu()
            
            elif order_menu_input == 1:
                load_orders_database()
                
            elif order_menu_input == 2:
                create_order_database()
            
            elif order_menu_input == 3:
                update_order_database()
            
            elif order_menu_input == 4:
                update_existing_order_database()
            
            elif order_menu_input == 5:
                delete_order_database()
    


main_menu()