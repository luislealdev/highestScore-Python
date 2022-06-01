scores = input("Enter the scores separated by commas ex.(10,9,8,5): ").split(',')
for i in range(0, len(scores)):
    scores[i] = int(scores[i])
highestScore = 0;
for score in scores:
    if(score>highestScore):
        highestScore = score

print(f"The highest score is: {highestScore}")