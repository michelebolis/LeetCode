from typing import List
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        max_score = 0
        min_power = 0
        max_power = len(tokens) - 1
        while min_power <= max_power :
            if power >= tokens[min_power]:
                power -= tokens[min_power]
                score += 1
                min_power += 1
                max_score = max(max_score, score)
            elif score > 0 :
                power += tokens[max_power]
                score -= 1
                max_power -= 1
            else : break
        return max_score