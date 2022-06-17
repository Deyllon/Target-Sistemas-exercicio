from ntpath import join


string = input("digite uma palavra ou um texto: ")
string_reversa = []
tamanho = len(string)

while tamanho > 0:
    string_reversa += string[tamanho-1]
    tamanho -= 1
    
    

string_reversa = "".join(string_reversa)
print(f" A palavra ou o texto ao contrario é igual a: {string_reversa} ")