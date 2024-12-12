# Bottleworks Web Scraper
    #### Video Demo:  https://youtu.be/FqFrrAn2MpU
    #### Description: As a beer connoisseur, I'm always on the lookout for new and exciting brews to try, but searching through the vast selection of products on my favorite Seattle bottle shop's website can be tedious and exhausting. To simplify this process, I created a web scraper that streamlines the search by automatically scanning the entire website for beers that match specific search criteria. This tool helps save time and ensures I don't miss out on potential favorites.

    The program prompts the user to input search criteria, such as beer style, brewery, or size. It then performs a comprehensive search across all pages of the store's website, looking for products that contain the search term in their names. Once the program identifies matching products, it retrieves both the product name and its price, then displays this information directly in the terminal. Additionally, the program saves the results to a .txt file for later review, helping the user stay organized while discovering new beers.

How It Works:

Behind the scenes, the program utilizes two popular Python libraries:

Requests: This library is used to send HTTP requests to the website and retrieve the raw HTML content of each page.
BeautifulSoup: Once the page is fetched, BeautifulSoup is used to parse the HTML and extract relevant data, such as the beer name and price.
The program is designed to handle websites with multiple pages of products. It starts on the first page and works through subsequent pages until it reaches the end of the product list. On each page, it identifies and parses HTML elements containing the beer names and prices by targeting their specific CSS classes and tags. The program ensures that only the products matching the search term are selected.

If the program finds any matching products, it prints the results directly to the terminal, showing the product name and its price. Simultaneously, it appends the same results to a .txt file, allowing the user to easily save and reference their findings later.

Key Features:

Customizable Search Criteria: The user can specify the type of beer they are looking for, based on style, brewery, or size.
Multi-Page Scraping: The program automatically navigates through all pages of the bottle shop's website, ensuring no matching products are missed.
Terminal Output & File Saving: Results are shown in the terminal and saved to a text file for later use.
Efficient Data Handling: The program uses a generator to yield matching products, which ensures it can process large amounts of data without consuming excessive memory.
User-Friendly Flow: The program prompts the user for input and provides feedback throughout the process, making it easy to use even for those with little technical knowledge.
Whether you're looking for a specific beer style or exploring new breweries, this program helps streamline the search process, saving you time and effort as you discover new brews to enjoy.