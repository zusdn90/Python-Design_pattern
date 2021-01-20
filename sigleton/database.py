import sqlite3

class MetaSingleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]            
    

class Database(metaclass=MetaSingleton):
    connection = None
    
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj
    
if __name__ == '__main__':
    # 단 한개의 database 클래스 객체만 생성한다.
    # 데이터베이스의 동기화가 보장된다.
    # 리소스를 적게 사용해 메모리와 CPU 사용량을 최적화 할 수 있다.
    db1 = Database().connect()
    db2 = Database().connect()
    
    print("Database Objects DB1", db1)    
    print("Database Objects DB2", db2)    