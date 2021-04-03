from predict import Predict

print('digite uma quantidade de dias')
try:
    days_input = int(input())
except:
    print('Sua entrada não é um numero inteiro, tente novamente')

answer = Predict()

answer.predict(days_input)
