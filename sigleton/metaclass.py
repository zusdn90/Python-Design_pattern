class MetaSingleton(type):
    _instances = {}
    
    # __call_ - 이미 존재하는 클래스의 객체를 생성할 때 호출되는 파이썬의 특수 메소드
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]            
    
class Logger(metaclass=MetaSingleton):
    pass

if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()
    
    print(logger1, logger2)

    


              