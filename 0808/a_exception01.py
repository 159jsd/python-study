### 예외처리 ###

number = int(input('정수입력 : ')) # 사용자 입력란
print(f'입력한 숫자는 {number}입니다.')
# ValueError: invalid literal for int() with base 10: '안녕'
# - 사용자가 정수가 아닌 문자열을 입력할 경우 오류 발생

a = 5
b = 3
print(a + b)
