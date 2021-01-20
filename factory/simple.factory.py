
# 심플 팩토리 패턴: 인터페이스는 객체 생성 로직을 숨기고 객체를 생성한다.
from abc import ABCMeta, abstractmethod

# ABCMeta는 파이썬에서 특정 클래스를 Abstract로 선헌하는 특수 메타클래스
class Animal(metaclass = ABCMeta):    
    @abstractmethod
    def do_say(self):
        pass
    
class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")
        
class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")

## forest factory 정의
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

## 클라이언트 코드
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    print(animal)
    ff.make_sound(animal)