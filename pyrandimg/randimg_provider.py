from faker.providers import BaseProvider
from random import randint
import urllib.request


class RandImgProvider(BaseProvider):
    """
    The class RandImgProvider contains all the logic for generate random
    image urls and also for download it.
    """
    base_url = 'http://www.rand-img.com'

    def image_url(self, width=720, height=480, category='', **kwargs):
        """
        Generate a random image url.
        :param width: int
        :param height: int
        :param category: string
        :param kwargs: Optional list of parameters for the image.
        :return: a string containing the full url
        """
        started_query = False
        url = self.base_url
        url += "/%d/%d" % (width, height, )

        if len(category) > 0:
            url += "/%s" % category

        index = 0
        # Join all key=value for generating the query URL
        for key, val in kwargs.items():
            if key == 'rand':
                if val:
                    rand_param = 'rand=%d' % randint(1, 1000000)
                    if index == 0:
                        url += '?' + rand_param
                        started_query = True
                    else:
                        url += '&' + rand_param
            else:
                if started_query:
                    url += '&%s=%s' % (key, str(val),)
                else:
                    url += '?%s=%s' % (key, str(val),)
                    started_query = True
            index += 1

        return url

    def squared_image_url(self, width=720, category='', **kwargs):
        """
        Helper method that generate a squared image url.
        :param width: the width (and height) of the image
        :param category: string
        :param kwargs: Optional list of parameters for the image.
        :return: a string containing the full url
        """
        return self.image_url(width, width, category, **kwargs)

    def gif_url(self, rand=False):
        """
        Generate a random gif url. It can attach
        a random number to avoid that multiple gifs loaded
        in the page will be all the same gif.

        :param rand: bool if True then a random number will be attached to the URL.
        :return:
        """
        url = '%s/gif' % self.base_url
        if rand:
            url += '?rand=%d' % randint(1, 1000000)

        return url

    def image(self, dir=None, width=720, height=480, category='', **kwargs):
        """
        Downloads an image to the specified directory.
        :param dir: the directory where to be placed the image
        :param width: the width of the image
        :param height: the height of the image
        :param category: string with the category name
        :param kwargs:
        :return:
        """
        pass

    def gif(self, dir=None):
        """
        Downloads a gif to the specified directory.
        :param dir:
        :return:
        """
        url = self.gif_url()
        req = urllib.request.Request(url)
        req_handler = urllib.request.urlopen(req)
        # print(req_handler.read())

