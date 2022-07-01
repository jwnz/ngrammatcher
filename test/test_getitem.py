from ngrammatcher import NGramMatcher
import logging
import unittest
import json

logger = logging.getLogger(__name__)


class TestGetItem(unittest.TestCase):
    def setUp(self):
        logger.info('Starting...')
        with open('test/ngram_getitem_cases.json') as f:
            self.test_cases = json.load(f)

    def tearDown(self):
        logger.info('Ending.')

    def test_delete_keywords(self):
        """For each of the test case initialize a new NGramMatcher.
        Check the __getitem__ function
        """
        for test_id, test_case in enumerate(self.test_cases):
            ngm = NGramMatcher()
            for original,ngram in test_case['dictionary'].items():
                ngm[ngram] = original

            for ngram, target in test_case['output']:
                self.assertEqual(ngm[ngram], target)

if __name__ == '__main__':
    unittest.main()