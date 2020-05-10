scoreInput = input('Enter score between 0.0 - 1.0')

try:
    score = float(scoreInput)
except:
    print('Enter only Numbers')
    quit()

if score <= 1.0 and score > 0.0:
    if score >= 0.9:
        grade = 'A'
        print(grade)
    elif score >= 0.8:
        grade = 'B'
        print(grade)
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print ('F')
else:
    print('Enter score between only 0.0-1.0')
