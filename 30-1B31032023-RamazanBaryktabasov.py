import sqlite3


conn = sqlite3.connect('hw.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price NUMERIC(10, 2) NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')
conn.commit()


def add_products():
    products = [
        ('Товар 1', 9.99, 5),
        ('Товар 2', 19.99, 10),
        ('Товар 3', 29.99, 2),

    ]
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    conn.commit()

def change_quantity(product_id, new_quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()

def change_price(product_id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()


def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()


def select_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)


def select_products_less_than_100_and_quantity_greater_than_5():
    cursor.execute('SELECT * FROM products WHERE price < 100.0 AND quantity > 5')
    products = cursor.fetchall()
    for product in products:
        print(product)


def search_products_by_title(keyword):
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%{}%'.format(keyword),))
    products = cursor.fetchall()
    for product in products:
        print(product)


add_products()
change_quantity(1, 3)
change_price(2, 39.99)
delete_product(3)
select_all_products()
select_products_less_than_100_and_quantity_greater_than_5()
search_products_by_title('мыло')


conn.close()

        