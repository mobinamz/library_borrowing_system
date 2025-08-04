from db_library import create_database, create_table
from crud_library import add_member, search_member, update_member, delete_member, add_book, search_book, show_books, delete_book, add_borrow, show_borrows, update_borrow, delete_return_borrow
def main():
    print("Dear user, welcome...")
    while True:
        user=int(input("create_database=1 or create_table=2 or add member=3 or search member=4 or update member=5 or delete member=6 or add book=7 or search book=8 or show books=9 or delete book=10 or add borrow=11 or show borrows=12 or update borrow=13 or delete return borrow=14 or exit=0:"))
        if user==0:
            print("you went out.")
            break
        if user==1:
            create_database()
        elif user==2:
            create_table()
        elif user==3:
            name=input("enter your name:")
            phone=input("enter your phone number:")
            add_member(name, phone)
        elif user==4:
            idd=int(input("enter the desired id:"))
            search_member(idd)
        elif user==5:
            idd=int(input("enter the desired id:"))
            name=input("enter your new name or blank:")
            if name=="":
                name=None
            phone=input("enter your new phone number or blank:")
            if phone=="":
                phone=None
            update_member(idd, name, phone)
        elif user==6:
            idd=int(input("enter the desired id:"))
            delete_member(idd)
        elif user==7:
            title=input("enter the book title:")
            author=input("enter the name of the book's author:")
            year=int(input("enter the year the book was published:"))
            add_book(title, author, year)
        elif user==8:
            idd=int(input("enter the id of the desired book:"))
            search_book(idd)
        elif user==9:
            show_books()
        elif user==10:
            idd=int(input("enter the id of the desired book:"))
            delete_book(idd)
        elif user==11:
            member_id=int(input("enter the desired member id:"))
            book_id=int(input("enter the id of the desired book:"))
            add_borrow(member_id, book_id)
        elif user==12:
            show_borrows()
        elif user==13:
            member_id=int(input("enter the desired member id:"))
            book_id=int(input("enter the id of the desired book:"))
            update_borrow(member_id, book_id)
        elif user==14:
            member_id=int(input("enter the desired member id:"))
            book_id=int(input("enter the id of the desired book:"))
            delete_return_borrow(member_id, book_id)
if __name__=="__main__":
    main()

            


