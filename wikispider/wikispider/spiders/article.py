import scrapy
'''開啟方式:需要先cd到wikispider\wikispider(cd..回到上個目錄)'''
'''執行方式:scrapy crawl article(name的名稱)'''
class ArticleSpider(scrapy.Spider):
    name='article'

    def start_requests(self):
        urls = [
            "http://en.wikipedia.org/wiki/Python_%28programming_language%29",
            "https://en.wikipedia.org/wiki/Functional_programming",
            "https://en.wikipedia.org/wiki/Monty_Python"]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))