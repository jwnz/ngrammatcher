from ngrammatcher import NGramMatcher
import logging
import unittest
import json

logger = logging.getLogger(__name__)


class TestKeywordDelete(unittest.TestCase):
    def setUp(self):
        logger.info('Starting...')
        with open('test/ngram_del_cases.json') as f:
            self.test_cases = json.load(f)

    def tearDown(self):
        logger.info('Ending.')

    def test_delete_keywords(self):
        """For each of the test case initialize a new NGramMatcher.
        Insert the ngrams into the NgramMatcher.
        Delete ngrams and confirm all were deleted.
        """
        for test_id, test_case in enumerate(self.test_cases):
            ngm = NGramMatcher()
            for original,ngram in test_case['dictionary'].items():
                ngm[ngram] = original
            for del_status, del_ngram in test_case['delete']:
                del_result = ngm.delete_ngram(del_ngram)
                del_status = True if del_status=='True' else False
                self.assertEqual(del_status, del_result)

            ngrams = ngm.get_all_ngrams(keys_only=True)
            self.assertEqual(len(ngm), len(ngrams))
            self.assertCountEqual(ngrams, test_case['output'],
                            "matched ngrams don't match the expected results for test case: {}".format(test_id))

if __name__ == '__main__':
    unittest.main()