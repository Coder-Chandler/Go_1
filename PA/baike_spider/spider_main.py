# Url Scheduler
from baike_spider import html_outputer, html_downloader, url_manager, html_parser


class SpiderMain(object):
    def __init__(self):
        # Url manager
        self.urls = url_manager.UrlManager()
        # Url downloader
        self.downloader = html_downloader.HtmlDownloader()
        # Url parser
        self.parser = html_parser.HtmlParser()
        # Url output device
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # Add a new url (any website you want to get !
        self.urls.add_new_url(root_url)  # (method in url manager)
        # We should use a loop to get information we need
        # from the website which we input
        while self.urls.has_new_url():  # (method in url manager)
            # Use a 'try...except' to print some error when we Crawling information from failed link
            try:
                # Call 'get_new_url()' from url_manager to get a new url(method in url_manager)
                new_url = self.urls.get_new_url()
                # To tell us which url the spider has already crawing to
                print 'Craw %d : %s'%(count, new_url)
                # when we get the new_url from url_manager,we need to download that url with html_downloader
                html_cont = self.downloader.download(new_url)
                print 'html_cont is OK !'
                # Every time When we download a new_url,we need to get the data from it,
                # and we also need to get all the sub-links(html_cont) from this new_url,
                # so we need a parser(in html_parser) !
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                print 'new_urls, new_data is OK !'
                # Take these sub links back to url_manager that make the spider_main can call these sub links
                # in this while loop and get some data we need from thses sub links
                self.urls.add_new_urls(new_urls)
                print 'add_new_urls is OK !'
                # Every time we complete the fetch, download, parse a url,
                # we need to output the data we get through the outputer
                self.outputer.collect_data(new_data)
                print 'collect_data is OK !'

                # We need to set a judgment condition to break the loop,
                # also the number of times to crawl the data
                if count == 10:
                    break
                count += 1
            except:
                # print some information if the spider fetch some failed links
                print 'Craw failed'
        # When the spider crawls 1000 times , we just output !
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://www.pinterest.com/search/pins/?q=watercolor%20love%20couple'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
