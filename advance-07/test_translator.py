import unittest
from unittest.mock import Mock, patch, call

from translator import translate, is_ny


class TestTranslator(unittest.TestCase):

    def test_translate_empty(self):
        res = translate("")
        self.assertEqual(res, "")

        res = translate("\t\n\n\t   \t")
        self.assertEqual(res, "")

    def test_translate_get_mocked(self):
        with patch("translator.requests.get") as mget:
            mget.return_value = Mock(text="йцукен")

            res = translate("qwerty")
            self.assertEqual(res, "йцукен")

            expected_calls = [
                call("translate.wiki.org/q=qwerty"),
            ]
            self.assertEqual(expected_calls, mget.mock_calls)

    @patch("translator.requests.get")
    def test_translate_get_mocked_side_effect(self, mget):
        mget.side_effect = lambda x: Mock(text=x[21:].title())

        res = translate("QWERTY")
        self.assertEqual(res, "Qwerty")

        res = translate("part")
        self.assertEqual(res, "Part")

        res = translate("go ducks")
        self.assertEqual(res, "Go Ducks")

        expected_calls = [
            call("translate.wiki.org/q=qwerty"),
            call("translate.wiki.org/q=part"),
            call("translate.wiki.org/q=go ducks"),
        ]
        self.assertEqual(expected_calls, mget.mock_calls)

    @patch("translator.requests.get")
    def test_translate_get_mocked_side_effect_predef(self, mget):
        mget.side_effect = [
            Mock(text="Qwerty"),
            Mock(text="Part"),
            Mock(text="Go Duck"),
            # ValueError("WRONG"),
        ]

        res = translate("QWERTY\npart\ngo ducks")
        self.assertEqual(res, "Qwerty\nPart\nGo Duck")

        expected_calls = [
            call("translate.wiki.org/q=qwerty"),
            call("translate.wiki.org/q=part"),
            call("translate.wiki.org/q=go ducks"),
        ]
        self.assertEqual(expected_calls, mget.mock_calls)

    def test_translate_wrong_url(self):
        with self.assertRaises(Exception) as err:
            res = translate("qwerty")

        exp = err.exception
        self.assertEqual(
            str(exp),
            "Invalid URL 'translate.wiki.org/q=qwerty': No scheme supplied. Perhaps you meant http://translate.wiki.org/q=qwerty?"
        )
