#import pymssql
import pymysql
import configparser

class Dbconnect():
    """
    This class is used to connect to databases and run queries.
    """
    def __init__(self):
        pass

    def dbfile(self):
        d = {}
        database_file = open("E:\\robotframework\pwms\\token.txt", "r")
        for line in database_file:
            key, value = line.split("=")
            d[str(key)] = value
            print type(d)
            print(d)
            list = d.items()
            print type(list)
            print (list)
            keys = d.keys()
            print keys
            values = d.values()
            print values
            list_keys = [k for k in d]
            print list_keys
            list_values = [v for v in d.values()]
            print list_values
            list_key_value = [[k,v] for k, v in d.items()]
            print list_key_value

        #return d
        #database_file.close()
        #print(database_file.read())

    def __connect(self,db):
        """
        This method stablishe's a connection with the passed in database and returns the connection.
        The host and user information are hardcoded here.
        :param db: the database name to connect to
        :return: the connection object
        """
        # connect to the db at the specified host
        config = configparser.ConfigParser()
        config.read("E:\\robotframework\pwms\\dbconnect.ini")
        host = config.get('SectionOne', 'host')
        port = config.get('SectionOne', 'port')
        user = config.get('SectionOne', 'user')
        password = config.get('SectionOne', 'password')
        db = config.get('SectionOne', 'db')
        #conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
        conn = pymysql.connect(host=host, port=3306, user=user, password=password, db=db, charset='utf8')

        return conn

    def select(self, db, query):
        """
        This method is use to connect to a database and run a 'SELECT' statement.
        :param db: the database name to connect to
        :param query: the query to run
        :return: the result of the query (a list of lists)
        """

        # make the connection and execute the query
        conn = self.__connect(db)
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()

        # store the result in a list of lists. Each row is a list.
        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col))
            all_rows.append(row)

        conn.close() #closing the db connection
        cur.close() #clearing the cursor

        return all_rows


    def update(self, db, query):
        """
        This method is use to connect to a database and run a 'DELETE', 'UPDATE', 'INSERT' statements.
        :param db: the database name to connect to
        :param query: the query to run
        :return: result ( the number of rows affected)
        """

        # create connection
        conn = self.__connect(db)
        cur = conn.cursor()

        # execute the query
        result = cur.execute(query)
        conn.commit()

        conn.close()
        cur.close()

        return  result


#test = Dbconnect()
#test.dbfile()


