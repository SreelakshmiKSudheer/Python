final = int(input("Upto what number you wanna play this FIZZ BUZZ game: "))
def FizzBuzz(final):
    for count in range(1,final + 1):
        if count % 3 == 0 and count % 5 == 0:
            print(str(count) + " = FIzz Buzz")
        elif count % 3 == 0:
            print(str(count) + " = Fizz")
        elif count % 5 == 0:
            print(str(count) + " = Buzz")
        else:
            print(count)
