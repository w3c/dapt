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

    def testValidFileAfterPruning(self):
        with open(
            os.path.join(fixture_dur, 'valid_dapt.ttml'),
            mode='rb') \
                as dapt_file:
            result = validate_dapt(
                args=Namespace(
                    dapt_in=dapt_file,
                    noprune=False))

        self.assertEqual(result, 0)

    def testInvalidFileBeforePruning(self):
        with open(
            os.path.join(fixture_dur, 'valid_dapt.ttml'),
            mode='rb') \
                as dapt_file:
            result = validate_dapt(
                args=Namespace(
                    dapt_in=dapt_file,
                    noprune=True))

        self.assertEqual(result, -1)
