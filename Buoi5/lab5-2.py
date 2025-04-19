import random
import os
import time


def userInput(n = 100):
    while True:
        user = int(input(f"Nhap so trong khoan 1-{n} : " ))
        if 0< user <= n:
            return user

def menu():
    print("""===========================MENU=======================================
1.In ra danh sách vừa tạo.
2.In đảo ngược danh sách.
3.Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
4.tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
5.đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
6.In ra vị trí các phần tử là số nguyên tố.
7.tìm các số duy nhất (không trùng lặp) trong danh sách.
8.liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
9.In ra các đoạn con trong danh sách giảm liên tiếp.
10.Thoát.
===========================CHOOSE ONE=======================================""")
    while True:
        user = int(input("Nhap: "))
        if 0< user< 11:
            return user
        
def createList(n):
    return [random.randint(1, 100) for _ in range(n)]

def revertList(l):
    return l[::-1]

def sortList(l):
    return sorted(l)

def findLastMaxValue(l):
    maxIndexValue = 0
    maxValue = l[0]
    for i in range(1,len(l)):
        if l[i] >= maxValue:
            maxValue = l[i]
            maxIndexValue= i
    return (maxValue,maxIndexValue)

def countValue(l,x):
    c = 0
    pos = []
    for i in range(len(l)):
        if x == l[i]:
            c+=1
            pos.append(i)
    return c,pos

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def findPrime(l):
    pos = []
    value = []
    for i in range(len(l)):
        if isPrime(l[i]):
            pos.append(i)
            value.append(l[i])
    return pos,value

def countNum(l):
    count = {}
    for i in l:
        if i not in count:
            count[i] =1
        else:
            count[i]+=1
    return [(key,value) for key, value in count.items()]

def uniqueNum(l):
    count = countNum(l)
    return [num for num, value in count if value == 1]

def subNumLst(l):
    newList = sorted(l,reverse=True)
    sub = []
    i = 0
    j = 1
    while i < len(l) and j < len(l):
        if j- i == newList[i] - newList[j]:
            j+=1
        else:
            sub.append(newList[i:j])
            i = j
            j = i+1
    sub.append(newList[i:j])
    return sub
        

def controller():
    isContinue = True
    n = userInput()
    userList = createList(n)
    while isContinue:
        choose  = menu()
        match choose:
            case 1:
                print(f"Mang cua ban la: {userList}")
            case 2:
                print(revertList(userList))
            case 3:
                print(sortList(userList))
            case 4:
                max, idx = findLastMaxValue(userList)
                print(f"Phần tử lớn nhất: {max}")
                print(f"Vị trí phần tử lớn nhất cuối cùng: {idx}")
            case 5:
                n = int(input("Nhap: "))
                print(f"số lượng các phần tử bằng giá trị {n} là: {countValue(userList,n)[0]}")
            case 6:
                pos , v = findPrime(userList)
                print(f"Mang cua ban la: {userList}")
                print(f"Vị trí các phần tử là số nguyên tố: {pos}")
            case 7:
                print(f"Mang cua ban la: {userList}")
                print(f"Các số duy nhất (không trùng lặp) trong danh sách : {uniqueNum(userList)}")
            case 8:
                l = countNum(userList)
                print(f"Mang cua ban la: {userList}")
                for v, f in l:
                    print("Giá trị ",v," xuất hiện ",f," lần")
            case 9:
                sub = subNumLst(userList)
                print("Các đoạn con trong danh sách giảm liên tiếp:")
                for i in sub:
                    print(f"\t{i}")
            case 10:
                isContinue = False
        time.sleep(2)


if __name__ == '__main__':
    controller()