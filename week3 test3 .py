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