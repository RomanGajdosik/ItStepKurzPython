import psycopg2

try:
    conn =psycopg2.connect(
        database="byncjuw7s8tagen1muul",
        user="udmw0ybt4tlrfip6qvod",
        password="iBSHgCbIOtxBAixxJoeNQAMXflngee",
        host="byncjuw7s8tagen1muul-postgresql.services.clever-cloud.com",
        port="50013"
    )
    
    cursor = conn.cursor()
    new= 'Ja2'
    # cursor.execute("SELECT author_id FROM authors ORDER BY author_id DESC")
    # cursor.execute("SELECT author_id FROM authors WHERE name =%s", (new,))
    cursor.execute( "SELECT b.title, a.name AS author, g.name AS genre FROM books b
                JOIN authors a ON b.author_id = a.author_id
                JOIN genres g ON b.genre_id = g.genre_id
                WHERE b.title ILIKE %s
                   OR a.name ILIKE %s
                   OR g.name ILIKE %s")
    lastAuthorId = cursor.fetchone()
    print (lastAuthorId)
    #ursor.execute('DELETE FROM authors WHERE author_id = %s', (lastAuthorId,))
    
    #conn.commit()
    # data = [
    #     ("Patrik", "Test bio 1"),
    #     ("Milan", "Test bio 2"),
    #     ("Peter", "Test bio 3"),
    # ]

    # cursor.executemany("INSERT INTO authors(name, bio) VALUES (%s, %s)", data)

    # cursor.execute("SELECT author_id FROM authors WHERE name = %s", ("Patrik",))
    # patrikAuthor = cursor.fetchone()[0]

    # cursor.execute("SELECT author_id FROM authors WHERE name = %s", ("Milan",))
    # milanAuthor = cursor.fetchone()[0]

    # cursor.execute("SELECT author_id FROM authors WHERE name = %s", ("Peter",))
    # peterAuthor = cursor.fetchone()[0]

    # cursor.execute("SELECT genre_id from genres where name = 'Fantasy'")
    # fantasyGenreId = cursor.fetchone()[0]

    # dataKnihy = [
    #     ("Patrikova knizka", patrikAuthor, fantasyGenreId, "123456789", 2021, 1),
    #     ("Milanova knizka", milanAuthor, fantasyGenreId, "12322222", 2023, 1),
    #     ("Petova knizka", peterAuthor, fantasyGenreId, "123123123123", 2024, 5),
    # ]

    # cursor.executemany("""
    # INSERT INTO books(title, author_id, genre_id, isbn, publication_year, copies) 
    # VALUES(%s, %s, %s, %s, %s, %s)""", dataKnihy)

    # conn.commit()
    # cursor.close()
    # conn.close()
    
    # first_name = 'Roman'
    # last_name = 'Gajdosik'
    # email = 'moj@email.com'
    # cursor = conn.cursor()
    
    # cursor.execute("""
    #                INSERT INTO members (first_name, last_name, email) 
    #                VALUES (%s, %s, %s)
    #                """, (first_name, last_name, email))
    # conn.commit()
    # print('Member added successfully') 

    
    # cursor.execute("SELECT title FROM loans INNER JOIN books ON loans.book_id = books.book_id WHERE loans.loan_date > %s AND loans.loan_date <%s", ('2022-01-01','2022-02-21',))
    # autor = cursor.fetchall()
    # print(autor)
    
    # cursor.execute("SELECT * FROM books INNER JOIN genres ON genres.genre_id = books.genre_id WHERE genres.name = %s", ('Fantasy',))
    # autor = cursor.fetchall()    
    # print(autor)
    
    # cursor.execute("SELECT * FROM books WHERE publication_year > %s AND publication_year < %s", (1900, 1950))
    # autor = cursor.fetchall()
    
    # print(autor)
    
    
    cursor.close()
    conn.close()
finally:
    print('Disconected from the database')