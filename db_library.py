import mysql.connector as sql 
def get_connection():
    return sql.connect(user="root",host="localhost",passwd="",database="library_manager")

def create_database():
    c=sql.connect(user="root",host="localhost",passwd="")
    try:
        cu=c.cursor()
        cu.execute("create database if not exists library_manager")
        print("database created.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("database created error.",e)
    finally:
        c.close()
        cu.close()

def create_table():
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute("create table if not exists books(id int auto_increment primary key, title varchar(100), author varchar(50), year int)")
        cu.execute("create table if not exists members(id int auto_increment primary key, name varchar(50), phone varchar(100))")
        cu.execute("create table if not exists borrows(id int auto_increment primary key, book_id int, member_id int, borrow_date date, return_date date, foreign key (book_id) references books(id) on delete cascade, foreign key (member_id) references members(id) on delete cascade)")
        print("tables created.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("tables created error.",e)
    finally:
        c.close()
        cu.close()

