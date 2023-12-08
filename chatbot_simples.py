import random
from datetime import datetime
import webbrowser
from resposta import obter_frase_aleatoria, obter_correcoes, obter_palavras_chave
from bs4 import BeautifulSoup
import requests
import pandas as pd

def obter_resultados_futebol():
    pagina = requests.get("https://www.placardefutebol.com.br/")
    site = BeautifulSoup(pagina.content, 'html.parser')

    notici = site.find_all('div', attrs={'class': 'w-25 p-2 team-name'})
    casa_1 = []

    for h3 in notici:
        texto_link = h3.text.strip()
        if texto_link:
            casa_1.append(texto_link)

    resultado = site.find_all('div', attrs={'class': 'w-25 p-1 match-score d-flex justify-content-end'})

    contaçao = site.find_all('span', attrs={'class': 'badge badge-default'})

    resulta = contaçao[0:16:2]
    resultado_1 = []

    for span in resulta:
        texto_link = span.text.strip()
        if texto_link:
            resultado_1.append(texto_link)

    resulta_2 = contaçao[1:16:2]

    resultado = []

    for span in resulta_2:
        texto_link = span.text.strip()
        if texto_link:
            resultado.append(texto_link)

    casa_h = casa_1[0:16:2]

    vizitante = casa_1[1:16:2]

    dados_iteracao = pd.DataFrame({
        'casa': casa_h,
        'placa_c': resultado_1,
        'placa_v': resultado,
        'vizitante': vizitante
    })

    return dados_iteracao

def exibir_resultados():
    dados = obter_resultados_futebol()

    for index, row in dados.iterrows():
        mensagem = f"{row['casa']} {row['placa_c']} x {row['placa_v']} {row['vizitante']}"
        print(mensagem)

def obter_noticias_esportivas():
    # URL da página de esportes do UOL
    url = "https://www.uol.com.br/esporte/noticias/"

    # Realiza a requisição à página
    pagina = requests.get(url)

    # Cria o objeto BeautifulSoup
    site = BeautifulSoup(pagina.content, 'html.parser')

    # Encontra todas as notícias esportivas na página
    noticias = site.find_all('div', attrs={'class': 'thumb-caption col-xs-5 col-sm-18 no-gutter'})

    # Lista para armazenar as notícias
    lista_noticias = []

    for noticia in noticias:
        texto_noticia = noticia.text.strip()
        if texto_noticia:
            lista_noticias.append(texto_noticia)

    # Retorna as 10 primeiras notícias (ou menos, se não houver 10)
    return lista_noticias[:10]

def exibir_noticias():
    noticias = obter_noticias_esportivas()

    for i, noticia in enumerate(noticias, start=1):
        mensagem = f"{i}. {noticia}"
        print(mensagem)

def noticias_cam_estaduais(website_url):
    if 'eaulas.usp.br' in website_url:
        return "Acesse a plataforma E-Aulas da USP para encontrar conteúdo de Português."

def verificar_palavras(texto, palavras_chave, correcoes):
    palavras_texto = set(texto.lower().split())
    palavras_chave = set(palavras_chave)

    palavras_incorretas = palavras_texto - palavras_chave

    if not palavras_incorretas:
        return "As palavras estão corretas!"
    else:
        sugestoes_correcao = {palavra: correcoes.get(palavra, "Nenhuma sugestão disponível") for palavra in
                              palavras_incorretas}
        return f"Palavras incorretas: {', '.join(palavras_incorretas)}\nSugestões de correção: {sugestoes_correcao}"

def start():
    return 'Olá! Eu sou a analista esportiva cleo, escolha uma opção?'

def handle_text(user_input, correcoes):
    # Adiciona uma resposta sobre criar textos
    if 'criar texto' in user_input.lower():
        texto_usuario = input("Digite o texto que você criou: ")

        # Lista de palavras-chave que você deseja verificar no texto
        palavras_chave = obter_palavras_chave()

        correcoes = obter_correcoes()

        resultado = verificar_palavras(texto_usuario, palavras_chave, correcoes)

        return resultado

    # Adiciona uma resposta sobre as horas
    if 'que horas sao' in user_input.lower():
        current_time = datetime.now().strftime("%H:%M")
        return f"Agora são {current_time}."

    # Adiciona uma resposta sobre a data
    elif 'hoje e que dia' in user_input.lower():
        current_date = datetime.now().strftime("%d/%m/%Y")
        return f"Hoje é {current_date}."

    # Adiciona uma resposta sobre acessar um site
    elif 'acessar site' in user_input.lower():
        try:
            # Solicita a URL ao usuário
            url = input('Informe a URL do site: ')

            # Abre o site no navegador padrão
            webbrowser.open(url)

            return "Site aberto no navegador."

        except Exception as e:
            return f"Ocorreu um erro ao acessar o site: {str(e)}"

    elif 'resultados de jogos' in user_input.lower():
        exibir_resultados()
        return "Exibindo os resultados dos jogos em tempo real."

    elif 'noticias esportivas' in user_input.lower():
        exibir_noticias()
        return f"Notícias Esportivas:"

    elif 'noticias_cam_estaduais' in user_input.lower():
        website_url = 'https://www.terra.com.br/esportes/futebol/estaduais/'
        print(noticias_cam_estaduais(website_url))
        webbrowser.open(website_url)
        return f"Redirecionando para {website_url}."

    # Retorna uma frase aleatória da lista
    return obter_frase_aleatoria()

def main():
    correcoes = obter_correcoes()

    print(start())

    while True:
        user_input = input('Você: ')

        if user_input.lower() == 'sair':
            print('tchau e Até logo!')
            return "tchau e Até logo!"

        response = handle_text(user_input, correcoes)
        print('cleo:', response)

if __name__ == '__main__':
    main()
