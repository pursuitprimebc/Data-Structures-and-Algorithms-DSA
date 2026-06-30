''' PROBLEM -  Teemo Attacking
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is 
poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned. 
'''


class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total = duration
        for i in range(len(timeSeries) - 1):
            currentime =  timeSeries[i]
            nexttime = timeSeries[i+1]

            real = min(duration, nexttime - currentime)
            total += real
        return total
