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