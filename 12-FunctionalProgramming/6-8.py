results=[37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
   return list(filter(lambda pts: pts>=limit,results))
print(f"Min 70 pts: {min_pts(70)}")
print(f"Min 40 pts: {min_pts(40)}")
print(f"Min 30 pts: {min_pts(30)}")