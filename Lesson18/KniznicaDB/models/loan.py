from db import get_connection

def borrow_book(member_id, book_id):
    """
    Borrows a book for a member.
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT available FROM books WHERE book_id = %s", (book_id,))
            available = cursor.fetchone()
            if not available or not available[0]:
                print(f"Book ID {book_id} is not available for borrowing.")
                return
            
            # Borrow the book
            cursor.execute("INSERT INTO loans (member_id, book_id) VALUES (%s, %s)", (member_id, book_id))
            
            # Mark the book as unavailable
            cursor.execute("UPDATE books SET available = FALSE WHERE book_id = %s", (book_id,))
def get_loan_history(member_id):
    """
    Retrieves the loan history of a member.
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM loans WHERE member_id = %s", (member_id,))
            loans = cursor.fetchall()
            
            if loans:
                print(f"Loan history for member ID {member_id}:")
                for loan in loans:
                    print(loan)
            else:
                print(f"No loan history found for member ID {member_id}.")

get_loan_history(1)