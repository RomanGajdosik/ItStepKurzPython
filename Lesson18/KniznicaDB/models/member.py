from db import get_connection

def register_member(first_name,last_name, email):
    """
    Registers a new member in the database.
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO members (first_name,last_name, email) VALUES (%s, %s,%s)", (first_name,last_name, email))
            conn.commit()
            print(f"Member '{first_name,last_name}' registered successfully.")
def get_member_loan(member_id):
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