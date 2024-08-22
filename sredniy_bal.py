grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
print(students)
sred_bal = [sum(grades[0])/len(grades[0]),
            sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]),
            sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4])]
print(sred_bal)
jurnal = {students[0]: sred_bal[0],
          students[1]: sred_bal[1],
          students[2]: sred_bal[2],
          students[3]: sred_bal[3],
          students[4]: sred_bal[4]}
print(jurnal)
