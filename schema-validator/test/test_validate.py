import os
import unittest
from argparse import Namespace
from src.validate import validate_dapt

fixture_dur = \
    os.path.join(
        os.path.dirname(__file__),
        'fixtures')


class testValidate(unittest.TestCase):
    maxDiff = None

    def testValidFile(self):
        with open(
            os.path.join(fixture_dur, 'valid_dapt.ttml'), newline='') \
                as dapt_file:
            result = validate_dapt(args=Namespace(dapt_in=dapt_file))

        self.assertEqual(result, 0)
