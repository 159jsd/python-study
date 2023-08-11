class Book():
    def set_info(self, name, author):
        self.name = name
        self.author = author
    
    def print_info(self):
        print(f'책의 이름은 {self.name}, 저자는 {self.author}입니다.')

book1 = Book()
book2 = Book()

book1.set_info('파이썬', '이승아')
book2.set_info('어린왕자', '생택쥐페리')

book1.print_info()
book2.print_info()