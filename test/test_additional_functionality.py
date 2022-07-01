from ngrammatcher import NGramMatcher
import logging
import unittest
import json

logger = logging.getLogger(__name__)


class TestGetAllNGrams(unittest.TestCase):
    def setUp(self):
        logger.info('Starting...')

    def tearDown(self):
        logger.info('Ending.')

    def test_delete_keywords(self):
        """Create NGramMatcher Object and test get all ngrams
        """
        ngm = NGramMatcher()
        ngram = ['programming', 'language']
        ngm[ngram] = 'programming language'

        self.assertEqual(ngm.get_all_ngrams(keys_only=True), [['programming', 'language']])

        all_ngrams = ngm.get_all_ngrams()[0]
        print(all_ngrams)

        self.assertCountEqual(all_ngrams[0], ['programming', 'language'])
        self.assertEqual(all_ngrams[1], 'programming language')

class TestContains(unittest.TestCase):
    def setUp(self):
        logger.info('Starting...')

    def tearDown(self):
        logger.info('Ending.')

    def test_delete_keywords(self):
        """Create NGramMatcher Object and test __contains__
        """
        ngm = NGramMatcher()
        ngram = ['programming', 'language']
        ngm[ngram] = 'programming language'

        self.assertEqual(ngram in ngm, True)
        self.assertEqual(['python'] in ngm, False)

class TestDel(unittest.TestCase):
    def setUp(self):
        logger.info('Starting...')

    def tearDown(self):
        logger.info('Ending.')

    def test_delete_keywords(self):
        """Create NGramMatcher Object and test __delitem__
        """
        ngm = NGramMatcher()
        ngram = ['programming', 'language']
        ngm[ngram] = 'programming language'

        del ngm[ngram]

        self.assertEqual(ngram in ngm, False)

if __name__ == '__main__':
    unittest.main()