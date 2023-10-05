dicionario = {"a":"letraA","b":"letraB","c":"letraC"}
print(dicionario["a"])
print(dicionario.get('c', 'Valor não encontrado.'))

agenda = {40408021:"josé", 87541236:"heloise", 78945612:"carlos",36925874:"claudio"}
print(agenda)
del(agenda[40408021])
print(agenda)

print(agenda.keys())
print(agenda.values)
print(len(agenda))

print(agenda.popitem())
print(agenda.popitem())
print(agenda)

