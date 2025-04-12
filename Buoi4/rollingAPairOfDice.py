import random

def rolling():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"Xuc xac 1 : {dice1}\nXuc xac 2 : {dice2}")
    return dice1,dice2, dice1+dice2

def guessing():
    print("1. TÀI\n2. XỈU")
    while True:
        guess = int(input("Ban chon: "))
        if 0< guess< 3:
            return guess

def bet(totalAmount):
    while True:
        print(f"Ban dang hien co {totalAmount}$")
        b = int(input("Cược (Cược phải lớn hơn 10,000$) :"))
        if 9999 < b <= totalAmount:
            return b
        print("Khong hop le!")

def result(totalDice, guess):
    r = 2
    if totalDice > 5:
        r = 1
    print(f"---Ket qua : {"Tài" if r == 1 else "Xỉu"}---")
    if guess == r:
        print("Ban da doan dung")
        return True
    print("Ban da doan sai")
    return False

def afterPlay(nPlay, nWin, amount, BaseAmount = 100):
    print(f"Ban da choi {nPlay} van")
    print(f"---Win : {nWin} van---")
    print(f"---Lose: {nPlay-nWin} van---")
    print(f"So du cuoi cung: {amount}$")
    res = amount - BaseAmount
    if res> 0:
        print(f"===Loi : {res}$===")
    elif res < 0:
        print(f"===Lo : {res}$===")
    else:
        print("Ban hoa von")
    
def gameController():
    BaseAmount = 100000
    amount = BaseAmount
    nGame = 0
    nWin = 0

    while True:
        nGame +=1
        guess = guessing()
        userBet = bet(amount)
        d1,d2,totalDice = rolling()
        isWin = result(totalDice,guess)
        if isWin:
            nWin+=1
            amount += userBet
            print(f"So du +{userBet}$")
            print(f"So du hien tai: {amount}$")
        else:
            amount -= userBet
            print(f"So du -{userBet}$")
            print(f"So du hien tai: {amount}$")

        isExit = input("Ban co muon tiep tuc (y/n)").lower()
        if isExit == 'n':
            break

        if amount < 1:
            print("Ban da het tien")
            break

    afterPlay(nGame,nWin,amount,BaseAmount)

if __name__ == '__main__':
    gameController()
    


