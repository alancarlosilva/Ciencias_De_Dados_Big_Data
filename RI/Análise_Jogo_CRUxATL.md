#![ ](http://aovivonatv.com/fotos/f230826991ea0f5d76ad12ead4f2f0a0.jpg "FinalMineiro")

**A final mineira entre Cruzeiro X Atlético - MG**

A partida entre Atlético - MG e Cruzeiro, realizada no Independência no dia 07 de Maio de 2017, valia o título estadual, mas esse clássico ganha contornos decisivos extra campos, por se tratar dos grandes times de Minas e considerado por muitos torcedores um dos grandes clássicos mundiais, o duelo entre esses gigantes mineiros tem grandes aspectos de rivalidade e contudo esse artigo tem o intuito de mostrar o infográfico da decisão mineira coletada através de twitters durante e depois da partida.

O resultado final de 2x1 para o time da casa (Atlético - MG) agitou a torcida presente no Independência e também a torcida presente nas redes sociais. O que os torcedores de Cruzeiro e Atlético - MG falaram sobre o jogo, você confere abaixo.
***

**Pré-requisitos**

Os exemplos e desenvolvimento desse trabalho utilizam o software Knime Analytics que pode ser baixado nesse [link](https://www.knime.org/downloads/overview).

***
**KNIME**

Para chegar ao resultado desejado, vamos utilizar o sotware de mineração de dados KNIME do qual é a principal solução aberta projetada para descobrir o potencial poder dos dados gerando insights e fazendo análises preditivas. O Knime foi construído há mais de uma década para acessar dados de forma intuitiva e interativa a fim de ajudar a comunidade de cientistas, analistas e engenheiro de dados.

***
**Obtendo Twitters**

A fonte de dados utilizada é o site https://twitter.com/, e será acessado pelo `Twitter API Connector`

![ ](https://github.com/alancarlosilva/Ciencias_De_Dados_Big_Data/blob/master/RI/RI_Trabalho/Knime_Twitter.png  "Twitter_API")

Nessa etapa, o nó `Twitter Streaming` recebe os twitters de Cruzeiro e Atlético em tempo real para análise.

![ ](https://github.com/alancarlosilva/Ciencias_De_Dados_Big_Data/blob/master/RI/RI_Trabalho/Config_twitter_streaming.png  "Twitter_Config")
***
**Criando Banco de Dados Local**

Após coleta dos twitters, foi criado um banco de dado local utilizando nó `Database Writer` e `SQLite Connector`. Obs.: Com um banco de dado local a consulta dos dados ficam mais eficientes.

![ ](https://github.com/alancarlosilva/Ciencias_De_Dados_Big_Data/blob/master/RI/RI_Trabalho/twitter_bd.png  "twitter_bd")

**Processando os dados**

Para o processamento e tratamento de textos, iremos usar o termos mais frequentes e exibí-los em uma Cloud Tag. Neste processo, o nó `Ponctuation Erasure` remove todos os caracteres de pontuação dos termos contidos em todos os documentos (linhas obtidas de cada twitter). O `Stop Word Filter` é o responsável por remover todos os termos do documento de entrada que correspondem com termos de uma lista (biblioteca de termos, preposições por exemplo). Com o `N Chars Filter`, foi excluído todos os termos abaixo de 10 caracteres da análise. O `Case Converter` transformou todos os termos em minúsculo. Por fim, o `Bag of Words Creator` separa em linhas cada um dos termos para a devida ação do nó `TF`.

**Cloud Tag**

![ ](https://github.com/alancarlosilva/Ciencias_De_Dados_Big_Data/blob/master/RI/RI_Trabalho/twitter_2.png "twitter_cloud_tag")

**Evolução de posts - twitters**

Para o processamento da evolução dos posts, foi extraído a coluna `time`e exportado para um documento `.csv` do qual foi feito uma estatística de frequência dos horários de posts durante o jogo.

O software utilizado para análise e visualização dos dados aqui foram o Excel e Power BI.

![ ]( https://github.com/alancarlosilva/Ciencias_De_Dados_Big_Data/blob/master/RI/RI_Trabalho/coluna_time.PNG "twitter_coluna")

Por fim, após processamento da frequência de horário, temos o gráfico de histograma abaixo:

![ ](https://github.com/alancarlosilva/Ciencias_De_Dados_Big_Data/blob/master/RI/RI_Trabalho/evolucao_posts_twitter.png "twitter_evolucao")

Podemos observar nesse gráfico a evolução de postagens por minuto, do qual ilustra com precisão o comportamento da torcida. Aos 12 minutos da etapa inicial, o primeiro gol do Atlético - MG marcado por Robinho fez a festa no estádio e também no twitter, foram mais de 800 posts por minuto após o gol anotado pelo atacante. A explosão veio após os 24 minutos da etapa final quando o Atlético - MG marcou o segundo gol atingindo novamente mais de 800 posts por minuto.

Abaixo podemos ver o número de posts durante o pico de twitters.

![ ](https://github.com/alancarlosilva/Ciencias_De_Dados_Big_Data/blob/master/RI/RI_Trabalho/evolucao.PNG "evolucao")
