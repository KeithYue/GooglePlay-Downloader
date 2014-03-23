import urlparse
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from googleplay_crawler.items import AppItem
from scrapy.contrib.loader import XPathItemLoader
from pprint import pprint

def get_start_urls():
    s = []
    f = open('url.txt', 'r')
    for line in f.readlines():
        s.append(line.strip())
    f.close()
    return s

class GoogleSpider(CrawlSpider):
    name = 'google_spider'
    allowed_domains = ['play.google.com']
    start_urls = get_start_urls()

    rules = (
            Rule(SgmlLinkExtractor(allow=r'store/apps/details\?id=*', process_value=lambda x: x+'&hl=en'), callback='parse_item', follow=True), # track all the app details
    )

    def parse_item(self, response):
        sel = Selector(response)
        print response.url
        app_loader = XPathItemLoader(item = AppItem(), selector = sel) # init the item loader
        # set app id
        app_loader.add_value('app_id', parse_id(response.url))
        # composite the title
        app_loader.add_xpath('title', '//div[contains(@class, "document-title")]//text()')
        app_loader.add_xpath('description', '//div[contains(@class, "id-app-orig-desc")]//text()')
        app_loader.add_xpath('score', '//meta[@itemprop="ratingValue"]//@content')
        app_loader.add_xpath('icon_url', '//div[contains(@class, "details-info")]//img[contains(@class, "cover-image")]/@src')
        app_loader.add_xpath('author', '//div[@itemprop="author"]//span[@itemprop="name"]//text()')
        app_loader.add_xpath('app_type', '//div[contains(@class, "details-info")]//span[@itemprop="genre"]/text()')

        # get the similarities and the more from developers
        app_loader.add_xpath('similarity', '//div[contains(@class, "recommendation")]//div[contains(@class, "details-section-contents")]/div[@class="rec-cluster" and position()=1]//div[contains(@class, "card")]/@data-docid')

        app_loader.add_xpath('more_from_devs', '//div[contains(@class, "recommendation")]//div[contains(@class, "details-section-contents")]/div[@class="rec-cluster" and position()=2]//div[contains(@class, "card")]/@data-docid')

        # print app_loader.load_item()
        # print app_loader.get_output_value('app_id')

        return app_loader.load_item()

def parse_id(url_str):
    '''
    given a url string, return the
    '''
    r = urlparse.urlparse(url_str)
    p = urlparse.parse_qs(r.query,True)
    return ''.join(p['id']).strip()
