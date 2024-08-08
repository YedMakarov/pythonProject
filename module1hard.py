
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

temp_l = sorted(students)
grades_stud = (sum(grades[0])/len(grades[0]),
               sum(grades[1])/len(grades[1]),
               sum(grades[2])/len(grades[2]),
               sum(grades[3])/len(grades[3]),
               sum(grades[4])/len(grades[4]))

students_grades = {temp_l[0]: grades_stud[0],
                   temp_l[1]: grades_stud[1],
                   temp_l[2]: grades_stud[2],
                   temp_l[3]: grades_stud[3],
                   temp_l[4]: grades_stud[4]}
print(students_grades)

# -= Result =-
#-----------------------------------------------------------------
#{'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}