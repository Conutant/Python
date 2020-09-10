def main():
    print("-----------------")
    print(" C      ||     F")
    print("-----------------")
    for i in range(11):      
        celsius = i * 10
        fahrenheit = 9/5 * celsius + 32
        print ("|" + str(celsius) + "  ------  " + str(fahrenheit) + "|")
    print("-------------------")
main()