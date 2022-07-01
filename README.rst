============
NGramMatcher
============

.. image:: https://badge.fury.io/py/ngrammatcher.svg
    :target: https://badge.fury.io/py/ngrammatcher
    :alt: Version

.. image:: https://coveralls.io/repos/github/jwnz/ngrammatcher/badge.svg?branch=master
    :target: https://coveralls.io/github/jwnz/ngrammatcher?branch=master
    :alt: Test coverage

.. image:: https://img.shields.io/badge/License-MIT-green.svg
    :target: https://github.com/jwnz/ngrammatcher/blob/master/LICENSE
    :alt: license


`NGramMatcher <https://github.com/jwnz/ngrammatcher?branch=master>`_ is a module that can be used to extract n-grams, tokens, or keywords from a list of tokens.



Installation
------------

.. code-block:: bash

    $ pip install ngrammatcher


Usage
-----

Overview

.. code-block:: python

    from ngrammatcher import NGramMatcher

    # init NgramMatcher object
    ngm = NGramMatcher()

    # add ngrams and their corresponding data
    ngm.insert_ngram(['programming','language'], 'programming language')
    ngm.insert_ngram(['Python'], 'Python')

    # match ngrams
    ngm.match_ngrams(['Python', 'is', 'a', 'programming', 'language'])
    # ['Python', 'programming language']

Adding n-grams

.. code-block:: python

    from ngrammatcher import NGramMatcher
    ngm = NGramMatcher()

    # You can add n-grams of any size
    ngm.insert_ngram(['programming','language'], 'programming language') # 2-gram
    ngm.insert_ngram(['Python'], 'Python') # 1-gram
    ngm.insert_ngram(['a']*10000, 'a'*10000) # 10_000-gram

    # you can map any kind of data to an n-gram
    data = {
        'word': 'programming language',
        'wikipedia': 'https://en.wikipedia.org/wiki/Programming_language'
        'desc': 'A programming language is any set of rules that converts...'
    }
    ngm.insert_ngram(['programming', 'language'], data)

    # you can also insert n-grams using dictionary sytax
    ngm[['c','plus','plus']] = 'c++'

    # or add words
    ngm.insert_ngram(list('test'), 'test')


Finding n-grams

.. code-block:: python

    from ngrammatcher import NGramMatcher
    ngm = NGramMatcher()
    ngm.insert_ngram(['programming','language'], 'programming language')
    ngm.insert_ngram(['Python'], 'Python')

    # here we will use spacy to create tokens
    import spacy
    nlp = spacy.load('en_core_web_lg')
    text = 'Python is a programming language'

    tokens = [tok.text for tok in nlp(text)]

    # find n-grams
    ngm.match_ngrams(tokens)
    # ['Python', 'programming language']

Additional Functionality

.. code-block:: python

    from ngrammatcher import NGramMatcher
    ngm = NGramMatcher()
    ngm.insert_ngram(['programming','language'], 'programming language')
    ngm.insert_ngram(['Python'], 'Python')

    # get all n-grams in the trie
    ngm.get_all_ngrams()
    # [(['Python'], 'Python'), (['programming', 'language'], 'programming language')]

    # you can exclude the data object too
    ngm.get_all_ngrams(keys_only=True) 
    # [['Python'], ['programming', 'language']]

    # delete n-grams (returns True if deleted, False otherwise)
    ngm.delete_ngram(['Python'])
    # True


    # Additional Quality-of-Life functionality
    len(ngm) # get the number of n-grams in trie

    ['programming', 'language'] in ngm # check if n-gram is in trie

    ngm[['programming', 'language']] = 'PL' # insert an n-gram into the trie

    ngm[['programming', 'language']] # get the data for a specific n-gram

    del ngm[['programming', 'language']] # delete an ngram using del
    



Test
----
.. code-block:: bash

     $ git clone https://github.com/jwnz/ngrammatcher
     $ cd ngrammatcher
     $ pip install pytest
     $ python setup.py test