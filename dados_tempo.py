import pyinputplus as pyip
import pandas as pd

def obter_nome_mes(numero_mes):
    """
    Retorna o nome do mês por extenso com base no número do mês.

    Args:
        numero_mes (int): O número do mês (1 a 12).

    Returns:
        str: O nome do mês por extenso ou None se o número do mês for inválido.
    """
    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
    }

    return meses.get(numero_mes)

def obter_dados_meteorologicos():
    """
    Coleta dados meteorológicos do usuário para cada mês do ano.

    Retorna:
        pandas.DataFrame: DataFrame com os dados de mês e temperatura máxima.
    """
    
    print("Intervalo válido para temperatura: -60 a +50 graus Celsius, tipo `float` com separador decimal ponto (.).")
    print("Ex.: 37.1, -20.5, 10, 10.0, -10.0000, 1.000159\n")
    dados = {'Mês': [], 'Temperatura Máxima': []}
    for mes in range(1, 13):
        temperatura = pyip.inputFloat(
            prompt=f"Digite a temperatura máxima para o mês {obter_nome_mes(mes)} em Celsius: ",
            min=-60,
            max=50
        )
        dados['Mês'].append(mes)
        dados['Temperatura Máxima'].append(temperatura)
    return pd.DataFrame(dados)

def calcular_estatisticas(df):
    """
    Calcula e exibe estatísticas meteorológicas com base nos dados fornecidos.

    Args:
        pandas.DataFrame: DataFrame com dados de mês e temperatura máxima.
    """
    temp_media_anual = df['Temperatura Máxima'].mean()
    meses_escaldantes = df[df['Temperatura Máxima'] > 33]
    mes_mais_quente = df.loc[df['Temperatura Máxima'].idxmax()]
    mes_menos_quente = df.loc[df['Temperatura Máxima'].idxmin()]

    print(f"\nTemperatura Média Máxima Anual: {temp_media_anual:.2f} °C")
    print(f"Quantidade de Meses Escaldantes: {len(meses_escaldantes)}")
    print(f"Mês Mais Quente: {obter_nome_mes(mes_mais_quente['Mês'])} ({mes_mais_quente['Temperatura Máxima']:.2f} °C)")
    print(f"Mês Menos Quente: {obter_nome_mes(mes_menos_quente['Mês'])} ({mes_menos_quente['Temperatura Máxima']:.2f} °C)")

# Coleta e valida os dados meteorológicos do usuário
df_dados = obter_dados_meteorologicos()

# Calcula e exibe as estatísticas
calcular_estatisticas(df_dados)