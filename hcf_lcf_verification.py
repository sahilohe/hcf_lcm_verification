def hcf(number0, number1):

    if number0 > number1:
        smaller = number1
    else:
        smaller = number0
    for i in range(1, smaller+1):
        if((number0 % i == 0) and (number1 % i == 0)):
            HCF = i 
    return HCF


def lcm(number0, number1):

   if number0 > number1:
       greater = number0
   else:
       greater = number1

   while(True):
       if((greater % number0 == 0) and (greater % number1 == 0)):
           LCM = greater
           break
       greater += 1

   return LCM

while True:

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: \n"))

    print(f'HCF: {hcf(num1, num2)}')
    print(f'LCM: {lcm(num1, num2)}\n')

    print(f'The product of two numbers: {num1*num2}')
    print(f'The product of HCF and LCM : {hcf(num1, num2) * lcm(num1, num2)}\n')

