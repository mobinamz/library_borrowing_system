from db_library import get_connection
import datetime as dt 
def add_member(name,phone):
    c=get_connection()
    try:
        cu=c.cursor()
        query="insert into members(name,phone)values(%s,%s)"
        values=(name,phone)
        cu.execute(query,values)
        print(f"member added with id {cu.lastrowid}.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("member added error.",e)
    finally:
        c.close()
        cu.close()

def search_member(idd):
    c=get_connection()
    cu=c.cursor()
    cu.execute("select * from members where id=%s",(idd,))
    for i in cu:
        print(f"The desired member: {i}")
    c.close()
    cu.close()

def update_member(idd,name,phone):
    c=get_connection()
    try:
        cu=c.cursor()
        field=[]
        value=[]
        if name:
            field.append("name=%s")
            value.append(name)
        if phone:
            field.append("phone=%s")
            value.append(phone)
        if not field:
            print("nothing to update.")
            return
        value.append(idd)
        query=f"update members set {','.join(field)} where id=%s"
        cu.execute(query,tuple(value))
        print(f"member updated with id {idd}.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("member updated error.",e)
    finally:
        c.close()
        cu.close()

def delete_member(idd):
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute("delete from members where id=%s",(idd,))
        print(f"member deleted with id {idd}.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("member deleted error.",e)
    finally:
        c.close()
        cu.close()

def add_book(title,author,year):
    c=get_connection()
    try:
        cu=c.cursor()
        query="insert into books(title,author,year)values(%s,%s,%s)"
        values=(title,author,year)
        cu.execute(query,values)
        print(f"book added with id {cu.lastrowid}.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("book added error.",e)
    finally:
        c.close()
        cu.close()

def show_books():
    c=get_connection()
    cu=c.cursor()
    cu.execute("select * from books")
    for i in cu:
        print(i)
    c.close()
    cu.close()

def search_book(idd):
    c=get_connection()
    cu=c.cursor()
    cu.execute("select * from books where id=%s",(idd,))
    for i in cu:
        print(f"The desired book: {i}")
    c.close()
    cu.close()

def delete_book(idd):
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute("delete from books where id=%s",(idd,))
        print(f"book deleted with id {idd}.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("book deleted error.",e)
    finally:
        c.close()
        cu.close()

def add_borrow(member_id,book_id):
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute("select * from members where id=%s",(member_id,))
        result=cu.fetchone()
        if not result:
            print("member not found.")
            return
        else:
            print(f"member with id {member_id} exists.")
        cu.execute("select * from books where id=%s",(book_id,))
        if not result:
            print("book not found.")
            return
        else:
            print(f"book with id {book_id} exists.")
        query="insert into borrows(member_id,book_id,borrow_date,return_date)values(%s,%s,%s,%s)"
        borrow_date=dt.date.today()
        return_date=None
        values=(member_id,book_id,borrow_date,return_date)
        cu.execute(query,values)
        print(f"borrow record added with id {cu.lastrowid}.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("borrow record added error.",e)
    finally:
        c.close()
        cu.close()

def show_borrows():
    c=get_connection()
    cu=c.cursor()
    query="select borrows.id, members.name, books.title, borrows.borrow_date, borrows.return_date from borrows join members on borrows.member_id=members.id join books on borrows.book_id=books.id"
    cu.execute(query)
    rows=cu.fetchall()
    for row in rows:
        if row[4]:
            return_str = row[4]
        else:
            return_str = "not Returned"
        print(f"borrow id:{row[0]} member:{row[1]} book:{row[2]} borrow date:{row[3]} return date:{row[4]}")

def update_borrow(member_id,book_id):
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute("update borrows set return_date=curdate() where member_id=%s and book_id=%s and return_date is null",(member_id,book_id,))
        if cu.rowcount>0:
            print(f"borrow record updated with member_id{member_id} and book_id{book_id}.")
        else:
            print("nothing to update.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("borrow record updated error.",e)
    finally:
        c.close()
        cu.close()

def delete_return_borrow(member_id,book_id):
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute("delete from borrows where member_id=%s and book_id=%s and return_date is not null",(member_id,book_id))
        if cu.rowcount>0:
            print(f"borrow record deleted with member_id {member_id} and book_id {book_id}.")
        else:
            print("no returned borrow found to delete.")
        c.commit()
    except Exception as e:
        c.rollback()
        print("borrow record deleted error.",e)
    finally:
        c.close()
        cu.close()