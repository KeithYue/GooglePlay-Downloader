# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst, Compose
from scrapy.utils.markup import remove_entities
from scrapy.contrib.loader.processor import MapCompose, Join, TakeFirst, Compose

class AppItem(Item):
    # define the fields for your item here like:
    # name = Field()
    app_id = Field(
            input_processor = MapCompose(remove_entities, unicode.strip),
            output_processor = TakeFirst()
            )
    app_type = Field(
            input_processor = MapCompose(remove_entities, unicode.strip),
            output_processor = Join()
            )
    title  = Field(
            input_processor = MapCompose(remove_entities, unicode.strip),
            output_processor = Join()
            )
    description = Field(
            input_processor = MapCompose(remove_entities, unicode.strip),
            output_processor = Join()
            )
    score = Field(
            input_processor = MapCompose(remove_entities, unicode.strip),
            output_processor = Join()
            )
    author = Field(
            input_processor = MapCompose(remove_entities, unicode.strip),
            output_processor = Join()
            )
    icon_url = Field(
            output_processor = TakeFirst()
            )
    similarity = Field()
    more_from_devs = Field()

