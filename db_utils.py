
import gevent.hub
import MySQLdb


class DBUtils:
    def __init__(self):
        cnx = {'host': 'author.ckl4ngjgdh4k.ap-southeast-2.rds.amazonaws.com',
               'username': 'Du_M_',
               'password': 'ThisIsThe1Story#',
               'dbname': 'author',
               'port': 3306}
        try:
            conn = MySQLdb.connect(cnx['host'], user=cnx['username'], passwd=cnx['password'], database=cnx['dbname'])
            cur = conn.cursor()

            cur.execute("SELECT username, password FROM users")
            myresult = cur.fetchall()
            self.users = []
            for x in myresult:
                type(x)
                # print(x[0], x[1])
                self.users.append({'username': x[0],
                                   'password': x[1]}
                                  )
        except Exception as e:
            print(e)
            self.users = None

    def check_users(self, username, password):
        if self.users is None:
             return -1
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return 1
        return 0


if __name__ == '__main__':
    db = DBUtils()
