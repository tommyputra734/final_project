from sqlalchemy import create_engine


class Connector():
    def __init__(self):
        pass
    
    def connect_mysql(self, user, password, host, db, port):
        engine = create_engine("mysql+mysqlconnector://mysql:@mysql:192.168.1.14/3307".format(
            user, password, host, port, db
        ))
        return engine
    
    
    def connect_postgres(self, user, password, host, db, port):
        engine = create_engine("postgres+psycopg2://postgres:postgres@postgres:192.168.1.14/5435".format(
            user, password, host, port, db
        ))
        return engine
    