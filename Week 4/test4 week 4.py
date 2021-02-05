import os
choice = 0
listcom = [0,0,0,0,0,]
compick = 0
def menu():
    global choice
    print('\tโปรแกรมร้านเเต่งคอม\n','1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ : ')
    screen_clear()

def showmenu(): 
    print('\tรายการสินค้าร้านแต่งคอม')
    print('1.ซีพียู ราคา 5,000 บาท\n 2.เคส ราคา 1,000 บาท\n 3.จอภาพ ราคา 2,000 บาท\n 4.คีย์บอร์ด ราคา 500 บาท\n 5.แรม ราคา 2,000 บาท\n')

def pickmenu():
    global pick
    print("\t1.ซีพียู \t2.เคส \t3.จอภาพ \t4.คีย์บอร์ด \t5.แรม")
    pick = int(input('เลือกหยิบสินค้าหมายเลข :'))
    if pick == 1:
        listcom[0] += 1
    elif pick == 2:
        listcom[1] += 1
    elif pick == 3:
        listcom[2] += 1
    elif pick == 4:
        listcom[3] += 1
    elif pick == 5:
        listcom[4] += 1
    screen_clear()

def showuserpick():
    list_score = ["ซีพียู","เคส","จอภาพ","คีย์บอร์ด","แรม"]
    list_price = [5000,1000,2000,500,2000]
    print('{0:-<10}{1:-<10}{2:-<13}{3}'.format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print('{0:-<10}{1:-<10}{2:-<13}{3}'.format(list_score[i],list_price[i],listcom[i],listcom[i]*list_price[i]))

def deletuserpick():
    print("\t\n1.ซีพียู\n 2.เคส\n 3.จอภาพ\n 4.คีย์บอร์ด\n 5.แรม\n")
    depick = int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก'))
    if depick == 1:
        listcom[0] -= 1
    elif depick == 2:
        listcom[1] -= 1
    elif depick == 3:
        listcom[2] -= 1
    elif depick == 4:
        listcom[3] -= 1
    elif depick == 5:
        listcom[4] -= 1

def screen_clear():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        showmenu()
    elif choice == '2':
        screen_clear()
        pickmenu()
    elif choice == '3':
        screen_clear()
        showuserpick()
    elif choice == '4':
        deletuserpick()
        screen_clear()
    elif choice == '5':
        c = input('ต้องการใช้โปรแกรมต่อหรือไม่ y/n: ')
        if c.lower() == 'n':
            screen_clear()
        elif c.lower() == 'y':
            screen_clear()
            break