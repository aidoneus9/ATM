# balance : 통장에 들어있는 기본 금액을 담는 변수 
# 1. 입금, 2. 출금, 3. 영수증 보기, 4. 종료 => 글자를 입력 받을지(입금, 출금...) / 숫자를 입력받을지(1, 2, 3...)
# 숫자로 원하는 기능을 입력, 사용자가 입력한 기능은 num 변수에 담김 
# deposit_amount:
# withdrawal_amount:
# 영수증 기능에 사용되는 데이터 타입은 list 

# date.time 기능 이용해서 붙이기 // 11시 이후 접근 불가하게 만들기 

receipts = []

# 잔고
balance = 3000

# 사용자가 입력한 기능
while True: # while date.time.hour() < 12
    num = input("원하시는 서비스의 번호를 입력해 주세요. 입금: 1, 출금: 2, 영수증 보기: 3, 종료: 4 \n 입력: ")

    # 입금하기 💰
    if num == "1":
        deposit_amount = int(input("입금하실 금액을 숫자로 입력해 주세요. \n 입력: "))

        if isinstance(deposit_amount, int) and deposit_amount > 0: 
            # 참고: isdigit()은 문자열 내 숫자를 판별하는 메서드이므로, 숫자가 정말 숫자인지를 알고 싶으면 isinstance()를 쓰는 게 맞음 
            balance += deposit_amount
            print(f"입금이 완료되었습니다. 입금한 금액: {deposit_amount}, 현재 잔액: {balance}")

            # 영수증에 데이터 넣기
            receipts.append(["입금", deposit_amount, balance])

        else:
            print("입금 금액💰은 숫자로만 입력하실 수 있습니다.")

    if num == "2":
        withdrawal_amount = int(input("출금하실 금액💵을 숫자로 입력해 주세요. \n 입력: "))

        if isinstance(withdrawal_amount, int) and withdrawal_amount > 0: 
            withdrawal_amount = min(withdrawal_amount, balance)
            balance -= withdrawal_amount
            print(f"출금이 완료되었습니다. 출금한 금액: {withdrawal_amount}, 현재 잔액: {balance}")

            # 영수증에 데이터 넣기
            receipts.append(["출금", withdrawal_amount, balance])

        else:
            print("출금 금액💵은 숫자로만 입력하실 수 있습니다.")

    if num == "3":
        if receipts: 
            print("===🧾 영수증===")
            for i in receipts:
                print (f"{i[0]} : {i[1]}원 | 잔액 {i[2]}원")
        else:
            print("내역이 없습니다.")

    if num == "4":
        print("서비스를 종료합니다.")
        break



