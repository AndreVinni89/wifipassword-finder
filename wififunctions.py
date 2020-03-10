def criararquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')


def key(arqxml):
    import xml.etree.ElementTree as ET
    tree = ET.parse(f'C:\keys\{arqxml}')
    root = tree.getroot()
    filtro = '*'
    for child in root.iter(filtro):
        if child.tag == '{http://www.microsoft.com/networking/WLAN/profile/v1}keyMaterial':
            return (child.text)


def arqnames():
    import os
    list = os.listdir(f'C:\keys')
    return (list)


def gerarsenhas():
    try:
        import os
        os.system('netsh wlan show profile')
        os.system('netsh wlan export profile folder=C:\keys key=clear')
    except:
        print('ERRO! Tente executar o programa como administrador!')
    else:
        print('Senhas geradas com sucesso!')


def criarpasta():
    import os
    try:
        directorypath = R'C:\keys'
        os.mkdir(directorypath)
    except:
        print('pasta ja existe')
    else:
        print('pasta criada com sucesso')