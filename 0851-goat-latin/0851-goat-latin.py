class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel={"a","e","i","o","u","A","E","I","O","U"}
        words=sentence.split()

        for i in range(len(words)):
            word=words[i]
            if word[0] in vowel:
                words[i] = word+'ma'+'a'*(i+1)
            else:
                words[i] = word[1:]+word[0]+'ma'+'a'*(i+1)

        return " ".join(words)

# Time :O(O(n + k²))
# Space:O(n + k²)