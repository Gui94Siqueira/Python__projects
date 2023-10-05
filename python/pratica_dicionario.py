dicionario = {"dia1":"domingo","dia2":"segunda","dia3":"terça","dia4":"quarta","dia5":"quinta","dia6":"sexta","dia7":"sabado"}
dicionario.popitem()
dicionario.popitem()
del(dicionario["dia2"])
print(dicionario.keys())
print(dicionario.values())
print(dicionario)