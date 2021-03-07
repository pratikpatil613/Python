# pratik = komal = harshal = "man"
#
# print("pratik " + pratik)
# print("komal " + komal)
# print("harshal " + harshal)

number = int(input("enter number\n"))


def print_square(number):
    for num in range(number):
        print((str(num))+'*'+(str(num)), '\t=', num*num)


print_square(number)