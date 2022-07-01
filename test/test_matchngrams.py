from ngrammatcher import NGramMatcher
import logging
import unittest
import json

logger = logging.getLogger(__name__)


class TestKeywordExtractor(unittest.TestCase):
    def setUp(self):
        logger.info("Starting...")
        with open('test/ngram_match_cases.json') as f:
            self.test_cases = json.load(f)

    def tearDown(self):
        logger.info("Ending.")

    def test_extract_keywords(self):
        """For each of the test case initialize a new NgramMatcher.
        Insert the ngrams into the NgramMatcher.
        Match ngrams and test if correctly matched.
        """
        for test_id, test_case in enumerate(self.test_cases):
            ngm = NGramMatcher()
            for original,ngram in test_case['dictionary'].items():
                ngm[ngram] = original

            if test_case['span_info'] == 1:
                ngrams = ngm.match_ngrams(test_case['input'] , span_info=True)

                self.assertEqual(len(ngrams), len(test_case['output']))

                for (input_ngram,input_start,input_end), (output_ngram, output_start, output_end) in zip(ngrams, test_case['output']):
                    self.assertEqual(input_ngram, output_ngram)
                    self.assertEqual(input_start, output_start)
                    self.assertEqual(input_end, output_end)

            if test_case['span_info'] == 0:
                ngrams = ngm.match_ngrams(test_case['input'] , span_info=False)
                self.assertEqual(ngrams, test_case['output'],
                                "matched ngrams don't match the expected results for test case: {}".format(test_id))

if __name__ == '__main__':
    unittest.main()