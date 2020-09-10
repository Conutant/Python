def main():
    print("This will average 3 exam scores")
    score1,  score2, score3 = input("Give me 3 score seperated by commas: ").split(',')
    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    score = (score1 + score2 + score3)
    average = score / 3
    print(score)
    print("The average score is " + str(average))

main()



# had to spit it
# had to make each score and int
# had to make the average output as a string.