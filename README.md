# Python-Design_pattern

## 실습환경
- Language : Python 3.6
- Tool : Visual-Studio-Code

## 객체지향 프로그래밍의 주요기능
- 캡슐화
  > 객체의 기능과 상태 정보를 외부로부터 은닉한다.
  > 클라이언트는 객체의 내부 구조 및 상태를 직접 수정할 수 없고 수정 요청을 한다.(get, set 같은 함수를 사용해 내부 상태를 변경)
  > 함수나 변수 앞에 __를 붙여 접근 제어

- 다형성
  > 객체는 함수 인자에 따라 다른 기능을 한다.
  > 동일한 인터페이스를 여러 형식의 객체들이 공유한다.

- 상속
  > 클래스의 기능이 부모 클래스로부터 파생되는 것
  > 부모 클래스에서 정의된 함수를 재사용할 수 있고 application의 기본 기능을 확장
  > 다중 상속 지원

- 추상화
  > 클라이언트가 클래스 객체를 생성하고 인터페이스에 정의된 함수를 호출할 수 있는 인터페이스를 제공
  > 클라이언트는 클래스의 복잡한 내부 구현에 대한 이해없지 간편하게 인터페이스를 사용

- 컴포지션
  > 객체나 클래스를 더 복잡한 자료 구조나 모듈로 묶는 행위
  > 특정 객체는 다른 모듈의 함수를 호출 할 수 있다. 즉 상속 없이 외부 기능 사용이 가능
  
## 객체지향 디자인의 기본 원칙
- 개방-폐쇄 원칙
  > 클래스와 객체, 메소드 모드 확장엔 개방적이고 수정엔 폐쇄적이어야 한다는 원칙
  > 기본 클래스는 건드리지 않고 클래스를 확장해 새로운 기능을 추가 구현할 수 있는 구조

  - 장점
    > 기본 클래스를 수정하지 않기 때문에 실수가 줄어듬
    > 기존 코드의 호환성을 보장

- 제어 반전 원칙
  > 상위 모듈은 하위 모듈에 의존적이지 않아야 한다는 원칙
  > 클래스의 세부 내용을 추상화 한다. 반대로 추상화가 세부 사항에 의존하는 구조는 피해야 한다.

  - 장점
    > 모듈 간의 낮은 상호 의존도는 시스템 복잡도를 줄인다.
    > 관련 모듈을 연결하는 추상화 계층 덕분에 모듈 간 상호 관계를 쉽게 관리할 수 있다.

- 인터페이스 분리 원칙
  > 클라이언트는 불필요한 인터페이스에 의족하지 않아야 한다는 원칙
  > 해당 기능과 관련 있는 메소드만을 작성해야 한다. (ex Pizza 인터페이스에는 add_chicken()과 같은 메소드가 있으면 안된다.)

  - 장점
    > 인터페이스에 특화된 메소드만 있는 가벼운 인터페이스를 작성하게 된다.
    > 의도하지 않은 메소드로 인터페이스가 채워지지 않도록 한다.

- 단일 책임 원칠
  > 클래스는 하나의 책임만을 가져야 한다.
  > 클래스를 구현할 때 한가지 기능에만 중점을 둬야 한다.(두가지 이상의 기능이 필요하다면 클래스를 나눠라~~)
  
  - 장점
    > 특정 기능을 수정할 때 관련 클래스 외에는 건드릴 필요가 없다.
    > 한개의 클래스에 여러가지 기능이 있다면 관련된 모든 클래스를 수정해야 하는 상황이 발생될 수 있다.

- 치환 원칙
  > 상속받는 클래스는 기본 클래스의 역할을 완전히 치환할 수 있어야 한다는 원칙
  > 파생된 클래스는 기본 클래스를 완전히 확정해야 한다.
  > 코드 수정 또는 추가 없이도 파생된 클래스는 기본 클래스를 대체할 수 있어야 한다.

## 디자인 패턴 종류
- 생성 패턴
  > 객체가 생성되는 방식을 중시
  > 객체 생성 관련 상세 로직을 숨긴다.
  > 코드는 생성하려는 객체형과는 독립적
  + Sigleton, Factory 패턴

- 구조 패턴
  > 클래스와 객체를 병합해 더 큰 결과물로 합칠 수 있는 구조
  > 클래스 상속과 컴포지션을 중시
  + Facade 패턴, Proxy 패턴, Adapter 패턴

- 행위 패턴
  > 객체 간의 상호작용과 책임을 중시
  > 객체는 상호작용하지만 느슨하게 결합돼야 한다.
  + Observer 패턴

- Builder 패턴
- Prototype 패턴

## Singleton
- 클래스에 대한 객체가 단 하나만 생성되게 하는 설계 패턴
- 게으른 초기화(Lazy instantiation): 인스턴스가 꼭 필요한 시점에 생성하는 방식
- 모노스테이트 싱글톤: 모든 객체가 같은 상태를 공유하는 패턴
- 메타클래스: 클래스의 클래스 즉 클래스는 자신의 메타클래스의 인스턴스다.
- ex): 로깅, 쓰레드 풀, 캐시, 레지스트리 설정, 데이터베이스를 연결/제어하는 인터페이스 객체 등
  - 목적
    > 클래스에 대한 단일 객체 생성
    > 전역 객체 제공
    > 공유된 리소스에 대한 동시 접근 제어

## Factory
- 객체지향 프로그래밍에서 Factory는 다른 클래스의 객체를 생성하는 클래스를 말함
- 클라이언트는 특정 인자와 함께 메소드를 호출하고 / Factory는 해당 객체를 생성하고 반환한다.
- 객체를 생성하는 팩토리 클래스를 정의하고 어떤 객체를 만들지는 팩토리 객체에서 결정하여 객체를 만들도록 하는 설계 패턴
  - 목적
    > 객체 생성과 클래스 구현을 나눠 상호 의존도를 줄인다.
    > 클라이언트는 생성하려는 객체 클래스 구현과 상관없이 사용 가능
    > 코드를 수정하지 않고 간단하게 팩토리에 새로운 클래스를 추가할 수 있다.
    > 이미 생성된 객체를 팩토리가 재활용할 수 있다.

- 세부적으로 두가지 패턴이 존재
  1. factory method: input에 따라 객체 생성이 달라지는 방식 (상속을 통해 객체 생성)
  2. abstract factory: 여러 객체 생성을 연관된 group별로 묶어서 객체를 생성하는 방식

- ex): 모바일 플랫폼별 스마트폰 객체 생성

- factory method: 인스턴스 생성을 서브 클래스에게 위임한다.
- abstract factory: 클래스를 직접 호출 하지 않고 관련된 객체를 생성하는 인터페이스를 제공 -> 관련된 객체의 집합을 생성한다.
-> 클라이언트는 오직 인터페이스를 통해 객체에 접근 할 수 있다.

## Facade
- 복잡한 내부 시스템 로직을 감추고 클라이언트가 쉽게 시스템에 접근할 수 있는 인터페이스를 제공
-> 단일 인터페이스 객체로 복잡한 서브시스템을 대체한다.
-> 클라이언트와 내부 구현을 분리

  - 최소지식원칙
    > 클래스 간의 의존도를 낮추는 방식으로 설계

## Adapter
- 클라이언트의 요구에 따라 특정 인터페이스를 다른 인터페이스에 맞춘다. 서로 다른 클래스의 인터페이스를
목적에 맞춰 변환한다.

## Observer
- 객체의 상태 변경 시, 관련된 다른 객체들에게 상태 변경을 notify하는 설계 패턴
- 관찰자(관련된 다른 객체)들에게 변경된 객체의 특정 이벤트 발생을 자동으로 모두 전달하는 패턴
- ex): SMS, Email Push

## Builder
- 여러가지 step을 걸쳐서 객체를 생성해야할 경우
- 생성자에 들어갈 매개 변수가 복잡하여 가독성이 떨어지고, 어떤 변수가 어떤 값인지 알기 어렵고, 전체 변수 중 일부 값만 설정하는 경우 

## Prototype
- 클래스로 객체를 새로 생성하는 것이 아니라 기존 객체를 복사해와서 새로운 객체를 생성해내는 패턴