# chatbo
2 chatbot uma analista esportiva e uma professora com python

# chat.professora

Este código Python implementa um assistente educacional que fornece informações sobre diferentes disciplinas escolares.

1. **Função `start`:** A função inicializa o assistente educacional, saúda o usuário e fornece opções de disciplinas para estudar.

2. **Função `comment_website`:** Fornece comentários específicos sobre diferentes sites relacionados a cada disciplina.

3. **Função `get_subject_info`:** Retorna informações sobre uma disciplina específica, explicando seu escopo e importância.

4. **Função `handle_text`:** Analisa a entrada do usuário e executa ações com base na disciplina escolhida. Abre um site relacionado à disciplina e fornece informações sobre ela.

5. **Função `get_website_url`:** Mapeia disciplinas para URLs correspondentes, permitindo o redirecionamento para sites específicos de aprendizado.

6. **Função `speak_text`:** Utiliza a biblioteca `pyttsx3` para sintetizar e falar um texto em voz alta, permitindo personalização de gênero da voz.

7. **Função `main`:** Função principal que inicia o assistente, exibe a saudação inicial e entra em um loop de interação com o usuário.

8. **Laço Principal:** O loop permite que o usuário faça escolhas e receba informações sobre diferentes disciplinas até decidir sair digitando "sair".

9. **Encerramento:** Quando o usuário decide sair, uma mensagem de despedida é exibida, encerrando a execução do programa.

10. **Execução Inicial:** Verifica se o script está sendo executado diretamente (`__name__ == '__main__'`) e, nesse caso, chama a função `main()`.

# chatbot.simples

Este código Python implementa um assistente de análise esportiva chamado "cleo". 

1. **Importações:** O código importa módulos como `random`, `datetime`, `webbrowser`, `BeautifulSoup` e outros para funcionalidades como geração aleatória, manipulação de datas, abertura de URLs no navegador, análise HTML, requisições web e manipulação de dados tabulares.

2. **Obter Resultados de Futebol:** A função `obter_resultados_futebol` faz uma requisição a um site de placar de futebol, extrai informações sobre jogos e cria um DataFrame com pandas.

3. **Exibir Resultados e Notícias:** As funções `exibir_resultados` e `exibir_noticias` apresentam informações sobre resultados de jogos e notícias esportivas, respectivamente.

4. **Notícias Cam Estaduais:** A função `noticias_cam_estaduais` fornece uma mensagem específica se a URL fornecida for relacionada a aulas da USP.

5. **Verificar Palavras:** A função `verificar_palavras` compara palavras-chave com o texto do usuário, identifica incorreções e sugere correções.

6. **Iniciar e Manipular Texto:** A função `start` retorna uma saudação inicial, e `handle_text` processa as entradas do usuário, respondendo a solicitações como criar texto, fornecer a hora, data, acessar sites, mostrar resultados de jogos e notícias esportivas.

7. **Loop Principal:** O programa entra em um loop interativo onde o usuário pode interagir até decidir sair digitando "sair".

8. **Encerramento:** Quando o usuário decide sair, uma mensagem de despedida é exibida, encerrando a execução do programa.

# chat_analista

Este código Python é um assistente de voz que fornece informações sobre resultados de jogos de futebol, notícias esportivas e interage com o usuário para realizar ações específicas.

1. **Importação de Bibliotecas:** O código começa importando várias bibliotecas, incluindo `random`, `pyttsx3` para síntese de voz, `datetime` para manipulação de datas, `webbrowser` para abrir páginas da web, `BeautifulSoup` para análise HTML e `pandas` para manipulação de dados.

2. **Função `obter_resultados_futebol`:** Essa função faz uma solicitação HTTP para o site "https://www.placardefutebol.com.br/" e usa BeautifulSoup para extrair informações sobre os resultados dos jogos de futebol. Os dados são organizados em um DataFrame usando a biblioteca `pandas`.

3. **Função `falar_resultados`:** Utiliza a função anterior para obter os resultados e utiliza a biblioteca `pyttsx3` para falar os resultados em voz alta.

4. **Função `obter_noticias_esportivas`:** Essa função obtém as últimas notícias esportivas do site "https://www.uol.com.br/esporte/noticias/" usando BeautifulSoup.

5. **Função `falar_noticias`:** Obtém as notícias e usa `pyttsx3` para falar as notícias em voz alta.

6. **Função `noticias_cam_estaduais`:** Retorna uma mensagem específica se a URL fornecida contiver "eaulas.usp.br".

7. **Função `verificar_palavras`:** Verifica palavras-chave em um texto fornecido e fornece sugestões de correção para palavras incorretas.

8. **Função `start`:** Retorna uma mensagem de boas-vindas.

9. **Função `handle_text`:** Analisa a entrada do usuário e executa ações com base em comandos específicos, como verificar palavras, fornecer a hora, data, acessar sites, exibir resultados de jogos ou notícias.

10. **Função `speak`:** Usa a biblioteca `pyttsx3` para falar uma mensagem em voz alta.

11. **Função `main`:** É a função principal que inicia o assistente de voz. Ela inicia a interação com o usuário, processa os comandos e responde usando a voz sintetizada.

12. **Laço Principal:** Um loop `while` mantém a interação contínua com o usuário até que a palavra "sair" seja digitada.

13. **Encerramento:** Quando o usuário decide sair, a mensagem de despedida é falada e a execução do programa é encerrada.

14. **Execução Inicial:** A última parte do código verifica se o script está sendo executado diretamente (`__name__ == '__main__'`) e, nesse caso, chama a função `main()`.

15. **Interação com o Usuário:** Durante a execução, o usuário pode fazer perguntas, obter resultados de jogos, notícias e realizar ações específicas, todas respondidas de forma interativa.
