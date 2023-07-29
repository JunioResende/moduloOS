import os
from time import sleep

print('caminho ate aqui')
caminho = os.getcwd()
print(caminho)

print('listar arquivos dentro de test folder')
listFiles = os.listdir()
print(listFiles)

print('criando pasta testFolder2')
os.mkdir('testFolder2')
print(listFiles)
sleep(10)
# remove testFolder2
os.rmdir('testFolder2')
