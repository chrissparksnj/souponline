import json
from bs4 import BeautifulSoup
import requests


class req_class():

    def __init__(self, jsons):
        for key, val in jsons.items():
            self.__setattr__(key, val)
        self.lookup_table = {"links":"a", "images":"img", "text":"p"}
        self.request = requests.get(self.url)
        self.soup =  BeautifulSoup(self.request.text, "html.parser")

    def get_url(self):
        return self.url

    def get_vars(self):
        varss =  vars(self)
        return {k:v for (k,v) in varss.items() if v == True}

    def return_tags(self):
        tags = []
        varss = self.get_vars()
        
        for key in varss:
            if key in self.lookup_table:
                tags.append(self.lookup_table[key])
        return tags

    def parse_tags(self):
        tags = self.return_tags()
        payload = {}
        for tag in tags:
            if tag == "a":
                resultset = self.soup.find_all(tag)
                parsed_links = self.parse_links(resultset)
                payload["links"] = parsed_links
            if tag == "p":
                parsed_text = self.text_from_html()
                payload["text"] = parsed_text
            if tag == "img":
                resultset = self.soup.findAll(tag)
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

    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        return True

    def text_from_html(self):
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
        return "".join(t.strip() for t in visible_texts)

    def parse_links(self, resultset):
        link_dict = {}
        for i in resultset:
            if len(i.get_text().strip()) != 0:
                anchor_text = i.get_text().strip()
                href =  self.url + i.get('href')
                link_dict[anchor_text] = href
        return link_dict


