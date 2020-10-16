name_list = []
age_list = []
phone_list = []

class person:
    def name(self):
       name_list.append(input("이름을 입력하세요"))
    def age(self):
        age_list.append(input("나이를 입력하세요"))

class content(person):
    def phone(self):
        phone_list.append(input("핸드폰 번호를 입력하세요"))

class container(content):
    def create(self):
        container.name(self)
        container.age(self)
        container.phone(self)
    def update(self):
        search = input("수정하고싶은 사람의 이름을 입력하세요")
        if search in name_list:
            age_list[name_list.index(search)] = input("새로운 나이를 입력하세요")
            phone_list[name_list.index(search)] = input("새로운 연락처를 입력하세요")
    def delete(self):
        search = input("지우고싶은 사람의 이름을 입력하세요")
        if search in name_list:
            phone_list.remove(name_list.index(search))
            age_list.remove(name_list.index(search))
            name_list.remove(name_list.index(search))

def main():
    a = container()
    print("전화번호를 저장하는 프로그램입니다.\n생성 = 1\t 수정 = 2\t 삭제 = 3\t 목록보기 = 4\t 종료 = 0 을 입력하세요")
    num = input()
    while True:
        if num == '1':
            a.create()
            print("저장이 완료되었습니다\n생성 = 1\t 수정 = 2\t 삭제 = 3\t 목록보기 = 4\t 종료 = 0 을 입력하세요")
            num = input()
        elif num == '2':
            a.update()
            print("수정이 완료되었습니다\n생성 = 1\t 수정 = 2\t 삭제 = 3\t 목록보기 = 4\t 종료 = 0 을 입력하세요")
            num = input()
        elif num == '3':
            a.delete()
            print("삭제가 완료되었습니다\n생성 = 1\t 수정 = 2\t 삭제 = 3\t 목록보기 = 4\t 종료 = 0 을 입력하세요")
            num = input()
        elif num == '4':
            for i in range(0,len(name_list)):
                print(i,"번 목록 이름 : ",name_list[i],"나이 : ",age_list[i],"연락처 : ",phone_list[i],"입니다")
            print("생성 = 1\t 수정 = 2\t 삭제 = 3\t 목록보기 = 4\t 종료 = 0 을 입력하세요")
            num = input()
        elif num == '0':
            break
        else:
            print("숫자를 잘못 입력하였습니다\n생성 = 1\t 수정 = 2\t 삭제 = 3\t 목록보기 = 4\t 종료 = 0 을 입력하세요")
            num = input()


main()
