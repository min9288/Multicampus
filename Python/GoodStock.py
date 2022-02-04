class GoodStock:
    def __init__(self, code, num):   # 변수 초기화
        self.goodsCode = code
        self.stockNum = num       # 재고 수량

    def addStock(self, amount):   # 추가된 수량
        # 재고 수량 = 재고 수량(기존수량) + 추가된 수량
        # self.stockNum = self.stockNum + amount
        self.stockNum += amount

# 클래스 만든 이유 ??? -> 결과물(객체) 생성하려고
# input() 함수의 결과 값 -> 데이터 타입 : string

code =  input("상품 코드를 입력하세요 : ")
num = int(input("재고 수량을 입력하세요: "))

# 객체 생성
# 객체이름 = 클래스이름()
obj = GoodStock(code , num)

# 객체에 저장된 내용 출력
print("상품 코드 : " + obj.goodsCode)
print("재고 수량 : " + str(obj.stockNum))

# 추가할 수량
amount = int(input("추가할 수량을 입력하세요 : "))

# addStock() 호출
obj.addStock(amount)

# 화면 출력
print("재고 수량 : " + str(obj.stockNum))