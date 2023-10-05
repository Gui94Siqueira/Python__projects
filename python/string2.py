# fatiamento de strings
#       012345
#nome = 'python'
#nova_string = nome[1:4:2]
#print(nova_string)

#print("a"=="b")
#print("b" != "a")
#print("a" > "X")
#print("a" > "1")

nome = "python"

#percorrer com for

for i in nome:
    print(i)

#pecorrer com while

i = 0 
while i < len(nome):
    print(nome[i])
    i+=1
print('-----------------------')
#percorre com for / enumerte

for k, v in enumerate(nome):
    print(k,v)