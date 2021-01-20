class Singleton:
    __instance = None
    
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.getInstance())            
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
    
    if __name__ == '__main__':
        
        s = Singleton()                                     # 클래스를 초기화했지만 객체는 생성하지 않음
        print("Object created", Singleton.getInstance())    # 객체생성
        s1 = Singleton()                                    # 객체는 이미 생성되었음
                