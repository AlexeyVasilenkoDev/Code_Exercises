import unittest


def formatted_name(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):
    def setUp(self):
        self.first_name = "Mark"
        self.last_name = "Jones"

    def test_normal_name(self):
        self.assertEqual(formatted_name(self.first_name, self.last_name), 'Mark Jones')

    def test_missing_parameter(self):
        with self.assertRaises(TypeError):
            formatted_name(self.first_name)

    def test_extre_parameter(self):
        with self.assertRaises(TypeError):
            formatted_name(self.first_name, self.last_name, 'David', 'Steve')

    def test_invalid_parameter(self):
        with self.assertRaises(TypeError):
            formatted_name(1, 2)

    def test_middle_name(self):
        self.assertEqual(formatted_name(self.first_name, self.last_name, '     '), 'Mark       Jones')

