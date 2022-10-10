import unittest
from unittest import mock

from salary import get_total_salary


class TestSalary(unittest.TestCase):

    def test_salary_good(self):
        res = get_total_salary("user", 100)
        self.assertEqual(res, 600)

        res = get_total_salary("user", 0)
        self.assertEqual(res, 500)

    def test_salary_negative(self):
        with self.assertRaises(ValueError) as err:
            get_total_salary("user", -1)

        self.assertEqual(str(err.exception), "low_bonus")

        self.assertRaises(ValueError, get_total_salary, "user", bonus=-1)

    def test_salary_with_api(self):
        with mock.patch("salary.get_salary_from_api") as m_get_sal:
            m_get_sal.return_value = 42
            res = get_total_salary("user", 0)
            self.assertEqual(res, 42)
            self.assertEqual(
                m_get_sal.mock_calls,
                [
                    mock.call("user")
                ],
            )

        with mock.patch("salary.get_salary_from_api") as m_get_sal:
            m_get_sal.side_effect = lambda x: 10 if x == "qwerty" else 20

            res = get_total_salary("user", 0)
            self.assertEqual(res, 20)

            res = get_total_salary("qwerty", 0)
            self.assertEqual(res, 10)

        with mock.patch("salary.get_salary_from_api") as m_get_sal:
            m_get_sal.side_effect = [99, 44]

            res = get_total_salary("user", 0)
            self.assertEqual(res, 99)

            res = get_total_salary("qwerty", 0)
            self.assertEqual(res, 44)

            self.assertEqual(
                m_get_sal.mock_calls,
                [
                    mock.call("user"),
                    mock.call("qwerty"),
                ],
            )
