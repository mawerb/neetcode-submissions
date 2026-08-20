class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return -1

        trusted = dict()
        potential = set()

        for people in trust:
            trusted_person = people[1]

            if trusted_person not in trusted:
                trusted[trusted_person] = 0

            trusted[trusted_person] += 1

            if (people[0] in potential):
                potential.remove(people[0])

            if (trusted[trusted_person]) == n-1:
                potential.add(trusted_person)
        
        if (potential):
            return potential.pop()
        return -1
