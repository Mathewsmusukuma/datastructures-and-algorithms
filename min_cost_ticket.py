from bisect import bisect_left

def mincostTickets(days, costs):
    """
    :type days: List[int]
    :type costs: List[int]
    :rtype: int
    """
    dp = [0]+[min(costs)*i for i in range(1,len(days)+1)]
    for i in range(1,len(days)):
        one = dp[i]+costs[0]
        a = bisect_left(days,days[i]-6)
        seven = dp[a]+costs[1]
        b = bisect_left(days,days[i]-29)
        thirty = dp[b]+costs[2]
        dp[i+1] = min(one,seven,thirty)
    return dp[-1]
        