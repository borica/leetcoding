class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            # Creating an array of 26 positions with 0 as default value
            count = [0] * 26

            # iterate over string letter
            for c in s:
                # append to count array the corresponding position in the alphabet
                # need to subtract the actual ord(c) from ord("a") so that it starts from 0
                count[ord(c) - ord("a")] += 1

            # uses the tuple of the count list as key and append the string to this group
            groups[tuple(count)].append(s)

        return groups.values()
                