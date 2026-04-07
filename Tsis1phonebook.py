import psycopg2



def connect():
    return psycopg2.connect(
        host="localhost",
        database="phoneboook",
        user="artoryu",
        password="",
        port=5432
    );


def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Table ready!")



def insert_from_console():
    conn = connect()
    cur = conn.cursor()
    username = input("Enter name: ")
    phone = input("Enter phone: ")
    if username and phone:
        cur.execute(
            "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
            (username, phone)
        )
        conn.commit()
        print("Contact added!")
    else:
        print("Error: empty input")
    cur.close()
    conn.close()


def update_contact():
    conn = connect()
    cur = conn.cursor()
    username = input("Enter username to update: ")
    new_phone = input("Enter new phone: ")
    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE username = %s",
        (new_phone, username)
    )
    if cur.rowcount == 0:
        print("User not found")
    else:
        print("Updated successfully")
    conn.commit()
    cur.close()
    conn.close()


def query_contacts():
    conn = connect()
    cur = conn.cursor()
    print("1 - Show all")
    print("2 - Search by username")
    print("3 - Search by phone")
    choice = input("Choose: ")
    if choice == "1":
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
    elif choice == "2":
        username = input("Enter username: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE username ILIKE %s",
            ('%' + username + '%',)
        )
        rows = cur.fetchall()
    elif choice == "3":
        phone = input("Enter phone: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE phone = %s",
            (phone,)
        )
        rows = cur.fetchall()
    else:
        print("Invalid choice")
        rows = []
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def delete_contact():
    conn = connect()
    cur = conn.cursor()
    print("1 - Delete by username")
    print("2 - Delete by phone")
    choice = input("Choose option: ")
    if choice == "1":
        username = input("Enter username: ")
        cur.execute(
            "DELETE FROM phonebook WHERE username = %s",
            (username,)
        )
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute(
            "DELETE FROM phonebook WHERE phone = %s",
            (phone,)
        )
    else:
        print("Invalid choice")
    if cur.rowcount == 0:
        print("No such contact")
    else:
        print("Deleted successfully")
    conn.commit()
    cur.close()
    conn.close()


def main():
    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1 - Create table")
        print("2 - Import from CSV")
        print("3 - Add contact")
        print("4 - Update contact")
        print("5 - Query contacts")
        print("6 - Delete contact")
        print("0 - Exit")
        choice = input("Select: ")
        if choice == "1":
            create_table()
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            query_contacts()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
