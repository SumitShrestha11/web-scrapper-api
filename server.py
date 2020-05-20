from flask import Flask
from flask_cors import CORS
import json

from classes.newyorktimes import GlobalNews
from classes.myrepublica import *

app=Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "This is working!"

@app.route("/news", methods=['GET'])
def news():
	return (json.dumps(all_news),200,{'content-type': 'application/json'})


if __name__=='__main__':
	global_news = GlobalNews().global_news()
	local_news = NagarikNews().local_news()
	political_news = NagarikNews().political_news()
	# All these are of return type; list
	all_news = {
		"global_news":global_news,
		"local_news":local_news,
		"political_news":political_news
	}
	
	# print (f'{global_news} \n {local_news} \n {political_news}')
	#print(all_news)

	app.run(debug=True)
    

