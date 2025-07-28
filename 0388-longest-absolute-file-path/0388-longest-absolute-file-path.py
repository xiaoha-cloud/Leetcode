class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}  # level 0 starts with length 0

        for line in input.split('\n'):
            level = line.count('\t')  # count how deep the file/dir is
            name = line.lstrip('\t')  # actual name of file or dir

            if '.' in name:
                # is a file, compute total length
                max_len = max(max_len, path_len[level] + len(name))
            else:
                # is a dir, update the path length for next level
                path_len[level + 1] = path_len[level] + len(name) + 1  # +1 for the "/"

        return max_len

# O(n) 
# O(d) 