### 클래스의 구성 ###

# 사람
# : 이름, 나이, 연락처, 주소, ...
# : 잔다, 먹는다, 공부한다, 걷는다, ...

# 1. 클래스 구성: 변수 & 함수
# 변수 - 값(상태)
# 함수 - 기능(동작)

# 클래스를 구성하는 변수
# : 클래스 변수 & 인스턴스 변수

# 클래스를 구성하는 함수 - 메서드(method)
# : 클래스 메서드, 정적 메서드, 인스턴스 메서드

# 2. 인스턴스 변수 & 인스턴스 메서드

# 2-1. 인스턴스 변수
# : 클래스를 기반으로 만들어지는 모든 인스터스(객체)들이 각각 따로 저장하는 변수
# : 클래스 내에 정의되지만 각 클래스 인스턴스(객체)에서 개별적으로 다루는 변수
# : 각 객체의 상태 저장
# : self.variable_name

# 2-2. 인스턴스 메서드
# : 클래스 내에 정의된 함수, 클래스의 객체가 수행할 수 있는 동작을 나타냄
# : 인스턴스 변수를 사용하는 메서드
# : 첫 번째 인자로 'self'를 받아야 한다.
# self: 메서드를 호출하는 객체 자신을 참조

class Person:
    # 첫 번째 매개변수가 self - 인스턴스 메서드
    def who_am_i(self, name, age, tel, address):
        # self.name은 인스턴스 변수 name을 의미
        # 우항의 name은 매개변수 name
        # who_am_i() 메서드를 호출할 때 전달된 name이 인스턴스 name이 된다.
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

sundong = Person()
sundong.who_am_i("순동", 22, "01028076732", "전포동")
print(sundong.address, sundong.age, sundong.name, sundong.tel)

