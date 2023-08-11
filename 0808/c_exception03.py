# 파이썬 예외 처리 방식 #

#! 1. 모든 예외를 처리하는 방식
# : 모든 예외를 처리하면 예상치 못한 오류가 발생할 때도 프로그램이 계속 될 수 있다.
# : 가능한 특정 예외를 지정하여 처리하는 것을 권장
# try - except 문을 사용하여 예외 처리

#* 예외 처리 기본 형태
# trY:
#    코드 작성 영역
# except:
#    예외 발생 시 처리 영역

try:
    a = int(input('정수를 입력하세요 : '))
    b = int(input('정수를 입력하세요 : '))
    print('{} / {} = {}'.format(a, b, a / b))
except:
    print('예외가 발생했습니다.')

#! 2. 특정 예외만 처리하는 방식

# 1. 0으로 나누려고 하는 경우 - 0으로 나눌 수 없습니다.
# 2. 정수가 아닌 값을 입력하는 경우 - 정수만 입력할 수 있습니다.

try:
    a = int(input('정수를 입력하세요 : '))
    b = int(input('정수를 입력하세요 : '))
    print('{} / {} = {}'.format(a, b, a / b))
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('정수만 입력할 수 있습니다.')
except Exception:
    print('기타 오류가 발생했습니다') # 예상치 못한 오류 발생 시.

#! 3. 예외 메시지 처리하기
# 모든 예외는 기본적으로 예외 메세지를 내장하고 있다.
# as 키워드를 통해 except문서 예외 메세지를 가져올 수 있다.

#* 예외 메시지 처리의 기본형태
# try:
#     코드 작성 영역
# except 예외명 as 예외 메세지명:
#     예외 발생 처리 영역

# 리스트에 존재하지 않는 인덱스를 사용: IndexError 예외 발생
a = [10, 20, 30, 40, 50]

try:
    a[10]
except IndexError as message:
    print(message)