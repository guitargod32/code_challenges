class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        final = []
        medals = {1:"Gold Medal", 2:"Silver Medal", 3:"Bronze Medal"} #set medal names
        sscore = sorted(score, reverse=True) #sort score from winner to loser
        mel = sscore[:3] #slice off first 3 as winners, so we can check if they are medal winner

        for i in range(len(sscore)): #range is num to iterate through score and use it to build final, with ability to access sorted list
            if score[i] in mel:
                final.append(medals[mel.index(score[i])+1]) #add one because athletes index at 1 instead of 0
            else:
                final.append(str(sscore.index(score[i])+1)) #still gotta index, yo              
        return final