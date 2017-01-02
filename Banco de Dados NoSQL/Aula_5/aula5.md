##Aula 5

###Exercício 1
Você e um grupo de amigos da faculdade decidem-se juntar e criar uma empresa de na área de IoT. Todos seus amigos são excelentes programadores porém estão em dúvida como montar a infraestrutura para suportar a grande quantidade de dados gerados pelos sensores da aplicação. O que vocês devem fazer?

>Para casos de IoT, podemos descrever que esse tipo de tecnologia precisa de streaming de alta resiliência, onde há um grande fluxo contínuo de informação, para esse caso iremo precisar de um sistema de filas para armazenamento de dados, entre os principais sistemas de filas podemos descrever o Kafka e RabbitMQ. Como os dados são contínuos pode-se observar que o volume de dados será grande então se faz necessário o uso de um SGDB NoSQL, para o caso IoT os bancos que são do tipo AP(Availability-Partition Tolerance) são os melhores descritos para tal tecnologia.

###Exercício 2
 Dentro de sua empresa certamente existem pontos que podem ser adaptados para uma arquitetura Big Data. Explique a infraestrutura atual e o que você mudaria para melhorar a eficiência.
 
 >Atualmente, usando um modelo simples, podemos descrever o sistema RFID que será implantado para gerenciar coletas e amostragens de minerio de ferro, como um sistema RFID pode se expandir, podemos tratar a tecnologia como um IoT que nesse caso como descrito no exercício anterior, podemos usar sistemas de filas para armazenamento contínuo de informações e um SGDB NoSQL.
 

