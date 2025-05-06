import psycopg2

def get_connection():
    """
    Establishes a connection to the PostgreSQL database and returns the connection object.
    """
    try:
        conn = psycopg2.connect(
            database="byncjuw7s8tagen1muul",
            user="udmw0ybt4tlrfip6qvod",
            password="iBSHgCbIOtxBAixxJoeNQAMXflngee",
            host="byncjuw7s8tagen1muul-postgresql.services.clever-cloud.com",
            port="50013"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise