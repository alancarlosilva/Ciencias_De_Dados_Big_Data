#![ ](https://i.ytimg.com/vi/cqqXlu-DB4k/hqdefault.jpg  "FinalMineiro")

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

![ ](/home/alan/Imagens/RI_Trabalho/Knime_Twitter.png  "Knime_Twitter")


Nessa etapa, o nó `Twitter Streaming` recebe os twitters de Cruzeiro e Atlético em tempo real para análise.

![ ](/home/alan/Imagens/RI_Trabalho/Config_twitter_streaming.png  "Twitter_Config")

