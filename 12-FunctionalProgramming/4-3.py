grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
more_than = list(filter(lambda x: x>2.0,grades))
mean=round(sum(more_than)/len(more_than),2)
print(f"Arithmetic mean for grades <> 2.0 is {mean}")