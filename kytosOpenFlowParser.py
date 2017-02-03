'''
Kytos Challenge
Autor: Leandro Pessoa
Versao python: 2.7

Instrucoes:
Instalar requirements.txt: pip install -r requirements.txt
Para executar script: python kytosOpenFlowParser.py ofpt_hello.dat 
'''


import sys

import pandas as pd

#Abre arquivo 
file = open(sys.argv[1], "rb")

#Lista que recebe bytes do arquivo
raw_header = []
#leitura do primeiro byte
byte = file.read(1)
#Adiciona primeiro byte em lista
raw_header.append(byte.encode('hex'))
#Loop condicional 
while byte != b"":
	#Leitura de byte a byte
	byte = file.read(1)
	#Adiciona byte lido anteriormente em lista
	raw_header.append(byte.encode('hex'))

#Dicionario a receber header formatado de acordo com definicao presente em documentacao
#OpenFlow Switch Specification 1.0.0, paginas 15-16
header = {}
header['version'] = int(raw_header[0])
header['type'] = int(raw_header[1])
header['length'] = int(raw_header[2] + raw_header[3])
header['xid'] = raw_header[4] + raw_header[5] + raw_header[6] + raw_header[7]


#Carrega tabela de referencia para identificacao de campos do header
#Tabela obtida de: http://flowgrammable.org/sdn/openflow/message-layer/
flowMessageTypesTable = pd.DataFrame().from_csv('flowTable.csv')
flowMessageTypesTable =flowMessageTypesTable.set_index("type")

#Definicao de versao
defVersion = ["1.0","1.1","1.2","1.3","1.4"]

#print(flowMessageTypesTable)

#Identifica tipo de mensagem
type = flowMessageTypesTable.loc[header['type']][header['version']]

#Identifica versao
version = defVersion[header['version']+1]

#Obtem tamanho do header
length = header['length']


print('Raw package information:')
print('Version: %s' % raw_header[0] )
print('Type: %s' % raw_header[1] )
print('Length: %s' % raw_header[2] + raw_header[3] )
print('xid: %s' % raw_header[4] + raw_header[5] + raw_header[6] + raw_header[7] )


print('Parsed header information:')
print('Version: %s' % version )
print('Type: %s' % type )
print('Length: %s' % length )
print('xid: %s' % raw_header[4] + raw_header[5] + raw_header[6] + raw_header[7] )



