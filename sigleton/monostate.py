class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass
    
if __name__ == '__main__':
    b = Borg()
    b1 = Borg()
    b.x = 4
    
    print("Bord Object 'b': ", b)           # b와 b1은 다른 객체다.
    print("Bord Object 'b1': ", b1)         # b와 b1은 다른 객체다.
    print("Object State 'b' ", b.__dict__)  # b와 b1은 상태를 공유한다.
    print("Object State 'b1' ", b1.__dict__)  # b와 b1은 상태를 공유한다.
    
    
        