import requests
import random
import config

class Quotes:
    def __init__(self) -> None:
        self.quotes = {}
        self.consumeAPI()

    def consumeAPI(self):
        print('Creating quotes...')
        api_url = config.quotesAPI
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            self.quotes = response.json()
        else:
            self.quotes = None
            print('API ERROR')

    def getQuote(self):
        select = random.randint(1,len(self.quotes)-1)
        quote = "\""+self.quotes[select]['text']+"\""+"\n-"+self.quotes[select]['author']
        return quote