#1 -Define the map function to process each input document

var map = function(){

	#In the function, this refers to the document that map-reduce
	#The function maps the last 2 words to the text for each document and emits the last 2 words and text pair

	emit(this.text.substring(this.text.length-2, this.text.length),1);
}

#2 - Define the corresponding reduce function with two arguments KeyText and valuesText

var reduce = function(keyText, valuesText){
	#The valuesText is an array whose elements are the Text values emitted by the map function and grouped by keyText
	return Array.sum(valuesText);
}

#3 - Perform the map-reduce on all documents in the Vocabulary collection using the map map function and the reduce reduce function

db.Vocabulary.mapReduce(
		map,
		reduce,
		{
			query: { text: {$in: [/((ar)|(er)|(ir)|(or)|(ur))$/]}},
			out: "resultado"
		}
) 

