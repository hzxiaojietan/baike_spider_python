import urllib.request


class HtmlDownload(object):
    """docstring for HtmlDownload"""

    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        print(response.status, type(content), len(content))
        if response.status != 200:
            return None
        return content
