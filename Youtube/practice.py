def ave_score(marks):
    ave_sum = sum(marks)
    num_obj = len(marks)
    total_ave = ave_sum / num_obj
    return total_ave

def grade_letter(total_ave):
    if total_ave >= 80:
        grade = 'A'
    elif total_ave >= 70:
        grade = 'B'
    elif total_ave >= 60:
        grade = 'C'
    else:
        grade = 'F'
    return grade 

marks = [80, 90, 90, 74, 84]
average =  ave_score(marks)
grade = grade_letter(average)
print("Your test score is:",average)
print("Your letter grade is:",grade)
