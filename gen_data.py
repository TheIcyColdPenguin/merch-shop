import sqlite3


def create_table1():
    return '''
    create table USERS (
        id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        name text NOT NULL,
        password text NOT NULL,
        role textNOT NULL
    )
    '''


def insert_users1():
    users = [
        ('TheIcyColdPenguin', 'password123', 'admin'),
        ('Bob Ross', 'ahappylittlepainting123', 'user'),
        ('John Wick', 'uCL<XS_dog_nq-A24Dy6', 'user'),
        ('Elon Musk', 'YX3S', 'user'),
        ('i_like_cookies', "noteveryoneknowsthisbutcookiesaregreat", 'user'),
        ('Michael Scott', 'whyareyouthewayyouare', 'user'),
    ]

    for name, passw, role in users:
        yield f'INSERT INTO USERS VALUES (NULL, "{name}", "{passw}", "{role}");'


def create_table2():
    return '''
    create table ITEMS (
        id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        apparel text NOT NULL,
        material text NOT NULL,
        cost integer NOT NULL
    )
    '''


def insert_users2():
    users = [
        ('White Cap', 'nylon', '1200'),
        ('Blue Cap', 'nylon', '1200'),
        ('Green Cap', 'nylon', '1200'),
        ('Black Cap', 'nylon', '1200'),
        ('White Hoodie', 'wool', '2500'),
        ('Black Hoodie', 'wool', '2500'),
        ('Blue Hoodie', 'wool', '2500'),
        ('Red Hoodie', 'wool', '2500'),
        ('Red T-shirt', 'synthetic', '2500'),
        ('Blue T-shirt', 'synthetic', '2500'),
        ('Purple T-shirt', 'synthetic', '2500'),
        ('Skinny jeans', 'denim', '3600'),
        ('Slim jeans', 'denim', '3600'),
        ('Regular jeans', 'denim', '3600'),
        ('Sneakers', 'leather', '5000'),
    ]

    for apparel, material, cost in users:
        yield f'INSERT INTO ITEMS VALUES (NULL, "{apparel}", "{material}", {cost});'


def main():
    input('Waiting to clear database')

    with open("important.db", "wb+") as database:
        database.write(b"")

    input('Cleared database, waiting to write data')

    with sqlite3.connect('important.db') as conn:

        conn.execute(create_table1())

        for command in insert_users1():
            conn.execute(command)

        conn.execute(create_table2())

        for command in insert_users2():
            conn.execute(command)


if __name__ == "__main__":
    main()
