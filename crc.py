#This function is for XOR operation without using ^ operator
def XOR(a, b):
    xor_output=''
    for i in range(len(a)):
        diff=abs(int(a[i])-int(b[i]))
        xor_output+=str(diff)
    return xor_output

#Binary division using XOR
def division(frame, generator):
    n=len(generator)
    count=n
    a=frame[:n] #Selects a part of frame. length of the selected part is equal to the length of the generator
    while True:
        xor_output=XOR(a,generator)
        index=xor_output.find('1') #Finds the first index of 1 in the output. This is because in the next iteration, the new division will be performed on a binary number that begins with '1'
        a=xor_output[index:] #This extracts the part of the output where the first element is '1'

        #This part adds extra bit from the dividend(original frame) to the modified XOR output so as to make the binary number's length equal to the length of the generator
        if(len(a)<n):
            required=n-len(a)
            #Overflow check
            if(count+required>len(frame)):
                break
            else:
                a+=frame[count: count+required]
                count+=required
    #Adds the extra bits from the dividend to the output
    if(count<len(frame)):
        xor_output+=frame[count:]
    
    xor_output=xor_output[(len(xor_output)-(n-1)):] #This part extracts only the last n-1 bits from the output. n = length of generator
    added_result=str(int(frame)+int(xor_output)) #This part replaces the last n-1 bits from the dividend with the new XOR output
    print(added_result)


frame = input("Enter the frame value: ")
generator = input("Enter the generator value: ")
n=len(generator)
#Padding
for i in range(n-1):
    frame+='0'

division(frame, generator)