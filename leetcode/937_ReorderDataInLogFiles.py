class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []

        for ele in logs:
            if ele.split()[1].isdigit():
                digit.append(ele)
            else:
                letter.append(ele)
        
        letter.sort(key = lambda x : (x.split()[1:], x.split()[0]))

        return letter+digit
