'''
spider is a python module
which fetches the HTML content
of the given url and calls the callback
functions
'''

import scrapy

print(dir(scrapy))
class BookSpider(scrapy.Spider):

    name = "books"

    def start_requests(self):
        return [
            scrapy.Request(url = "https://books.toscrape.com/", callback = self.parse )
        ]
    
    def parse(self, response):
        '''
        parse is being called as
        soon as start_request method
        runs and fetches the data.
        response is the parameter
        which carries the request html

        
        '''
        # with open("books.html", "wb") as file:
        #     file.write(response.body)

        '''
        fetch only title of the books using
        response.css()
        '''

        '''
        Yield is a lazy iterator,
        unlike other iterator it gives
        the current element and load into memory
        and writes in a file
        '''
        # titles = response.css("article.product_pod img::attr(alt)").getall()
        # prices = response.css("div.product_price p.price_color::text").getall()
        # for title in titles:
        #     yield{"book title": title}
        
        # for price in prices:
        #     yield{"price":price}

        for selector in response.css("article.product_pod"):
            title = selector.css("img::attr(alt)").get()
            price = selector.css("p.price_color::text").get()

            yield{"book title":title, "price":price}


        #I want all 50 pages data
        #get next_page url
        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            url_hit = response.urljoin(next_page)
            yield scrapy.Request(url = url_hit, callback = self.parse)