### 생성자 & 소멸자 예제 ###

class Service:
    def __init__(self, service):
        self.service = service
        print('{} 서비스가 시작되었습니다.'.format(self.service))

    # def __del__(self):
    #     print('{} 서비스가 종료되었습니다.'.format(self.service))

    def remove_from_game(self):
        print(f'{self.service} 서비스가 종료되었습니다.')

service = Service('공급')
del service

# 파이썬 소멸자 사용 시 주의사항
# : 소멸자(__del__)는 객체가 메모리에서 제거될 때 호출
# : 소멸자의 삭제 시점을 프로그래머가 명확하게 지정할 수 없음
# : 파이썬의 가비지 컬렉션이 언제 동작할지 불분명.