scores = [45,78,33,61,59,78]

scores = list(set(scores))
scores.sort()

print("Runner-up score:", scores[-2])