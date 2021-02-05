a = 60
b = 13
c = 0

c = a & b
print(c)

c = a | b 
print(c)

c = a ^ b
print(c)

c = ~a
print(c)

c = a << 2
print(c)

c = a >> 2
print(c)


#Korawan Kamesri
print("Day Converter Program")
num_day = int(input("Input number of Days --> "))
print(num_day,"Days --> Hour",24*num_day,"Hours")
print(num_day,"Days --> Minutes",60*24*num_day,"Minutes")
print(num_day,"Days --> Seconds",60*60*24*num_day,"Seconds")


#Korawan Kamesri 633050433-8
#Day Converter Program
x=int (input("Number of Days-->"))
print("Days--> Hour :",24*x,"Hour")
print("Days--> Minutes :",60*24*x,"Minutes")
print("Days--> Seconds :",60*60*24*x,"Seconds")


friend=["jan","cream","phu","bam","aom","pee","bas","kong","da","james"]
friend.append("dome")
friend.append("poondang")
friend.insert(1,"csa")

animal={"cat","dog","rat","pig","ant"}
animal.add("monkey")


food = []
for i in range(1,6):
    number_food = input("หยิบสินค้าชิ้นที่ %d : "%i)
    food.append(number_food)
print("สินค้าที่หยิบใส่ตะกร้ามีดังนี้\n 1.",food[0])
print("2.",food[1])
print("3.",food[2])
print("4.",food[3])
print("5.",food[4])

print("\tโปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์")
print("_"*50)
print("\tรถยนต์ 4 ล้อ กด 1")
print("\tรถยนต์ 6 ล้อ กด 2")
print("\tรถยนต์มากกว่า 6 ล้อ กด 3\n")
car1_list = ["ลาดกระบัง-->บางบ่อ:25 บาท","ลาดกระบัง-->บางประกง:30 บาท","ลาดกระบัง-->พนัสนิคม:45 บาท","ลาดกระบัง-->บ้านบึง:55 บาท","ลาดกระบัง-->บางพระ:60 บาท"]
car2_list = ["ลาดกระบัง-->บางบ่อ:40 บาท","ลาดกระบัง-->บางประกง:45 บาท","ลาดกระบัง-->พนัสนิคม:75 บาท","ลาดกระบัง-->บ้านบึง:90 บาท","ลาดกระบัง-->บางพระ:100 บาท"]
car3_list = ["ลาดกระบัง-->บางบ่อ:60 บาท","ลาดกระบัง-->บางประกง:70 บาท","ลาดกระบัง-->พนัสนิคม:110 บาท","ลาดกระบัง-->บ้านบึง:130 บาท","ลาดกระบัง-->บางพระ:140 บาท"]
car = int(input("\tเลือกประเภทยานพาหนะ : """))
if car == 1:
    print("\tค่าบริการรถยนต์ 4 ล้อ")
    for x in car1_list:
        print("\n",x)
elif car == 2:
    print("\tค่าบริการรถยนต์ 6 ล้อ")
    for x in car2_list:
        print("\n",x)
elif car == 3:
    print("\tค่าบริการรถยนต์ 6 ล้อขึ้นไป")
    for x in car3_list:
        print("\n",x)


print("เลือกเมนูเพื่อทำรายการ")
print("############################")
print("กด 1 เลือกเหมาจ่าย")
print("กด 2 เลือกจ่ายเพิ่ม")
choose = int(input(""))
Km = int(input("กรอกระยะทาง"))
if choose == 1 :
    if Km <= 25 :
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท")
    else :
        print("ค่าใช้จ่ายรวมทั้งหมด 55 บาท") 
if choose == 2 :
    if Km <= 25 :
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท")
    else :
        print("ค่าใช้จ่ายรวมทั้งหมด 80 บาท")


print(" กรุณากรอกจำนวนครั้งการรับค่า")
n = int(input(" "))
i = 1
sum = 0
while (i<= n) :
    d = int(input("กรอกตัวเลข"))
    i += 1
    sum = sum + d
print(" ผลรวมค่าที่รับมาทั้งหมด = " + str(sum))


print("    ป้อน")
i=0
c=1
blist=[]
while (True):
    i+=1 
    b=str(input(" "+str(c)+":"))
    blist.append(b)
    c+=1
    if(b=="exit"):
        break    
print("อาหารโปรดของคุณมีดังนี้")
for x in range (1,i):
    print(x,'.',blist[x-1])

    

print(" ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากระบบ ")
i = 0
keylist = []
while(True) :
    i += 1
    key = str(input("อาหารสุดโปรดลำดับที่ " +str(i).format(i)))
    keylist.append(key)
    if(key == 'exit') :
        break
for x in range (1,i) :
    print(x,".",keylist[x-1],end ="  ") 


a=[]
while True:
    b = input('----ร้านคุณหลินบิวตี้-----\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n')
    b = b.lower()
    if b=='a': 
        c = input('ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด')
        a.append(c)
        print('\n*************ข้อมูลได้เข้าสู่ระบบแล้ว*********\n')
    else b == 's' :
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a: 
            e = d.split(":")
            print('{0[0]:<6} {o[1]:<10}({0[2]:<10})'.format))
            continue
    elif b == 'x':
        break
print('คำสั่งถัดไป')


a=[]
while True:
    b = input('----ร้านคุณหลินบิวตี้-----\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n')
    b = b.lower()
    if b=='a': 
        c = input('ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด')
        a.append(c)
        print('\n*************ข้อมูลได้เข้าสู่ระบบแล้ว*********\n')
    else b == 's' :
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a: 
            e = d.split(":")
            print('{0[0]:<6} {o[1]:<10}({0[2]:<10})'.format))
            continue
    elif b == 'x':
        break
print('คำสั่งถัดไป')







score_l = ['90-100','80-89', '70-79', '60-69','50-59', '0-49']
sum_s = [0,0,0,0,0,0] 
n = int(input("จำนวนนักเรียนที่คุณต้องการ :"))
i = 0
while i < n: 
    score = int(input("คะแนนของนักเรียนคนที่ "+str(i+1)+" :"))
    i +=1 
    if score<=100 and score>=90:
        sum_s[0] +=1 
    elif score<98 and score>=80:
        sum_s[1] +=1 
    elif score<88 and score>=70:
        sum_s[2] +=1 
    elif score<70 and score>=60:
        sum_s[3] +=1 
    elif score<60 and score>=50:
        sum_s[4] +=1 
    else:
        sum_s[5] +=1 
for j in range(0,6): 
    print(score_l[j],":", sum_s[j]*"*")















