import string

#Funcion para eliminar las puntuaciones y espaciones en blanco
def eliminate_punctuations(word):
    word = word.lower()
    for x in word:
        if x in string.punctuation or x == " ":
            word=word.replace(x,"")
    return word

#Fucnion que regresa si dos palabras son anagramas
def are_anagrams(word1, word2):
    
    word1 = eliminate_punctuations(word1)
    word2 = eliminate_punctuations(word2)

    #Ordenamos los caracteres
    word1 = sorted(word1)
    word2 = sorted(word2)
    
    if word1 == word2:
        return True #si ambas cadenas son iguales, devuelve True
    else:
        return False    #False en caso contrario

word1 = input("Ingresa la primera palabra o frase: ")
word2 = input("Ingresa la segunda palabra o frase: ")

if (are_anagrams(word1,word2)):
    print("Si son anagramas!!")
else:
    print("No son anagramas")
