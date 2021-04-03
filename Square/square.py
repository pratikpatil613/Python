number = int(input("enter number\n"))


def print_square(number):
    for num in range(1, number+1):
        print(1,' * ',num,' = ', num*num)


print_square(number)