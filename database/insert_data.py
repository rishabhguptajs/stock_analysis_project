import psycopg2
import pandas as pd
import connection_string

CONNECTION_STRING = connection_string

def connect_db():
    try:
        conn = psycopg2.connect(CONNECTION_STRING)
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error: Could not connect to the database: {e}")
        return None

def insert_data(data):
    conn = connect_db()
    if conn is None:
        print("Aborting data insertion due to connection failure.")
        return

    cursor = conn.cursor()

    for index, row in data.iterrows():
        cursor.execute(
            """
            INSERT INTO stock_data (instrument, date, open_price, high, low, close_price, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (row['instrument'], row['datetime'], row['open'], row['high'], row['low'], row['close'], row['volume'])
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted successfully")


if __name__ == '__main__':
    data = pd.read_csv('data/stock_data.csv', parse_dates=['datetime'])
    insert_data(data)
