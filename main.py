import pandas as pd
import os
import xlrd

# Lista de empresas
from Tools.scripts.dutree import display

empresas = ["ABEV3", "AZUL4", "BTOW3", "B3SA3", "BBSE3", "BRML3", "BBDC4", "BRAP4", "BBAS3", "BRKM5", "BRFS3", "BPAC11", "CRFB3", "CCRO3", "CMIG4", "HGTX3", "CIEL3", "COGN3", "CPLE6", "CSAN3", "CPFE3", "CVCB3", "CYRE3", "ECOR3", "ELET6", "EMBR3", "ENBR3", "ENGI11", "ENEV3", "EGIE3", "EQTL3", "EZTC3", "FLRY3", "GGBR4", "GOAU4", "GOLL4", "NTCO3", "HAPV3", "HYPE3", "IGTA3", "GNDI3", "ITSA4", "ITUB4", "JBSS3", "JHSF3", "KLBN11", "RENT3", "LCAM3", "LAME4", "LREN3", "MGLU3", "MRFG3", "BEEF3", "MRVE3", "MULT3", "PCAR3", "PETR4", "BRDT3", "PRIO3", "QUAL3", "RADL3", "RAIL3", "SBSP3", "SANB11", "CSNA3", "SULA11", "SUZB3", "TAEE11", "VIVT3", "TIMS3", "TOTS3", "UGPA3", "USIM5", "VALE3", "VVAR3", "WEGE3", "YDUQ3"]
# Dicionário
fundamentos = {}
# Lista todos os arquivos de um diretório
arquivos = os.listdir("balancos")
# pegando o nome do índice da empresa
for arquivo in arquivos:
    nome = arquivo[-9:-4]
    if "11" in nome:
        nome = arquivo[-10:-4]
    # Pega somente os nomes que estão na váriável empresa
    if nome in empresas:
        print(nome)

        # pega o balanço daquela empresa
        balanco = pd.read_excel(f'balancos/{arquivo}', sheet_name=0)
        # tratamento na tabela
        # na 1ª coluna colocar o título como nome da empresa
        balanco.iloc[0, 0] = nome
        # pegar 1ª linha e tornar um cabeçalho
        balanco.columns =  balanco.iloc[0] # transforma a linha 0 no nome das colunas
        balanco = balanco[1:] # exclui a linha 0 que agora é o nome das colunas
        # tornar a 1ª coluna no come das linhas
        balanco = balanco.set_index(nome)

        dre = pd.read_excel(f'balancos/{arquivo}', sheet_name=1)
        # tratamento na tabela
        # na 1ª coluna colocar o título como nome da empresa
        dre.iloc[0, 0] = nome
        # pegar 1ª linha e tornar um cabeçalho
        dre.columns = dre.iloc[0]  # transforma a linha 0 no nome das colunas
        dre = dre[1:]  # exclui a linha 0 que agora é o nome das colunas
        # tornar a 1ª coluna no come das linhas
        dre = dre.set_index(nome)

        # adiciona cada empresa no discionário fundamentos
        fundamentos[nome] = balanco.append(dre) # concatena balanco com dre