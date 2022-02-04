class Account:
    # 클래스 내부에서 사용할 변수 초기화
    # self.변수이름 = 값
    def __init__(self, accountNo, ownerName, balance):
        self.c_accountNo = accountNo
        self.c_ownerName = ownerName
        self.c_balance = balance

    # 입금한다
    def deposit(self, amount):
        # self.c_balance = self.c_balance + amount
        self.c_balance += amount

    # 출금한다 
    def withdraw(self, amount):
        # 기존 잔액 < 출금하려는 금액  
        if self.c_balance < amount:
            return 0

        # self.c_balance = self.c_balance - amount
        self.c_balance -= amount
        return amount

# obj1 객체 생성
# 객체이름 = 클래스()
obj1 = Account("111-222-3333333", "정수아", 50000)

# obj2 객체 생성
obj2 = Account("555-666-7777777", "손이안", 100000)

# 영수증 출력
def printAccount(obj):
    print("계좌번호 : " + obj.c_accountNo)
    print("예금주 이름 : " + obj.c_ownerName)
    print("잔액 : " + str(obj.c_balance))
    print()

# 입금한다
# 클래스 내부 함수 호출 방법 : 객체이름.함수이름()
obj1.deposit(100000)     # c_balance -> 150000

# 영수증 출력
printAccount(obj1)

# 출금한다
obj2.withdraw(30000)    # c_balance -> 70000

# 영수증 출력
printAccount(obj2)