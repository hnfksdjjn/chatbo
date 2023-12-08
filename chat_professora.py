import random
import webbrowser
import pyttsx3

def start():
    intro_text = '''Olá! Eu sou a professora cleo. Como posso ajudar? Escolha qual é a matéria que você vai estudar:
                   Opções: portugues, matematica, geografia, artes, filosofia, historia e sociologia'''
                 
    speak_text(intro_text)
    return intro_text

def comment_website(website_url):
    # Adicione comentários sobre o site aqui
    if 'eaulas.usp.br' in website_url:
        return "Acesse a plataforma E-Aulas da USP para encontrar conteúdo de Português."
    elif 'somatematica.com.br' in website_url:
        return "Visite Somatemática para recursos educacionais de Matemática."
    elif 'sogeografia.com.br' in website_url:
        return "Explore o site SoGeografia para informações de Geografia."
    elif 'sohistoria.com.br' in website_url:
        return "Confira SoHistória para aprender mais sobre História."
    elif 'blog.stoodi.com.br/artes/' in website_url:
        return "Descubra recursos relacionados a Artes no blog do Stoodi."
    elif 'filosofia.com.br' in website_url:
        return "Aprofunde-se na Filosofia visitando Filosofia.com.br."
    elif 'blog.stoodi.com.br/sociologia/' in website_url:
        return "Encontre conteúdo de Sociologia no blog do Stoodi."

def get_subject_info(subject):
    # Adicione informações sobre a matéria aqui
    subject_info = {
        'portugues': "Português é a disciplina que estuda a língua portuguesa, suas regras gramaticais, literatura e formas de comunicação escrita e oral. O aprendizado de português é essencial para a expressão clara e eficaz em diversos contextos.",
        
        'matematica': "Matemática é a ciência que estuda a lógica dos números, padrões, quantidade, espaço e estrutura. Envolve a resolução de problemas utilizando fórmulas e técnicas matemáticas. Essencial em muitas áreas, a matemática contribui para o desenvolvimento do pensamento lógico e analítico.",
        
        'geografia': "Geografia é a ciência que investiga a superfície terrestre, suas características físicas, climáticas, culturais e as interações entre o homem e o meio ambiente. Estuda a distribuição de recursos e fenômenos geográficos, fornecendo uma compreensão abrangente do mundo.",
        
        'historia': "História é a disciplina que explora e interpreta os acontecimentos passados da humanidade. Examina mudanças sociais, políticas, culturais e econômicas, oferecendo insights valiosos para compreender o presente e moldar o futuro.",
        
        'artes': "Artes engloba diversas formas de expressão artística, incluindo música, pintura, escultura, teatro e dança. Estudar artes permite apreciar e compreender diferentes manifestações culturais, desenvolvendo a criatividade e a sensibilidade estética.",
        
        'filosofia': "Filosofia busca compreender questões fundamentais relacionadas à existência, conhecimento, valores, razão, mente e linguagem. Examina criticamente conceitos e ideias, incentivando o pensamento reflexivo e a busca por significado na vida.",
        
        'sociologia': "Sociologia é a ciência que estuda a sociedade, suas instituições e as relações sociais. Analisa padrões comportamentais, estruturas sociais e questões como classe, gênero e etnia, proporcionando insights sobre a dinâmica social e os desafios contemporâneos."
    }
    return subject_info.get(subject, '')


def handle_text(user_input):
    user_input_lower = user_input.lower()

    if user_input_lower in ['portugues', 'matematica', 'geografia', 'historia', 'artes', 'filosofia', 'sociologia']:
        subject_info = get_subject_info(user_input_lower)
        speak_text(subject_info, gender='male')  # Explicação sobre a matéria
        website_url = get_website_url(user_input_lower)
        comment = comment_website(website_url)
        speak_text(comment, gender='male')  # Escolhe uma voz masculina
        webbrowser.open(website_url)
        speak_text(f"Redirecionando para a plataforma. {comment}", gender='male')
        return f"Redirecionando para {website_url}."
    else:
        return "Desculpe, não entendi. Por favor, escolha uma das opções: portugues, matematica, geografia, artes, filosofia, historia ou sociologia."

def get_website_url(subject):
    # Mapeia a matéria para a URL correspondente
    subject_mapping = {
        'portugues': 'https://eaulas.usp.br/portal/home',
        'matematica': 'https://www.somatematica.com.br/',
        'geografia': 'https://www.sogeografia.com.br/',
        'historia': 'https://www.sohistoria.com.br/',
        'artes': 'https://blog.stoodi.com.br/artes/',
        'filosofia': 'http://www.filosofia.com.br/',
        'sociologia': 'https://blog.stoodi.com.br/sociologia/'
    }
    return subject_mapping.get(subject, '')

def speak_text(text, gender='female'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)

    # Configurações para voz masculina
    if gender == 'male':
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Escolhe uma voz masculina

    engine.say(text)
    engine.runAndWait()

def main():
    print(start())

    while True:
        user_input = input('Você: ')
        if user_input.lower() == 'sair':
           print('Até logo estudante!')
           break

        response = handle_text(user_input)
        print(f'Bot: {response}')

if __name__ == '__main__':
    main()
