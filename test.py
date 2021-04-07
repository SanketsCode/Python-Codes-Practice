def print_formatted(number):
    for i in range(1,number+1):
        binary = bin(i)[2:]
        decimal = 0
        for digit in binary: 
            decimal = decimal*2 + int(digit) 
        print(decimal,oct(i)[2:],hex(i)[2:],bin(i)[2:])
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)