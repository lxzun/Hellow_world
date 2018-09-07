import os

class costomer:
    def __init__(self, ID, PW):
        self.ID = ID
        self.PW = PW
        self.bookshelf = []

    def buy_book(self):
        a = 0
        while a != 3:
            book_list = [x for x in Wep().book_list if self.bookshelf.count(x) == 0]
            a = int(input("\n1.구매 가능 목록    2.구매하기    3.나가기\n--> "))
            if a == 1:
                for i, x in enumerate(book_list):
                    print(i, '| ', x)
            if a == 2:
                b = int(input('\n원하는 책 번호를 입력하시오\n--> '))
                if b < len(book_list) and b >= 0:
                    self.bookshelf.append(book_list[b])
                else:print('\n없는 번호입니다.\n')

    def show_book(self):
        for i, x in enumerate(self.bookshelf):
            print(i, '| ', x)
        if self.bookshelf is False: print('\n구매하신 책이 없습니다.\n')

    def read_book(self):
        a = int(input("\n읽고 싶은 책 번호를 입력하세요\n-->"))
        if a < len(self.bookshelf) and a >= 0:
            f = self.bookshelf[a]
            f = open(os.getcwd()+'/book/'+f, 'r')
            print(f.read())
            f.close()
        else:print("\n없는 번호입니다.\n")


class Wep:
    def __init__(self):
        self.book_list = [x for x in os.listdir(os.getcwd()+'/book') if x.find('.txt') != -1]
        self.costomers = []

    def log_in(self, ID, PW):
        x = [x for x in self.costomers if x.ID == ID and x.PW == PW]
        if x:
            x = x[0]
            a = 0
            while a != 4:
                a = int(input("\n1.책 구매    2.내 책장    3.책 읽기    4.log_out\n--> "))
                if a == 1:
                    x.buy_book()
                if a == 2:
                    x.show_book()
                if a == 3:
                    x.read_book()

        else: print('\nFail\n')


    def join_with(self, ID, PW):
        self.costomers.append(ID, PW)

    def start(self):
        while 1:
            a = int(input("\n1.책 목록    2.log_in    3.join\n--> "))
            if a == 1:
                for i, x in enumerate(self.book_list):
                    print(i, '| ', x)

            if a == 2:
                ID = input('\nType your ID\n--> ')
                PW = input('\nType your PW\n--> ')
                self.log_in(ID,PW)

            if a == 3:
                b = 1
                ID = input('\nType your ID what you want\n--> ')
                for i in self.costomers:
                    if i.ID == ID:
                        print('\n이미 있는 ID 입니다.\n')
                        b = 0
                        break
                if b == 0: continue
                PW = input('\nType your PW what you want\n--> ')
                self.costomers.append(costomer(ID, PW))

a = Wep()
a.start()