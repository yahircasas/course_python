# For each point, use the print() function

# 1. Use 'in' operator to obtain a True value
name = 'Yahir'
print('Yah' in name)

# 2. Use not in operator to obtain a True value
book = "El placer de la X"
print('integral' not in book)

# 3. Use * operator with a string (as you want)
print(name * 3)

# 4. Use + operator with a string and with a list(as you want)
surname = 'Casas'
print(name + surname)

# ------------------- Slicing for strings-----------------------
# We can use s[i:j:k] to make a slicing in python, solve each point

# 5. From the sentence, print out "is a logical consequence of the axioms and previously proved theorems"
sentence = """In mathematics, a theorem is a statement that has been proved, or can be proved. The proof of a theorem 
is a logical argument that uses the inference rules of a deductive system to establish that the theorem 
is a logical consequence of the axioms and previously proved theorems."""
print(sentence[176:])  # se imprime una porción específica de la variable sentence

# 6.From the user's input, print the name, but beginning with the last names. Make sure each first letter is capitalized
# sheldon axler -> Axler Sheldon
# name = input('What is your full name? ') UNCOMMENT WHEN YOU USE THIS
name_6 = 'sheldon axler'
new_name = name_6.split()  # se divide la cadena en una lista de palabras
print(new_name[1].capitalize(),new_name[0].capitalize())  # se imprimen las palabras en orden inverso con la primera letra en mayúscula

# 7. 'tcerroc eht tuo tnirp dna ti esrever tsuJ .od ot deen uoy tahw tuoba tnih a uoy evig ot ecnetnes a tsuj si sihT'
sentence_2 = '.od ot deen uoy tahw tuoba tnih a uoy evig ot ecnetnes a tsuj si sihT'
new_sentence_2 = sentence_2[::-1]  # se utiliza un slicing para invertir la cadena de caracteres
print(new_sentence_2)

# 8. The frog jump two letters in the mot string. What is the final string?
mot = 'you are doing well. Do not doubt on you!'
print(mot[::2])  # se imprime cada segundo carácter de la cadena mot

# 9. From the sentence variable, how many characters are in there?
print(len(sentence))  # se imprime la longitud de la cadena sentence