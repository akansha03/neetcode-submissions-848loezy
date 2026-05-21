class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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
                            
        