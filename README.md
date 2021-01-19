# Python-Design_pattern

## 실습환경
- Language : Python 3.6
- Tool : Visual-Studio-Code

## 디자인 패턴 종류
- Sigleton 패턴
- Observer 패턴
- Builder 패턴
- Factory 패턴
- Prototype 패턴
- Facade 패턴

## Singleton
- 클래스에 대한 객체가 단 하나만 생성되게 하는 설계 패턴
- ex): 데이터베이스를 연결/제어하는 인터페이스 객체

## Observer
- 객체의 상태 변경 시, 관련된 다른 객체들에게 상태 변경을 notify하는 설계 패턴
- 관찰자(관련된 다른 객체)들에게 변경된 객체의 특정 이벤트 발생을 자동으로 모두 전달하는 패턴
- ex): SMS, Email Push

## Builder
- 여러가지 step을 걸쳐서 객체를 생성해야할 경우
- 생성자에 들어갈 매개 변수가 복잡하여 가독성이 떨어지고, 어떤 변수가 어떤 값인지 알기 어렵고, 전체 변수 중 일부 값만 설정하는 경우 

## Factory
- 객체를 생성하는 팩토리 클래스를 정의하고 어떤 객체를 만들지는 팩토리 객체에서 결정하여 객체를 만들도록 하는 설계 패턴
- 세부적으로 두가지 패턴이 존재
  1. factory method: input에 따라 객체 생성이 달라지는 방식
  2. abstract factory: 여러 객체 생성을 연관된 group별로 묶어서 객체를 생성하는 방식
- ex): 모바일 플랫폼별 스마트폰 객체 생성

## Prototype
- 클래스로 객체를 새로 생성하는 것이 아니라 기존 객체를 복사해와서 새로운 객체를 생성해내는 패턴

## Facade
- 복잡한 classes들과 instructions들을 하나의 function을 통해 실행 가능토록 하는 설계 패턴