import scrapy


class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?groups=top_1000&start=1',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=51',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=101',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=151',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=201',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=251',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=301',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=351',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=401',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=451',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=501',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=551',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=601',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=651',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=701',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=751',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=801',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=851',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=901',
                  'https://www.imdb.com/search/title/?groups=top_1000&start=951',]

    def parse(self, response):
        movies = response.xpath("//div[@class='lister-item-content']")

        for movie in movies:
            movie_name = movie.xpath(".//h3//a//text()").get()
            movie_year = movie.xpath(".//h3//span[@class='lister-item-year text-muted unbold']//text()").get()
            movie_link = "https://www.imdb.com" + movie.xpath(".//h3//a//@href").get()
            movie_rating = movie.xpath(".//div[@class='ratings-bar']//strong//text()").get()
            metascore_rating = movie.xpath(".//div[@class='ratings-bar']//span[@class='metascore  favorable']//text()").get()
            movie_votes = movie.xpath(".//p//span[@name='nv']//text()").get()

            yield{
                    'movie name':movie_name,
                    'year':movie_year,
                    'movie link':movie_link,
                    'movie_rating':movie_rating,
                    'metascore':metascore_rating,
                    'votes':movie_votes,
                  }


