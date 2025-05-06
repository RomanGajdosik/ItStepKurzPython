from models import book, loan, member

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Books")
        print("3. Register Member")
        print("4. Borrow Book")
        print("5. View Loan History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genreid = input("Enter genre id: ")
            book.add_book(title, author, genreid)
        elif choice == '2':
            title = input("Enter book title (or leave blank): ")
            author = input("Enter book authorId (or leave blank): ")
            genre = input("Enter book genreId (or leave blank): ")
            book.search_book(title, author, genre)
        elif choice == '3':
            first_name = input("Enter member First name: ")
            last_name = input("Enter member Last name: ")
            email = input("Enter member email: ")
            member.register_member(first_name,last_name, email)
        elif choice == '4':
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            loan.borrow_book(member_id, book_id)
        elif choice == '5':
            member_id = int(input("Enter member ID: "))
            loan.get_loan_history(member_id)
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()