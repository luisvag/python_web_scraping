import bs4
import requests

"""PROGRAMA PARA EXTRAER TITULOS DE LIBROS DE 4 O 5 ESTRELLAS DE TOSCRAPE"""

#url sin nro de pag
url_principal = 'https://books.toscrape.com/catalogue/page-{}.html'

#lista de titulos
titulos_rating_alto = []

#loop iterar pags
for pag in range(1,11): #solo lo puse hasta el 11 pq se me pega la pc xd ponlo como tu quieras
    #crear soup en cada pag
    url_pagina = url_principal.format(pag)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #selecciono datos de los libros
    libros = sopa.select('.product_pod')

    #iterar libros
    for libro in libros:

        #ver si tienen 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            #guardar titulo en variable 
            titulo_libro = libro.select('a')[1]['title']

            #agregar libro a lista
            titulos_rating_alto.append(titulo_libro)

#ver libros en terminal

for titulo in titulos_rating_alto:
    print(titulo)

