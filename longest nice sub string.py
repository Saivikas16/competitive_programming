class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        windowsize = len(s)
        while windowsize >1:
            slidecount = len(s)-windowsize +1
            index=0
            while slidecount>0:
                mp={}
                tmpstr=s[index:windowsize+index]
                for i in tmpstr:
                    if i not in mp:
                        j=i.swapcase()
                        if j in mp:
                            mp[j]=2
                        else:
                            mp[i]=1
                for i,j in mp.items():
                    if j==1:
                        break
                else:
                    return tmpstr
                index+=1
                slidecount-=1
            windowsize-=1
        return ""
