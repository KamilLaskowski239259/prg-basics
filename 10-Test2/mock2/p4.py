my_dict= {
'programming': [3,4,5],
'data notations':[2,1,4],
'physical education':[5,5,5]

}


def f(subjects):
    max_avg=0
    best_subject=""
    for subject,grades in subjects.items():
        avg = sum(grades)/len(grades)
        if avg > max_avg:
            max_avg = avg
            best_subject = subject
    return best_subject
print(f(my_dict))
