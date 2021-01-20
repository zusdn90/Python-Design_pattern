class Singleton(object):
    
    # python 전용 특수 생성자
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    

if __name__ == '__main__':
    s = Singleton()
    print("Object created", s)
    
    s1 = Singleton()
    print("Object created", s1)