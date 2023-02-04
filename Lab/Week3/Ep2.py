def add_score(subject_score, student, subject, score):

    if  student not in subject_score:
        subject_score[student] = {subject:score}
    else:
        subject_score[student][subject] = score

    return subject_score

def calc_average_score(subject_score):
    avg = dict()
    for i in subject_score: 
    # i ที่ได้คือ key student
    # subject_score[i] จะได้ dict ที่มี {key:values}
        total = f'{sum(subject_score[i].values())/len(subject_score[i]):.2f}'
        avg[i] = total
    print(subject_score)
    # {'65010001': {'python': 50, 'calculus': 60}}
    print(subject_score[i])
    # {'python': 50, 'calculus': 60}
    print(subject_score[i].keys())
    # (['python', 'calculus'])
    print(subject_score[i].values())
    # ([50, 60])
    return avg

a = add_score({ '65010001' : { 'python' : 50 } }, student = '65010002', subject = 'calculus', score = 60)
print(a)

calc_average_score({'65010001': {'python': 50, 'calculus': 60}})