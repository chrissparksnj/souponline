import json
from bs4 import BeautifulSoup
import requests


class req_class():

    def __init__(self, jsons):
        ''' take in a json post request and dynamically assign object properties '''
        for key, val in jsons.items():
            self.__setattr__(key, val)

        ''' self.url will always be in POST request so just set it up here '''
        self.request = requests.get(self.url)
        self.soup =  BeautifulSoup(self.request.text, "html.parser")

    def get_vars(self):
        ''' get all object variables and return only True ones '''
        varss =  vars(self)
        return {k:v for (k,v) in varss.items() if v == True}

    def parse_tags(self):
        items_to_get = self.get_vars()
        payload = {} # final payload that will be returned
        for itm in items_to_get:
            if itm == "links":
                resultset = self.soup.find_all("a")
                parsed_links = self.parse_links(resultset)
                payload["links"] = parsed_links
            if itm == "text":
                parsed_text = self.parse_text()
                payload["text"] = parsed_text
            if itm == "images":
                resultset = self.soup.findAll("img")
                images = self.parse_images(resultset)
                payload["images"] = images
        return payload

    def parse_images(self, resultset):
        image_dict = {}
        count = 0
        for img in resultset:
            count = count + 1
            # get the first tag name in the images attributes. 
            # helps differentiates between img.get("src") and img.get("data-src")
            src = next(iter(img.attrs))
            image_dict["image_link_" + str(count)] = img.get(src)
        return image_dict
    
    def parse_links(self, resultset):
        link_dict = {}
        for i in resultset:
            if len(i.get_text().strip()) != 0:
                anchor_text = i.get_text().strip()
                href =  self.url + i.get('href')
                link_dict[anchor_text] = href
        return link_dict


    def parse_text(self):
        text_dict = {}
        count = 0
        texts = self.soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)
        for txt in visible_texts:
            if len(txt) == 1:
                pass
            else:
                count = count + 1
                text_dict["text_" + str(count)] = txt.strip()
        return text_dict


    # these to functions are from GOD tier stackoverflow: https://stackoverflow.com/a/1983219/6536037
    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        return True






