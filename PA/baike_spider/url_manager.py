# Url Manager


class UrlManager(object):
    def __init__(self):
        # We need to use set to filter the same data !
        self.new_urls = set()
        self.old_urls = set()

    # Add a new url in new_urls
    def add_new_url(self, url):
        #  url is None,then return None
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # Add a mount of url to new_urls from spider_main
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        # Add the url to the urls with the iterative way
        for url in urls:
            self.add_new_url(url)

    # To determine whether the new_urls is not empty !
    def has_new_url(self):
        return len(self.new_urls) != 0

    # Every time when the spider call get_new_url , We take a new_url give to the spider from new_urls ,
    # then we should add that new_url in old_urls to avoid recrawl
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
