values = [48,47,54,50,42,68,39,46]
higher=list(filter(lambda x:x>50, values))
print(f"Recorded values: {values}")
print(f"Speed too high: {higher}")