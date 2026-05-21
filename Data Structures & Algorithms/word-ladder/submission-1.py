class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        Time and Space Complexity 
        TC :
        O(n) - queue will execute
        Internal loop - O(m)- length of the word
        creating one new word - O(m)
        total is - O(m*m*26)
        Total TC - O(n* m^2)
        Space - O(n*m)
        '''
        if endWord not in wordList:
            return 0
        
        word_set = set(wordList)
        word_set.add(beginWord)

        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            word_set.discard(word)

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] != c:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in word_set:
                            queue.append((new_word, steps+1))
        return 0
                            
        