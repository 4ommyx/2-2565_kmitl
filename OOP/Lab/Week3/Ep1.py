def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score):
    count,total = 0,0
    for i in subject_score.keys(): 
        # subject_score.keys() หรือ subject_score จะได้ค่า i เป็น key
      total += float(subject_score[i])
      count += 1
      avg = total / count

    return "{:.2f}".format(avg)
    

a = calc_average_score({ 'python' : 50, 'calculus' : 60 })
print(a)
