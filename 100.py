def product_of_digits(number):
    d, s = str(number), 0
    while s <= (len(d)-5):
        print(int(d[s]) * int(d[s+1]) * int(d[s+2]) * int(d[s+3]) * int(d[s+4]))
        s += 1

product_of_digits(123456)
