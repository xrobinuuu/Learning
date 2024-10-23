class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n <= limit:
            candies = [limit, 0, 0]
        elif n - limit > limit:
            candies = [limit, limit, n - 2 * limit]
        else:
            candies = [limit, limit, 0]
        cnt = 1
        print(candies)
        for member, suger in enumerate(candies[:-1]):
            for sug in candies[member + 1:]:
                cnt += suger - sug
        return cnt


if __name__ == '__main__':
    res = Solution().distributeCandies(3, 3)
    print(res)
