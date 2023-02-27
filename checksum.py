#Checsum algorithm
DATA = '10111001011000101101011100011010'
CHECKSUM_BIT = 8

def binary_addition(a,b):
    #Padding
    if(len(a)>len(b)):
        diff = len(a)-len(b)
        padding = "0"*diff
        b=padding+b
    elif(len(b)>len(a)):
        diff = len(b)-len(a)
        padding = "0"*diff
        a=padding+a
    n=len(a)
    sum=''
    carry=0
    for i in range(n-1, -1, -1):
        sum_int=carry+int(a[i]) + int(b[i])
        if(sum_int>1):
            carry=1
            sum_int=sum_int%2
        else:
            carry=0
        sum+=str(sum_int)
    if(carry==1):
        sum+=str(carry)
    sum=sum[::-1]
    return sum

#9, 2, 3, 8
#Sum = 22
#Frame 4 contains the 1's complement form of the summation of 9,2,3,8 in binary
frame_dict = {
    "frame0":"00001001",
    "frame1":"00000010",
    "frame2":"00000011",
    "frame3":"00001000",
    "frame4": "11101001"
}

# for i in range(len(DATA)):
#     pos=i//CHECKSUM_BIT
#     frame_dict[f"frame{pos}"]+=DATA[i]

# print(binary_addition('111', '10'))
val='0'
sum=''
for i in range(0,5):
    number = frame_dict[f"frame{i}"]
    sum=binary_addition(val, number)
    val=sum
frame_dict.update({"frame5":""})
print(frame_dict)
print(sum)


