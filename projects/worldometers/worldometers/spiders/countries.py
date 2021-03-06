# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country']

    def parse(self, response):
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath('.//text()').get()
            country_link = country.xpath('.//@href').get()


            yield response.follow(url = country_link)

            # yield {
            #     'country_name' : country_name,
            #     'country_link' : country_link
            #     }
