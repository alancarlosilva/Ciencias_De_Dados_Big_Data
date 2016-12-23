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
####Criando uma conexão
```python

client = pymongo.MongoClient()

##nome do banco de dados
db = client.bd_nosql 

##nome da coleção
collection = db.pubs
```

####Testando a conexão
Para verificarmos uma conexão simples e se a mesma traz algum resultado podemos executar o código abaixo:

```python
myQuery = db.pubs.find({})

for documento in myQuery:
	print(documento)
```
>Essa operação irá trazer uma query dos pubs existentes na coleção pubs, também poderíamos ter usado a biblioteca pprint para imprimir a query em formato JSON

###Algoritmos de agregação
Existem vários modos agregação no MongoDB, nesse trabalho serão demostrados as técnicas de pipeline e map reduce para verificarmos os termos mais frequentes, nesse caso os pubs mais populares.

**MapReduce**: Modelo para processar um grande volume de dados, dividindo o trabalho em um conjunto de tarefas. Nesse modelo definimos as funções map e reduce para contar o número de ocorrências de cada nome na matriz de nomes, atráves de toda a coleção.

**MapReduce em Python**
```python
#Função de mapeamento de dados, retornando chaves de valores
mapper = Code("""
				function(){
					emit(this.name, 1);
				};
			""")
#Função reduce para percorrer os valores que estão associados com a chave(mapper)
reducer = Code("""
				function(key, values){
					var total = 0;
					for (var i = 0; i < values.length; i++){
						total += values[i];
					}
					return total;
				}
			""")
```
**Imprimindo o resultado**
```python
#A query usado nessa parte retorna apenas os 5 pubs mais populares da fonte de dados utilizado
result_pubs = db.pubs.map_reduce(mapper, reducer, "result", query={"name": {"$lt":5}})
for document in result_pubs.find():
	pprint.pprint(document)
```
**Pipeline**: O modelo Pipeline utiliza múltiplos estágios para transformação e processamento de documentos, são eles, unwind da matriz de nomes, agrupamento e classificação por contagem. Nesse exemplo executamos uma agregação simples para contar o número de ocorrência de cada nome de pub na matriz de nomes em toda a coleção.

**Pipeline em Python**

```python
pipeline = [
	#Aqui fazemos o agrupamento de documentos pelo name e somamos 1 para cada nome igual encontrado
	{"$group": {"_id": "$name", "value": {"$sum": 1}}},
  	
  	#Ordenamos o pipeline anterior  	
  	{"$sort": {"value": -1}},

  	#Limitamos a pesquisa de pubs em 5
  	{"$limit": 5}
]
```
**Imprimindo o resultado**
```python
pprint.pprint(list(db.pubs.aggregate(pipeline)))
```

##TOP 5 - Pubs

Usando as técnicas de agregação é muito simples encontrar os nomes mais populares, bastando apenas agrupar pelo nome e depois resumir todas as ocorrências. Nesse exemplo os nomes foram classificados pelo valor somado e depois limitado as 5 maiores ocorrências:

+ 1 - Red Lion
+ 2 - Royal Oak
+ 3 - New Inn
+ 4 - White Hart
+ 5 - Crown

>**Curiosidade**: Tanto o método de pipeline quanto o de mapReduce levaram em média 0.9 segundos para serem executados.

###Considerações finais
Apesar da curva de aprendizado do MongoDB ser um pouco longa, pode se dizer que esse tipo de banco de dados é bastante útil para armazenar dados coletados na web, como por exemplo, as redes sociais e dados geolocalizados. Ele elimina a necessidade de escrever uma analisador, uma vez que você analisa os dados em tempo real. Conhecer a estrutura dos subdocumentos dos documentos nesse banco de dados nos ajuda melhor entender a programaçaõ para executar análises em Python(Ou outra linguagem de fácil conexão com o Mongo) usando MongoDB.





