print('โปรแกรมสินค้าออนไลน์')
print('*'*50)
shop_list=[]
number = [0,0,0,0,0,0,]
price = [5000,1000,2000,500,2000,5000]
cargo = ["ซีพียู","เคส","จอภาพ","คีย์บอร์ด","แรม","การ์ดจอ"]
n = 0
s = 1

def list_item():
    print("\tรายการสินค้า")
    print("*"*25)
    print('1.ซีพียู ราคา 5,000 บาท\n 2.เคส ราคา 1,000 บาท\n 3.จอภาพ ราคา 2,000 บาท\n 4.คีย์บอร์ด ราคา 500 บาท\n 5.แรม ราคา 2,000 บาท\n 6.การ์ดจอ บาท\n')
def pick_item():
    c=0
    while(True):
        print("1.ซีพียู\n 2.เคส\n 3.จอภาพ\n 4.คีย์บอร์ด\n 5.แรม\n 6.การ์ดจอ\n")
        c=(input("เลือกหยิบสินค้าหมายเลข: "))
        try:
            if int(c)==1 or c=="1":
                shop_list.append("ซีพียู")
            elif int(c)==2 or c=="2":
                shop_list.append("เคส")
            elif int(c)==3 or c=="3":
                shop_list.append("จอภาพ")
            elif int(c)==4 or c=="4":
                shop_list.append("คีร์บอรืด")
            elif int(c)==5 or c=="5":
                shop_list.append("แรม")
            elif int(c)==6 or c=="6":
                shop_list.append("การ์ดจอ")
                break
            else:
                print("กรุณากรอกหมายเลขให้ถูกต้อง")
                pass
def show_item():
    for i in shop_list:
        if i == "ซีพียู":
            number[0]+=1
        elif i == "เคส":
            number[1]+=1
        elif i == "จอภาพ":
            number[2]+=1
        elif i == "คีร์บอร์ด":
            number[3]+=1
        elif i == "เเรม":
            number[4]+=1
        elif i == "การ์ดจอ":
            number[5]+=1

ืีnumberttt=number[0]+number[1]+number[2]+number[3]+number[4]
pricett=number[0]*15+number[1]*10+number[2]*20+number[3]*+number[4]*25
print("")
print("สินค้าที่คุณได้หยิบไปมีดังนี้")
print('สินค้า--------จำนวน-------ราคา')


            