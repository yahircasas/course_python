
#Manera de utilizar los keywords arguments, todoa asi o tidos posionales.
# ra = range(1,10,2) # unicamente posicional
# ra = range(start=1,end=10,2) #La built funtion esta definida unicmanete psocional

#Defining a function with positional- only.
# def func1(value1, value2, value , /):
#     print(value1/value2 + value2)
# func1(1,2,3)

#Posicional-or-keyword with a built-in
#Complex va a permitir posiiconal and jey words arguments


# com = complex(imag=5, real=1)
# com2 = complex(real=1, imag=5)
# com2 = complex(5,4)
# com4 =complex(10)
# print( com4)

#Defininf a function with posicional-or-keywords
# def fun2(r, i=0):
#     print(f'{r}+{i}j')
# fun2(i=4,r=8)

#Keyword only
# def func3(pos1,*,live, student=''):
#     print(live+student+str(pos1))
#
# func3(5,live='True', student='jake')

# def some(obs, k_or_guess, my_iter='29',/,thresh='1e´05',check_finity='True',*,seed='None'):
#     print(obs+k_or_guess+my_iter+thresh+check_finity+seed)
#
# some('hola','adios',seed='example')

