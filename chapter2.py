def main():
    for i in range(5):
        print ("Welcome!")
        celsius = int(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print ("The temperature is " +  str(fahrenheit)  + " degrees Fahrenheit")

main()


# For this I had to modify it so that it could concatonate strings and ints.
# Eval did not work.
# If I put in 1.8 it works fine but not if I put in 9/5 ??
# Wasn't using python 3...