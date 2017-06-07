# Html Downloader
import urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        # open the url and give to response (Temporarily stored in the buffer)
        response = urllib2.urlopen(url)

        # 200 OK! Standard response for successful HTTP requests
        if response.getcode() != 200:
            return None
        # read all the information and give to spider
        return response.read()