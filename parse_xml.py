from bs4 import BeautifulSoup
import requests
import lxml

def parse_xml():
  url = "http://upload.itcollege.ee/~aleksei/test.xml"
  xml_content = requests.get(url).content
  soup = BeautifulSoup(xml_content,'xml')
  titles = soup.find_all('data')
  result = soup.find("data").get_text().strip()

  return result
