import bs4
import requests

resultado = requests.get('https://www.leagueoflegends.com/es-es/news/dev/dev-league-s-business-model-in-2023/')

#bs4(beautifulsoup) sirve para navegar entre todo el codigo y encontrar los elementos que buscamos
#pide dos parametros 1(el string a transformar en elemento bs4)2(motor para hacer el parcing)
beautysoup = bs4.BeautifulSoup(resultado.text, 'lxml')

print(beautysoup.select('title')[0].getText())