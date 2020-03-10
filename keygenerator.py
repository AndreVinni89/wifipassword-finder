import wififunctions as wf
import xml.etree.ElementTree as ET
import requests


#criando pasta
wf.criarpasta()

#gerando arquivos das info das senhas atraves do cmd
wf.gerarsenhas()

#listando o nomes dos arquivos de senha
arqs = wf.arqnames()

#gerando Keys
for arq in arqs:
    print(arq , end=' -> ')
    keys = wf.key(arq)
    print(keys)

x = input('Digite qualquer tecla para sair!!!')
