from faker.providers import BaseProvider
from random import randint, sample
import urllib.request
import urllib.parse
import tempfile
import os
import string


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

        if len(kwargs) > 0:
            if kwargs.get('rand', False):
                kwargs['rand'] = randint(1, 1000000)
            return url + '?' + urllib.parse.urlencode(kwargs)

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

    def image(self, dir=None, filename=None, width=720, height=480, category='', **kwargs):
        """
        Downloads an image to the specified directory.
        :param filename: the file name with the extension ('example.png'). If None
            random name will be generated
        :param dir: the directory where to be placed the image
        :param width: the width of the image
        :param height: the height of the image
        :param category: string with the category name
        :param kwargs:
        :return:
        """
        url = self.image_url(width, height, category, **kwargs)

        if dir is None:
            dir = tempfile.gettempdir()

        if filename is None:
            base62_chars = string.ascii_letters + string.digits
            filename = ''.join(sample(base62_chars, len(base62_chars))) + '.jpg'

        full_path = os.path.join(dir, filename)
        file = open(full_path, 'wb')
        req = urllib.request.Request(url)
        req_handler = urllib.request.urlopen(req)
        file.write(req_handler.read())
        file.close()

        return full_path

    def gif(self, dir=None, filename=None):
        """
        Downloads a gif to the specified directory.
        :param dir: the directory to store the gif. Default to None means
            that takes the default OS temporary directory.
        :param filename: the name to store the gif. Default to None means
            that takes a random name.
        :return: string with the full path name
        """
        url = self.gif_url()

        if dir is None:
            dir = tempfile.gettempdir()

        if filename is None:
            base62_chars = string.ascii_letters + string.digits
            filename = ''.join(sample(base62_chars, len(base62_chars))) + '.gif'

        full_path = os.path.join(dir, filename)
        file = open(full_path, 'wb')

        req = urllib.request.Request(url)
        req_handler = urllib.request.urlopen(req)
        file.write(req_handler.read())
        file.close()

        return full_path
