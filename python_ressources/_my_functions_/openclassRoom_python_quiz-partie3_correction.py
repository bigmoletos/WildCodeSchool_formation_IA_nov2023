from bs4 import BeautifulSoup
import requests

# URL = "https://quiz-partie3.oc"
url='http://127.0.0.1:3000/_my_functions_/quiz-partie3.html'

def extract_data(url):
    response = requests.get(url)
    html = response.content
    return html

def get_title(soup):
    return soup.title.string

def get_all_product_info(soup, products):
    for table in soup.find_all('table'):
        for tr in table.find_all('tr')[1:]:
            td = tr.find_all('td')
            name = td[0].get_text()
            description = td[1].get_text()
            price = td[2].get_text()
            quantity = td[3].get_text()
            product = {
                'nom': name,
                'description': description,
                'prix': price,
                'quantite': quantity
            }
            products.append(product)

def convert_dollar_to_euro(products):
    change_rate = 0.8
    for product in products:
        price_euro = product['prix'].replace('€', '')
        price_euro = float(price_euro)

        price_dollar = price_euro * change_rate
        product['prix'] = str(round(price_dollar, 2)) + '$'

def load_data(soup, products):
    title = get_title(soup)
    with open(f'{title}.csv', mode='w', newline='') as file:
        fieldnames = ['nom', 'description', 'prix', 'quantite']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for product in products:
            writer.writerow(product)

if __name__ == '__main__':
    html = extract_data(url)
    soup = Beautiful_Soup(html, "html.parser")

products = []
get_all_product_info(soup, products)
convert_dollar_to_euro(products)
load_data(soup, products)