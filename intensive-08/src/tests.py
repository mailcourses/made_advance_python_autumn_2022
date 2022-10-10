import unittest
import random
from unittest.mock import patch
from io import StringIO

from heap import heapsort
import utils

class TestHeapSort(unittest.TestCase):
    def setUp(self):
       pass

    def test_sort_shuffle(self):
        '''Сортируем случайный список.'''

        lst = list(range(10))
        expected = list(range(10))
        random.shuffle(lst)
        actual = heapsort(lst)
        self.assertEqual(actual, expected)

    def test_sort_sorted(self):
        '''Сортируем отсортированный список.'''

        lst = list(range(10))
        expected = list(range(10))
        actual = heapsort(lst)
        self.assertEqual(actual, expected)

class TestMerge(unittest.TestCase):
    def setUp(self):
       pass

    def test_merge_2(self):
        '''Мерджим одинаковые элементы двух
        отсортированных списков в один.'''

        with patch('sys.stdout', new=StringIO()):
            lst1 = [1, 2, 4, 6, 7]
            lst2 = [2, 3, 4, 7, 8, 10]

            expected = [2, 4, 7]
            actual = utils.merge(lst1, lst2)
            self.assertEqual(actual, expected)

            lst1 = [1, 2, 2, 4, 6, 7]
            lst2 = [2, 2, 3, 4, 7, 8, 10]
            expected = [2, 4, 7]
            actual = utils.merge(lst1, lst2)
            self.assertEqual(actual, expected)

    def test_merge_2_empty(self):
        '''Мерджим одинаковые элементы двух
        отсортированных списков в один.'''

        with patch('sys.stdout', new=StringIO()):
            lst1 = []
            lst2 = []

            expected = []
            actual = utils.merge(lst1, lst2)
            self.assertEqual(actual, expected)

    def test_merge_k(self):
        '''Мерджим одинаковые элементы k
        отсортированных списков в один.'''

        with patch('sys.stdout', new=StringIO()):
            lists = [ [1, 2, 4, 6, 7], \
                      [2, 3, 4, 7, 8, 10] ]

            expected = [1, 2, 2, 3, 4, 4, 6, 7, 7, 8, 10]
            actual = utils.sort_k(lists)
            self.assertEqual(actual, expected)

def mocked_requests_get(*args, **kwargs):
    with open('fake/lenta_rss_top_7.xml', 'r') as fd:
        lenta_xml_content = fd.read()

    class MockedResponse:
        def __init__(self, str_content, status_code):
            self.content = str_content
            self.status_code = status_code

    if args[0].startswith('https://lenta.ru/rss'):
        return MockedResponse(lenta_xml_content, 200)

    return MockedResponse('', 404)

class TestConverterXmlToJson(unittest.TestCase):
    def setUp(self):
        pass

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_common(self, mock_get):
        '''Конвертируем xml в json для rss от lenta.ru.'''

        with patch('sys.stdout', new=StringIO()):
            expected = [{'title': 'Зеленский объяснил свои слова о превентивных ударах по России', \
                        'author': 'Василий Мека',\
                        'link': 'https://lenta.ru/news/2022/10/07/opravdyvayetsa/'\
            }]
            actual = utils.convert_lenta_xml_to_json()
            self.assertEqual(mock_get.call_count, 1)
            self.assertEqual(len(actual), len(expected))
            self.assertEqual(actual, expected)
