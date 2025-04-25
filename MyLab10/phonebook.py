import psycopg2 as psg
import csv


conn = psg.connect(host="localhost", dbname="phonebook", user="postgres", password="Yeralim008!!!", port=5432)

cur = conn.cursor()

# Create Table
cur.execute(""" CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            user_name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            phone VARCHAR(15) NOT NULL
);
""")

# Insert first name and phone number by terminal
def insert_data() :
    user_name=input()
    surname=input()
    phone=input()
    cur.execute("INSERT INTO phonebook (user_name,surname,phone) VALUES(%s,%s,%s)",
                (user_name,surname,phone))

#insert_data()

# Insert first name and phone by csv file
# with open('txt.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         cur.execute(
#             "INSERT INTO phonebook (user_name, surname, phone) VALUES (%s, %s, %s)",
#             (line[0], line[1] , line[2])
#         )


# Update Data
def update_name(old_name, new_name):
    cur.execute("UPDATE phonebook SET user_name=%s WHERE user_name = %s",(new_name,old_name))


# update_name('Yeralim','Bek')

def query_data(name=None,surname=None,phone=None):
    if name:
        cur.execute("SELECT * FROM phonebook WHERE user_name=%s",(name,))
    elif surname:
        cur.execute("SELECT * FROM phonebook WHERE surname=%s",(surname,))
    elif phone:
        cur.execute("SELECT * FROM phonebook WHERE phone=%s",(phone,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# query_data(surname='Adolf')

def deleting_data(name):
    cur.execute("DELETE FROM phonebook WHERE user_name=%s",(name,))

deleting_data('Asyl')


conn.commit()

cur.close()
conn.close()
