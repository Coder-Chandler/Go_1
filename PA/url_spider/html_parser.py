# !/usr/bin/python
# -*- coding:utf-8 -*-
# Html Parser
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):

    # Sub-link style, we need to follow page_url to complete sub-link (Baidu entry sub-link style -->/item/.)
    # Sub-link style, we need to follow page_url to complete sub-link (Wikipedia entry sub-link style -->/wiki/.)
    def _get_new_urls(self, page_url, soup):
        # We need to use set to filter the same data !
        new_urls = set()
        # find all the sub-links
        links = soup.find_all('a', href=re.compile(r"/wiki/.+"))
        '''print "links of sub-link is OK !"'''
        for link in links:
            new_url = link['href']  # get the link
            new_full_url = urlparse.urljoin(page_url, new_url) # make sub-link complete
            new_urls.add(new_full_url)  # add that completed sub-link in new_urls
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # Url
        res_data['url'] = page_url
        '''print "page_url has already add in res_data !"'''

        # Title tag -> <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>  (Baidu entry)
        # <h1 id="firstHeading" class="firstHeading" lang="zh-CN">人工智能
        title_node = soup.find('h1')
        # Add the XX_node in res_data
        res_data["title"] = title_node.get_text()
        '''print "title_node has already add in res_data !"'''

        '''
        # Summary tag -> <div class="lemma-summary" label-module="lemmaSummary"> (Baidu entry)
        summary_node = soup.find('div', class_="pinMetaWrapper")
        # Add the summary in res_data
        res_data["summary"] = summary_node.get_text()
        print 'img_node has already add in res_data !'
        '''

        return res_data

    def parse(self, page_url, html_cont):  # html_cont-->sub-links
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        # Add all the sub-links(completed sub-link) in new_urls(set)
        new_urls = self._get_new_urls(page_url, soup)
        # Get the data we need !
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data





