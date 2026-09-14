# Exercício de 14/09: consulta de previsão do tempo.
# Para instalar a única biblioteca externa: py -m pip install requests
# Para executar este arquivo: py previsao_tempo_aula.py
 
import requests
from pathlib import Path
import webbrowser
from html import escape  # Permite inserir nomes no HTML como texto seguro.
 
# A API retorna um código para a condição do tempo.
# Este dicionário relaciona cada código à sua descrição em português.
# Documentação: https://open-meteo.com/en/docs
condicoes = {
    0: "Céu limpo",
    1: "Predominantemente limpo",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Nevoeiro",
    48: "Nevoeiro com formação de gelo",
    51: "Garoa leve",
    53: "Garoa moderada",
    55: "Garoa intensa",
    56: "Garoa congelante leve",
    57: "Garoa congelante intensa",
    61: "Chuva leve",
    63: "Chuva moderada",
    65: "Chuva forte",
    66: "Chuva congelante leve",
    67: "Chuva congelante forte",
    71: "Neve leve",
    73: "Neve moderada",
    75: "Neve forte",
    77: "Grãos de neve",
    80: "Pancadas de chuva leves",
    81: "Pancadas de chuva moderadas",
    82: "Pancadas de chuva fortes",
    85: "Pancadas de neve leves",
    86: "Pancadas de neve fortes",
    95: "Trovoadas",
    96: "Trovoadas com granizo leve",
    99: "Trovoadas com granizo forte",
}
 
try:
    # Recebemos a cidade pelo terminal, como no exercício de usuários.
    # Para diferenciar cidades, é possível informar cidade e estado/país.
    cidade_busca = input("Digite a cidade (ex.: São Paulo, Brasil): ").strip().lower()
    for caracter in cidade_busca:
        if caracter.isdigit():
            raise ValueError("O nome não pode conter números")
 
    if len(cidade_busca) < 2:
        raise ValueError("Digite o nome de uma cidade com pelo menos 2 caracteres.")
 
    # Primeiro, buscamos a latitude e a longitude da cidade.
    url_cidade = "https://geocoding-api.open-meteo.com/v1/search"
    parametros_cidade = {
        "name": cidade_busca,
        "count": 1,  # Esta versão utiliza o primeiro resultado da busca.
        "language": "pt",
        "format": "json",
    }
 
    resposta = requests.get(url_cidade, params=parametros_cidade, timeout=15)
    resposta.raise_for_status()
    dados_cidade = resposta.json()
 
    # O campo results contém uma LISTA de localidades.
    cidades = dados_cidade.get("results", [])
 
    if not cidades:
        raise ValueError("Cidade não encontrada. Confira o nome e tente novamente.")
 
    cidade = cidades[0]
    nome_cidade = cidade["name"]
    estado = cidade.get("admin1", "")
    pais = cidade.get("country", "")
    latitude = cidade["latitude"]
    longitude = cidade["longitude"]
 
    print(f"\nLocal encontrado: {nome_cidade} — {estado} — {pais}")
 
    # Agora consultamos a API de clima usando as coordenadas encontradas.
    url_tempo = "https://api.open-meteo.com/v1/forecast"
    parametros_tempo = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,weather_code",
        "daily": "temperature_2m_min,temperature_2m_max,weather_code",
        "temperature_unit": "celsius",
        "timezone": "auto",  # Horário local da cidade consultada.
        "forecast_days": 6,  # Hoje e mais cinco dias.
    }
 
    resposta = requests.get(url_tempo, params=parametros_tempo, timeout=15)
    resposta.raise_for_status()
    dados_tempo = resposta.json()
 
    # Acessamos os dados atuais pelas chaves do dicionário.
    atual = dados_tempo["current"]
    temperatura = atual["temperature_2m"]
    sensacao = atual["apparent_temperature"]
    umidade = atual["relative_humidity_2m"]
    condicao = condicoes.get(atual["weather_code"], "Condição não informada")
 
    # None corresponde a um valor null na resposta JSON da API.
    # O número zero continua sendo um valor válido.
    if temperatura is None or sensacao is None or umidade is None:
        raise ValueError("A API não disponibilizou todas as condições atuais.")
 
    # Criamos uma LISTA para armazenar a previsão dos próximos dias.
    previsoes = []
    diario = dados_tempo["daily"]
 
    # O índice 0 é hoje. range(1, 6) percorre os índices de 1 a 5.
    for indice in range(1, 6):
        data = diario["time"][indice]
        minima = diario["temperature_2m_min"][indice]
        maxima = diario["temperature_2m_max"][indice]
        condicao_dia = condicoes.get(
            diario["weather_code"][indice], "Condição não informada"
        )
 
        # A TUPLA agrupa os quatro dados relacionados a um mesmo dia.
        previsao_dia = (data, minima, maxima, condicao_dia)
 
        # Adicionamos essa tupla à LISTA de previsões.
        previsoes.append(previsao_dia)
 
    # Criamos a estrutura inicial do HTML em uma string.
    html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Previsão do tempo</title>
</head>
<body>
    <h1>Previsão do tempo</h1>
    <h2>{escape(nome_cidade)}</h2>
    <p><strong>Estado:</strong> {escape(estado)}</p>
    <p><strong>País:</strong> {escape(pais)}</p>
    <hr>
 
    <h2>Tempo atual</h2>
    <p><strong>Temperatura atual:</strong> {temperatura} °C</p>
    <p><strong>Sensação térmica:</strong> {sensacao} °C</p>
    <p><strong>Umidade:</strong> {umidade}%</p>
    <p><strong>Condição do tempo:</strong> {condicao}</p>
    <hr>
 
    <h2>Previsão para os próximos 5 dias</h2>
"""
 
    # Percorremos a lista e desempacotamos os quatro valores de cada tupla.
    for data, minima, maxima, condicao_dia in previsoes:
        # Transformamos a data de AAAA-MM-DD para DD/MM/AAAA.
        ano, mes, dia = data.split("-")
        data_formatada = f"{dia}/{mes}/{ano}"
 
        minima_texto = "Indisponível" if minima is None else f"{minima} °C"
        maxima_texto = "Indisponível" if maxima is None else f"{maxima} °C"
 
        # Acrescentamos um bloco HTML para cada dia usando +=.
        html += f"""
    <div>
        <h3>{data_formatada}</h3>
        <p><strong>Temperatura mínima:</strong> {minima_texto}</p>
        <p><strong>Temperatura máxima:</strong> {maxima_texto}</p>
        <p><strong>Condição do tempo:</strong> {condicao_dia}</p>
    </div>
    <hr>
"""
 
    # Finalizamos a página e identificamos as fontes dos dados.
    html += """
    <p>Dados meteorológicos: <a href="https://open-meteo.com/">Open-Meteo</a>.</p>
    <p>Localizações: <a href="https://www.geonames.org/">GeoNames</a>.</p>
    <p>As condições atuais são estimativas de modelos meteorológicos.</p>
    <p>Para consultar outra cidade ou atualizar os dados, execute o programa novamente.</p>
</body>
</html>
"""
 
    # Gravamos o HTML na pasta em que o programa foi executado.
    with open("previsao_tempo.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(html)
 
    # Obtemos o caminho completo e o transformamos em um endereço de arquivo.
    arquivo_path = Path("previsao_tempo.html").resolve()
    endereco_arquivo = arquivo_path.as_uri()
 
    print(f"\nPágina criada com sucesso: {arquivo_path}")
    if webbrowser.open(endereco_arquivo):
        print("Abrindo página no navegador...")
    else:
        print("Abra o arquivo previsao_tempo.html manualmente no navegador.")
 
# Timeout vem antes de ConnectionError porque um timeout de conexão
# pode pertencer às duas categorias.
except requests.exceptions.Timeout:
    print("\nERRO DE TIMEOUT: a consulta demorou. Tente novamente.")
 
except requests.exceptions.ConnectionError:
    print("\nERRO DE CONEXÃO: verifique sua internet e tente novamente.")
 
except requests.exceptions.HTTPError as erro:
    print("\nERRO HTTP:", erro)
 
except KeyError as erro:
    print("\nERRO DE CHAVE: campo não encontrado na resposta:", erro)
 
except IndexError:
    print("\nDADOS INCOMPLETOS: a API não retornou todos os dias da previsão.")
 
except ValueError as erro:
    print("\nERRO NOS DADOS:", erro)
 
except requests.exceptions.RequestException as erro:
    print("\nERRO NA CONSULTA:", erro)
 
except OSError as erro:
    print("\nERRO DE ARQUIVO OU NAVEGADOR:", erro)
 
except webbrowser.Error as erro:
    print("\nNão foi possível abrir o navegador:", erro)
    print("Abra o arquivo previsao_tempo.html manualmente.")