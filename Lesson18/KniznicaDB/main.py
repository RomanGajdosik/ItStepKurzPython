import psycopg2
from autor import Autor

try:
    conn =psycopg2.connect(
        database="byncjuw7s8tagen1muul",
        user="udmw0ybt4tlrfip6qvod",
        password="iBSHgCbIOtxBAixxJoeNQAMXflngee",
        host="byncjuw7s8tagen1muul-postgresql.services.clever-cloud.com",
        port="50013"
    )
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM authors WHERE author_id = 1")
    autorn1 = cursor.fetchall()
    autor = Autor(autorn1[0][0], autorn1[0][1], autorn1[0][2])
    
    print(autorn1)
    print(autor)
    
    # cursor.execute("SELECT * FROM authors")
    # autor = cursor.fetchone()
    # print(autor)
    
    cursor.close()
    conn.close()
finally:
    print('Connected to the database')