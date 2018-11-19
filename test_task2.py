from unittest import TestCase

import task2


class TestTask2(TestCase):

    def test_loop(self):
        """Test for task2"""
        self.assertEqual(task2.loop(1), 0)
        self.assertTrue(task2.loop(5))
