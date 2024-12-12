import requests
from bs4 import BeautifulSoup
import time

def main():
    search_term = get_search_criteria()
    if not search_term:
        return
    
    #print to show user something is happening
    print(f"Searching for '{search_term}'...")
    scrape_beers(search_term)

def get_search_criteria():
    search_term = input("Enter the search criteria ('size', 'brewery', 'style'): ").strip().lower()

    if not search_term:
        print("Please enter search criteria")
        return None
    return search_term


def fetch_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')


def parse_products(soup, search_term):
    products = soup.find_all('div', class_='astra-shop-summary-wrap')
    found_any = False
    for product in products:
        beer_name_tag = product.find('h2', class_='woocommerce-loop-product__title')
        price_tag = product.find('span', class_='woocommerce-Price-amount amount')

        if beer_name_tag and price_tag:
            beer_name = beer_name_tag.text.strip()
            price = price_tag.text.strip()

            if search_term in beer_name.lower():
                found_any = True
                yield beer_name, price

    return found_any

# save results to a txt file
def save_to_file(filename, data):
    with open(filename, "a") as file:
        for beer_name, price in data:
            file.write(f"{beer_name} = {price}\n")


#scrape beers based on search term
def scrape_beers(search_term, base_url='https://www.bottleworks.com/shop/'):
    page = 1  # start at page 1
    filename = "found_beers.txt"
    
    while True:
        url = f'{base_url}page/{page}/'
        soup = fetch_page(url)       
        if not soup:
            break
        
        # parse the products on the current page
        products_found = list(parse_products(soup, search_term))
        
        if products_found:
            # print results and save to file
            for beer_name, price in products_found:
                print(f"{beer_name} = {price}")
            save_to_file(filename, products_found)
        
        # another page?
        next_page_tag = soup.find('a', class_='next page-numbers')
        if next_page_tag:
            page += 1
            time.sleep(1)
        else:
            print("Done scraping.")
            break


if __name__ == "__main__":
    main()
