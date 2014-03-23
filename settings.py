# Scrapy settings for googleplay_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'googleplay_crawler'

SPIDER_MODULES = ['googleplay_crawler.spiders']
NEWSPIDER_MODULE = 'googleplay_crawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'googleplay_crawler (+http://www.yourdomain.com)'

DEFAULT_REQUEST_HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en'
        }
