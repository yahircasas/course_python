print('Welcome to the username generator, this program creates a username with the exponencial distribution'
      '(pdf and CDF), the number in the pdf and CDF will be in your username!')
number = int(input('What is your favorite number between 0 and infinitive? '))
your_lambda = float(input('What is your favorite lamda? '))
zodiac = input('What is your zodiaz sign? ')
density = your_lambda*pow(2.7182, -1*your_lambda*number)
acumulate = 1-pow(2.7182,-1*your_lambda*number)

density=str(density)
acumulate=str(acumulate)

print(f'Your username is: {acumulate}{zodiac}{density}')
# print ('your name is: ' + str(CDF) +str(sign) + str(pdf)
