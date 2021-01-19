# 1. Singleton 클래스 만들기
class Singleton(type):                       # Type을 상속받음
    __instances = {}                         # 클래스의 인스턴스를 저장할 속성
    def __call__(cls, *args, **kwargs):      # 클래스로 인스턴스를 만들 때 호출되는 python 내장 메서드
        if cls not in cls.__instances:        # 클래스로 인스턴스를 생성하지 않았는지 확인
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

# 2. Singleton 클래스 상속
class PrintObject(metaclass=Singleton):
    def __init__(self):
        print("called by super().__call__")

if __name__ == '__main__':

    obj1 = PrintObject()
    obj2 = PrintObject()
    obj3 = PrintObject()
    
    print(obj1)
    print(obj2)
    print(obj3)