#![MongoDB](https://webassets.mongodb.com/_com_assets/cms/MongoDB-Logo-5c3a7405a85675366beb3a5ec4c032348c390b3f142f5e6dddf1d78e2df5cb5c.png  "MongoDB")

Trabalho Prático Utilizando Banco de Dados **MongoDB**

##Os nomes mais populares de PUB

Qual é o pub mais popular no `Reino Unido`?

Este trabalho começa com uma simples pergunta de qual é o pub mais popular no Reino Unido, porém por trás de uma simples pergunta podemos nos deparar com ferramentas e algoritmos poderosos que podem buscar além do nome do Pub mais popular, distância entre os Pubs, Pubs próximo a você, número de toilets e até mesmo o preço da cerveja.

Sabemos que existe uma gama de dados abertos, incluindo várias informações sobre Pubs disponíveis, porém o objetivo desse trabalho é demostrar de forma simples como usar o banco de dados MongoDB e algoritmos de `pipeline` e `mapReduce` para analisarmos uma fonte de dados.

Para esse trabalho foi usado a fonte dados do site ^1^[OpenStreeMap](http://www.openstreetmap.org), no qual pode ser baixado no link [PubsReinoUnido](http://www.overpass-api.de/api/xapi?*[amenity=pub][bbox=-10.5,49.78,1.78,59]). A fonte de dados vem no formato OSM e pode ser facilmente convertida para o formato JSON usando a [biblioteca imposm python](https://imposm.org/).

Uma vez obtido o arquivo, iremos importá-lo como uma coleção para o banco de dados MongoDB

	./bin/mongoimport -d nome_bd_mongo -c pubs ./path/pubs.json

Para processamento das informações foi usado a linguagem de programação `Python 2.7.12` e a biblioteca principal `PyMongo` para conexão com o MongoDB.

####Importando
Para utilizar o PyMongo em um ambiente de desenvolvimento Python é necessário importá-lo como biblioteca.

```python
from pymongo import MongoClient
```


























^1^ *O OpenStreetMap é desenvolvido por uma comunidade voluntária de mapeadores que contribuem e mantêm atualizados os dados sobre estradas, trilhos, cafés, estações ferroviárias e muito mais por todo o mundo. [](http://www.openstreetmap.org) *