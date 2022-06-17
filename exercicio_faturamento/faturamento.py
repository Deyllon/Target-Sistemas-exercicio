import json

menor = 100000000000000
maior = 0
total = 0
contador = 0
with open("dados.json") as f:
    faturamento = json.load(f)
    
for f in faturamento:
    if f["valor"] != 0:
        if f["valor"] < menor:
            menor = f["valor"]
        if f["valor"] > maior:
            maior = f["valor"]
        total += f["valor"]
        contador+=1


media = round(total/contador, 4)



print(f"O menor faturamento foi: {menor} e o maior faturamento: {maior} e a media de faturamento do mês foi {media}")
            
    
