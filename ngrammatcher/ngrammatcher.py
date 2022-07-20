class NGramMatcher():
    """NGramMatcher

    Attributes:
        trie : dict
            Trie dict build word by word used for lookup

        ngram_count : int
            Total number of ngrams stored in the trie

        end_boundary_tag : Any
            The key used to store the value corresponding to an ngram

    Examples:
        >>> from ngrammatcher import NGramMatcher
        >>> ngm = NGramMatcher()
        >>> # add ngrams (1-grams are also okay)
        >>> ngm.insert_ngram(['programming','language'], 'programming language')
        >>> ngm.insert_ngram(['Python'], 'Python')
        >>> ngm.match_ngrams(['Python', 'is', 'a', 'programming', 'language'])
        ['Python', 'programming language']

    Note:
        * Based off of `flashtext <https://arxiv.org/abs/1711.00046>`_ and modified to suit my personal needs.
    """
 
    def __init__(self):
        """Initialize NGramMatcher Object
        """
        self.trie = {}
        self.ngram_count = 0
        self.end_boundary_tag = -100

    def __setitem__(self, ngram, data):
        """Add ngram to the trie
        
        Args:
            ngram : List[str]
                ngram to be insert into trie
                
            data : Any
                object correlating to the ngram

        Examples:
            >>> from ngrammatcher import NGramMatcher
            >>> ngm = NGramMatcher()
            >>> ngram = ['programming', 'language']
            >>> ngm[ngram] = 'programming language'
        """
        self.insert_ngram(ngram, data)
        
    def __getitem__(self, ngram):
        """Get the value corresponding to a specified ngram

        Args:
            ngram : List[str]
                ngram in which to retrieve the correspondig value

        Returns:
            obj : Any
                object corresponding to the specified ngram

        Examples:
            >>> from ngrammatcher import NGramMatcher
            >>> ngm = NGramMatcher()
            >>> ngram = ['programming', 'language']
            >>> ngm[ngram] = 'programming language'
            >>> ngm[ngram]
            'programming language'
        """
        head = self.trie
        for word in ngram:
            if word in head:
                head = head[word]
            else:
                return None
        if self.end_boundary_tag not in head:
            return None
        return head[self.end_boundary_tag]

    def __delitem__(self, ngram):
        """Delete item from trie using del keyword

        Args:
            nrgam : List[str]
                ngram to delete from trie

        Example:
            >>> from ngrammatcher import NGramMatcher
            >>> ngm = NGramMatcher()
            >>> ngm.insert_ngram(['programming', 'language'], 'programming language')
            >>> ['programming', 'language'] in ngm
            True
            >>> del ngm[['programming', 'language']]
            >>> ['programming', 'language'] in ngm
            False
        """
        self.delete_ngram(ngram)

    def __contains__(self, ngram):
        """Check whether or not an ngram is in the trie

        Args:
            ngram : List[str]

        Returns:
            val : bool
                True if ngram is in the trie, False otherwise.

        Examples:
            >>> from ngrammatcher import NGramMatcher
            >>> ngm = NGramMatcher()
            >>> ngm.insert_ngram(['programming', 'language'], 'programming language')
            >>> ['programming', 'language'] in ngm
            True
            >>> ['Python'] in ngm
            False
        """
        head = self.trie
        for word in ngram:
            if word in head:
                head = head[word]
            else:
                return False

        return self.end_boundary_tag in head
    
    def __len__(self):
        """Return the number of ngrams in the trie

        Returns:
            ngram_count : int
                number of ngrams in the trie

        Examples:
            >>> from ngrammatcher import NGramMatcher
            >>> ngm = NGramMatcher()
            >>> ngm.insert_ngram(['programming', 'language'], 'programming language')
            >>> len(ngm)
            1
        """
        return self.ngram_count

    def delete_ngram(self, ngram):
        """Deletes an ngram from the trie.

        Args:
            nrgam : List[str]
                ngram to delete from trie

        Returns:
            deleted : bool
                True if the word was deleted otherwise False

        Example:
            >>> from ngrammatcher import NGramMatcher
            >>> ngm = NGramMatcher()
            >>> ngm.insert_ngram(['programming', 'language'], 'programming language')
            >>> ['programming', 'language'] in ngm
            True
            >>> ngm.delete_ngram(['programming', 'language'])
            True
            >>> ['programming', 'language'] in ngm
            False
        """
        subtrie = self.trie
        stack = []
        for word in ngram:
            if word in subtrie:
                stack.append((word,subtrie[word]))
                subtrie = subtrie[word]
            # the ngram isn't in the trie to begin with
            else:
                return False
                

        # remove last element - corresponding to ngram
        _, subtrie = stack[-1]
        if self.end_boundary_tag in subtrie:
            del subtrie[self.end_boundary_tag]
        else:
            return False

        # update trie to remove hanging leaves
        previous_word = None
        while stack:
            word, subtrie = stack.pop(-1)
            if previous_word is not None:
                del subtrie[previous_word]

            # the current subtrie is empty
            if len(subtrie) == 0:
                previous_word = word
            else:
                previous_word = None

        if previous_word is not None:
            del self.trie[previous_word]

        # update ngram count
        self.ngram_count -= 1
        return True

    def insert_ngram(self, ngram, data):
        """Insert ngram into trie

        Args:
            ngram : List[str]
                ngram in the form of a string list.
            
            data : Any
                Any object representing the inserting ngram

        Examples:
            >>> from ngrammatcher import NGramMatcher
            >>> ngm = NGramMatcher()
            >>> ngm.insert_ngram(['programming', 'language'], 'programming language')
        """
        head = self.trie

        for word in ngram:
            if word not in head:
                head[word] = {}
            head = head[word]

        # if absent, add data word to node in trie
        if self.end_boundary_tag not in head:
            head[self.end_boundary_tag] = data
            self.ngram_count += 1

    def get_all_ngrams(self, keys_only=False):
        """Return a list of all ngrams

        Args:
            keys_only : bool
                If True only return the ngram keys and not the values. Defaults
                to False.

        Returns:
            ngrams : List[List[str]]
                List of all ngrams in the trie

        Examples:
            >>> from ngrammatcher import NGramMatcher
            >>> ngm = NGramMatcher()
            >>> ngram = ['programming', 'language']
            >>> ngm[ngram] = 'programming language'
            >>> ngm.get_all_ngrams(keys_only=True)
            [['programming', 'language']]
            >>> ngm.get_all_ngrams()
            [(['programming', 'language'], 'programming language')]
        """
        ngrams = []

        stack = []
        for key in self.trie:
            stack.append(([key], self.trie[key]))

        while stack:
            key, subtrie = stack.pop(-1)
            if self.end_boundary_tag in subtrie:
                ngrams.append((key, subtrie[self.end_boundary_tag]))
            
            for subkey in subtrie:
                if subkey != self.end_boundary_tag:
                    stack.append((key+[subkey], subtrie[subkey]))

        if keys_only:
            return [ngram[0] for ngram in ngrams]
        return ngrams

    def match_ngrams(self, words, span_info=False):
        """Finds ngrams from the list of provided words.

        Args:
            words : List[str]
                List of words to be matched to ngrams

            span_info : bool
                True to return indicies of words correlating to ngram matches

        Returns:
            ngrams : List[str]
                List of ngrams found from input word list

        Examples:
            >>> from ngrammatcher import NGramMatcher
            >>> ngm = NGramMatcher()
            >>> ngram = ['programming', 'language']
            >>> ngm[ngram] = 'programming language'
            >>> ngm.find(['Python', 'is', 'a', 'programming', 'language'])
            ['programming language']
        """
        if not words:
            return []

        ngrams = []

        start_pos = None
        end_pos = None
        not_end = None
        ngram = None
        head = self.trie

        i = 0
        while i < len(words):
            # get current word
            word = words[i]

            # 1. word is in subtrie
            if word in head:
                head = head[word]
                if start_pos is None:
                    start_pos = i
                end_pos = i+1

                if self.end_boundary_tag in head:
                    ngram = (head[self.end_boundary_tag], start_pos, end_pos)
                    not_end = None
                elif not_end:
                    pass
                else:
                    not_end = i
                i += 1

            # 2. word is not in subtrie
            elif word not in head:
                # found an ngram
                head = self.trie
                if ngram is not None:
                    ngrams.append(ngram)
                    ngram = None
                    if not_end:
                        i = not_end
                    else:
                        i = end_pos
                    start_pos = None
                    end_pos = None
                    not_end = None

                # no ngram found
                else:
                    if start_pos is not None:
                        i = start_pos+1
                    else:
                        i += 1
                    start_pos = None
                    end_pos = None

        if ngram is not None:
            ngrams.append(ngram)

        if not span_info:
            return [w[0] for w in ngrams]
        return ngrams