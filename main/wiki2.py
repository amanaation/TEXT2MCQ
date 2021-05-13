import re
import requests
import unidecode

class chatbot():
    def __init__(self, question, url_given = False):
        pass

        if not url_given:
            url = "https://google.com/search?q=" + question
        else:
            url = "https://google.com" + question
        self.question = question

        headers = {
            'authority': url,
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/application/json/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Content-Type': 'application/json'
        }

        response = requests.get( url, headers=headers)
        self.response = unidecode.unidecode(response.text)
        self.response = self.response.replace("\n","")

    def get_related_names(self):
        #if "People also search for" in response:
        ind = self.response.index("People also search for")
        text = self.response[ind:]
        return re.findall('<div class="fl ellip oBrLN S1gFKb rOVRL" data-original-name="(.*?)">', text)
