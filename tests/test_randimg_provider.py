import unittest
import os
from faker import Faker
from pyrandimg.randimg_provider import RandImgProvider


class TestRandImgProvider(unittest.TestCase):
    def setUp(self):
        """ Initialize each unit test """
        self.faker = Faker()
        self.faker.add_provider(RandImgProvider)

    def test_generate_default_image_url(self):
        self.assertRegex(self.faker.image_url(), r'^(https?\:\/\/)?www\.rand\-img\.com\/720\/480$')

    def test_generate_image_url_with_custom_width(self):
        self.assertRegex(self.faker.image_url(200), r'^(https?\:\/\/)?www\.rand\-img\.com\/200\/480$')
        self.assertRegex(self.faker.image_url(980), r'^(https?\:\/\/)?www\.rand\-img\.com\/980\/480$')

    def test_generate_image_url_with_custom_width_and_height(self):
        self.assertRegex(self.faker.image_url(200, 500), r'^(https?\:\/\/)?www\.rand\-img\.com\/200\/500$')
        self.assertRegex(self.faker.image_url(320, 280), r'^(https?\:\/\/)?www\.rand\-img\.com\/320\/280$')
        self.assertRegex(self.faker.image_url(1920, 1080), r'(https?\:\/\/)?www\.rand\-img\.com\/1920\/1080')

    def test_generate_image_url_with_category(self):
        self.assertRegex(self.faker.image_url(200, 500, 'food'), r'^(https?\:\/\/)?www\.rand\-img\.com\/200\/500\/food$')
        self.assertRegex(self.faker.image_url(500, 653, 'sky'), r'^(https?\:\/\/)?www\.rand\-img\.com\/500\/653\/sky$')

    def test_generate_rand_image_url(self):
        self.assertRegex(
            self.faker.squared_image_url(320, rand=True),
            r'^(https?\:\/\/)?www\.rand\-img\.com\/320\/320\?rand=\d+$'
        )

    def test_generate_default_squared_image_url(self):
        self.assertRegex(self.faker.squared_image_url(200), r'^(https?\:\/\/)?www\.rand\-img\.com\/200\/200$')

    def test_generate_squared_image_url_with_category(self):
        self.assertRegex(
            self.faker.squared_image_url(200, 'food'),
            r'^(https?\:\/\/)?www\.rand\-img\.com\/200\/200\/food$'
        )
        self.assertRegex(
            self.faker.squared_image_url(1024, 'sky'),
            r'^(https?\:\/\/)?www\.rand\-img\.com\/1024\/1024\/sky$'
        )

    def test_image_url_with_parameters(self):
        self.assertRegex(
            self.faker.image_url(720, 480, 'food', rand=True, blur=4, gray=1),
            r'https?:\/\/www\.rand\-img\.com\/720\/480/food\?([(\&?rand\=\d+)(\&?blur\=4)(\&?gray\=1)])'
        )
        self.assertRegex(
            self.faker.image_url(250, 120, 'fashion', rand=False, blur=4, gray=1),
            r'https?:\/\/www\.rand\-img\.com\/250\/120/fashion\?([(\&?blur\=4)(\&?gray\=1)])'
        )

    def test_get_gif(self):
        self.assertRegex(self.faker.gif_url(), r'^(https?\:\/\/)?www\.rand\-img\.com\/gif$')

    def test_get_gif_with_rand(self):
        self.assertRegex(self.faker.gif_url(True), r'^(https?\:\/\/)?www\.rand\-img\.com\/gif\?rand\=\d+$')

    def test_download_gif(self):
        gif = self.faker.gif()
        gif_dirname = os.path.dirname(gif)
        _, file_ext = os.path.splitext(gif)

        self.assertEqual('.gif', file_ext)
        self.assertTrue(os.path.exists(gif))
        os.remove(gif)

    def test_download_gif_with_dirname(self):
        os.mkdir('output')
        output_dir = os.path.join(os.getcwd(), 'output')
        gif = self.faker.gif(dir=output_dir)
        gif_dirname = os.path.dirname(gif)
        _, file_ext = os.path.splitext(gif)

        self.assertEqual(output_dir, gif_dirname)
        self.assertEqual('.gif', file_ext)
        self.assertTrue(os.path.exists(gif))
        os.remove(gif)
        os.rmdir(output_dir)

    def test_download_gif_with_invalid_argument_exception(self):
        pass

    def test_download_image(self):
        gif = self.faker.gif()
        gif_dirname = os.path.dirname(gif)
        _, file_ext = os.path.splitext(gif)

        self.assertEqual('.gif', file_ext)
        self.assertTrue(os.path.exists(gif))
        os.remove(gif)

    def test_download_image_with_dirname(self):
        os.mkdir('output')
        output_dir = os.path.join(os.getcwd(), 'output')
        image = self.faker.image(dir=output_dir)
        image_dirname = os.path.dirname(image)
        _, file_ext = os.path.splitext(image)

        self.assertEqual(output_dir, image_dirname)
        self.assertEqual('.jpg', file_ext)
        self.assertTrue(os.path.exists(image))
        os.remove(image)
        os.rmdir(output_dir)

    def test_download_image_with_dirname_and_filename(self):
        os.mkdir('output')
        output_dir = os.path.join(os.getcwd(), 'output')
        image = self.faker.image(dir=output_dir, filename='testing.png')
        image_dirname = os.path.dirname(image)
        _, file_ext = os.path.splitext(image)

        self.assertEqual(output_dir, image_dirname)
        self.assertEqual('.png', file_ext)
        self.assertTrue(os.path.exists(image))
        os.remove(image)
        os.rmdir(output_dir)

    def test_download_image_with_exception(self):
        pass

    def test_download_image_with_invalid_argument_exception(self):
        pass
