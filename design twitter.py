class Twitter:
    tweetsList=[]
    followers={}
    def __init__(self):
        self.tweetsList=[]
        self.followers={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsList.append([userId,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        lst=[]
        for i in range(len(self.tweetsList)-1,-1,-1):
            if self.tweetsList[i][0]==userId:
                lst.append(self.tweetsList[i][1])
                if (len(lst)==10):
                    break
            else:
                if userId in self.followers:
                    val=self.followers[userId]
                    if self.tweetsList[i][0] in val:
                        lst.append(self.tweetsList[i][1])
                        if (len(lst)==10):
                            break
        return lst


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            val=self.followers[followerId]
            val.append(followeeId)
            self.followers[followeeId]=val
        else:
            lst=[followeeId]
            self.followers[followerId]=lst

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            val=self.followers[followerId]
            val.remove(followeeId)
            self.followers[followerId]=val
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
