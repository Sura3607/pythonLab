import random
def chooseLevel():
    print(f"Level 1: 9 mang\nLevel 2: 4 mang\nLevel 3: 3 mang")
    isValid = False
    while(isValid == False):
        level = int(input("Chon Level 1-3: "))
        if 0< level< 4:
            isValid =True
    return 9 if level == 1 else 6 if level == 2 else 4

          
def game(level):
    print("========================================")
    print("          Tro choi doan so              ")
    print("========================================")
    secret = random.randint(1, 100)
    times = level
    while times > 0:
        guess = int(input("Doan: "))
        if guess == secret:
            print(f" ✅ Ban da doan dung. Ket qua la {secret}")
            return 1
        times -= 1
        print(f"--- ❌ Sai. Mang: {'❤️'*times} ---")
        if times == 0:
            print(f"Bạn đã không đoán được đáp án là: {secret}")
            break
        if guess > secret:
            print("Gợi ý: Nhỏ hơn")
        else:
            print("Gợi ý: Lớn hơn")
    return 0

def gameController():
    nPlay = 0
    nWin = 0
    level = chooseLevel()
    while True:
        nPlay+=1
        nWin+=game(level)

        print("Ban co muon choi tiep (n/N)")
        again = input("(n/N)").lower()
        if again == 'n':
            break
    
    print(f"Ban da choi {nPlay} Game\n---Win : {nWin}---\n---Lose : {nPlay-nWin}---")

        

if __name__ == '__main__':
    gameController()