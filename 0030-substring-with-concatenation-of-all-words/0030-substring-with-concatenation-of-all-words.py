from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
    # define r l for position
    # counter
    # word_len num_len
    # res  --> 0
    # initialize

        word_len=len(words[0])
        num_len=len(words)
        window_len = num_len*word_len
        win_count= Counter(words)
        res = []

    # while the right + word_len < total len:
    #   1. take out the word + update the right positiion
    #   2. if the word in the counter ->update the curr_count
    #   3. when the curr_count is larger then the start to shrink and record the left position
    #   4.  if the word is not in the counter--》 update the curr——count and left position
        for i in range(word_len):
            l=i
            r=i
            curr_count = Counter()

            while r+word_len<=len(s):
                word=s[r:r+word_len]
                r=r+word_len
                if word in win_count:
                    curr_count[word]+=1
                    while curr_count[word]> win_count[word]:
                        curr_count[s[l:l+word_len]]-=1
                        l+=word_len
                    if r-l == window_len:
                        res.append(l)
                else:
                    curr_count.clear()
                    l=r

        return res

                    