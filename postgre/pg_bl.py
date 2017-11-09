"""
    @brief Postgre business logic
    @author Py.Brightside
"""
import psycopg2

def main():
    try:
        print("123")

        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password=''")

        cur = conn.cursor()
        cur.execute("""SELECT datname from pg_database""")

        rows = cur.fetchall()
        for row in rows:
            print( "   ", row[0] )

        print("234")

    except:
        print("I am unable to connect to the database")


if __name__ == "__main__":
	main()
