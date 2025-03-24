from databricks import sql
import os

SERVER_HOSTNAME = os.getenv('SERVER_HOSTNAME')
HTTP_PATH = os.getenv('HTTP_PATH')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

class Connection():
    def make_query(self, query):
        connection = sql.connect(
            server_hostname=self.SERVER_HOSTNAME, 
            http_path=self.HTTP_PATH, 
            access_token=self.ACCESS_TOKEN
        )

        cursor = connection.cursor()
        cursor.execute(query)

        df = cursor.fetchall_arrow()

        cursor.close()
        connection.close()

        return df