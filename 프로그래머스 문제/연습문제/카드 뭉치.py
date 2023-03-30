from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    answer = ''
    while goal:
        target = goal.popleft()
        if cards1:
            c1 = cards1.popleft()
            if c1 == target:
                continue
            else:
                cards1.appendleft(c1)

        if cards2:
            c2 = cards2.popleft()
            if c2 == target:
                continue
        
        return "No"
    
    return "Yes"

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))

