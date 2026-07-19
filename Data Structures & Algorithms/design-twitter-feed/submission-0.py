class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        user_follows = self.follows[userId] | {userId}

        max_heap = []
        for u in user_follows:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                ts, tweet = self.tweets[u][idx]
                heapq.heappush(max_heap, (-ts, tweet, u, idx))
        

        res = []

        while max_heap and len(res) < 10:
            ts, tweet, u, idx = heapq.heappop(max_heap)

            res.append(tweet)
            if idx > 0:
                prev_idx = idx - 1
                prev_ts, prev_tweet = self.tweets[u][prev_idx]
                heapq.heappush(max_heap, (-prev_ts, prev_tweet, u, prev_idx))
            
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
