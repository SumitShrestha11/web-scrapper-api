import requests 
import bs4 

class GlobalNews:
	def __init__(self):
		self.title_list = []

	def global_news(self):
		URL = 'https://www.nytimes.com/2020/05/14/world/coronavirus-news.html?type=styln-live-updates&label=global&index=0&action=click&module=Spotlight&pgtype=Homepage'
		
		try:
			response = requests.get(URL)
		except:
			print ('Cannot retrive info from nytimes')

		parsed_response = bs4.BeautifulSoup(response.text,'html.parser')

		titles = parsed_response.find_all('h2')

		for title in titles:
			self.title_list.append(title.text)

		return self.title_list
