import psycopg2

class PostgreSQL:
    def __init__(self, hostname, db, username, password):
        self.connection = psycopg2.connect(
                            host=hostname,
                            database=db, 
                            user=username, 
                            password=password,
                            port="5432" # default PostgreSQL port is 5432
                          )
        self.cursor = self.connection.cursor()

    def write_data(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Data written successfully")
        except Exception as e:
            print(f"Error occurred while writing to database: {e}")
          
    def read_data(self, query):
        try:
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(f"Error occurred while retrieving data: {e}")
