def calc_grade(sub1,sub2,sub3):
    avg=(sub1+sub2+sub3)/3

    if avg>=90:
        grade='O'
    elif avg>=80:
        grade='E'
    elif avg>=70:
        grade='A'
    elif avg>=60:
        grade='B'
    elif avg>=50:
        grade='C'

    return grade

print (calc_grade(67,80,92))

    

