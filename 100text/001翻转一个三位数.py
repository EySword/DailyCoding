number=900

def reverseInteger(number):
    h=number//100
    t=number%100//10
    z=number%10

    outNumber=100*z+10*t+h
    return outNumber

print(reverseInteger(number))