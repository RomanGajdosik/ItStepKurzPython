from db import get_connection

def add_book(title, author, genreid):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT author_id FROM authors WHERE name = %s", ("author",))
            searchedAuthor = cursor.fetchone()
            if not searchedAuthor:
                print(f"Author '{author}' not found in the database.Create a new author entry.")
                authorNew = input("Enter the author's name: ")
                bio = input("Enter the author's bio: ")
                cursor.execute("INSERT INTO authors (name,bio) VALUES (%s,%s)", (authorNew,bio))
                conn.commit()
                print(f"Author '{authorNew}' added to the database.")
                
            
            cursor.execute("SELECT * FROM genres")
            genres = cursor.fetchall()
            print("Available genres:")
            for genre in genres:
                print(f"ID: {genre[0]}, Name: {genre[1]}")
            genreid = input(f"Enter the genre ID: ")    
            
            cursor.execute("SELECT author_id FROM authors WHERE name = %s", (authorNew,))
            searchedAuthorId = cursor.fetchone()[0]
            cursor.execute("INSERT INTO books (title, author_id, genre_id) VALUES (%s, %s, %s)", (title, searchedAuthorId, genreid))
                       
            conn.commit()
            print(f"Book '{title}' added to the database.") 
# Search for book by title or author or genre
def search_book(title=None, author=None, genre=None):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT books.title, authors.name, genres.name 
                FROM books 
                INNER JOIN authors ON books.author_id = authors.author_id 
                INNER JOIN genres ON books.genre_id = genres.genre_id 
                WHERE books.title ILIKE %s OR authors.name ILIKE %s OR genres.name ILIKE %s
            """, (f"%{title}%", f"%{author}%", f"%{genre}%"))
            
            results = cursor.fetchall()
            
            if results:
                print("Search results:")
                for row in results:
                    print(f"Title: {row[0]}, Author: {row[1]}, Genre: {row[2]}")
            else:
                print("No results found.")