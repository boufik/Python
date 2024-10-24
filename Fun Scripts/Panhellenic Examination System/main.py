print("***************** RULE 1 *****************")
maxGrade1 = int(input("Max grade 1: "))
maxGrade2 = int(input("Max grade 2: "))
maxGrade3 = int(input("Max grade 3: "))
maxGrade4 = int(input("Max grade 4: "))
while maxGrade1 + maxGrade2 + maxGrade3 + maxGrade4 != 20000:
    maxGrade1 = int(input("Max grade 1: "))
    maxGrade2 = int(input("Max grade 2: "))
    maxGrade3 = int(input("Max grade 3: "))
    maxGrade4 = int(input("Max grade 4: "))
print()
print("*****************  PLAFON ******************")
plafon = int(input("Plafon = "))
print()
print("******** STUDENT GRADES (MAX = 100) ********")
grade1 = float(input("Grade 1: "))
grade2 = float(input("Grade 2: "))
grade3 = float(input("Grade 3: "))
grade4 = float(input("Grade 4: "))
grade = grade1 * maxGrade1 + grade2 * maxGrade2 + grade3 * maxGrade3 + grade4 * maxGrade4
grade /= 100
grade = int(grade)
print()
if grade > plafon:
    print("Grade = " + str(grade) + " > " + str(plafon))
    print("You passed!")
elif grade < plafon:
    print("Grade = " + str(grade) + " < " + str(plafon))
    print("You did not pass...")
else:
    print("Grade = " + str(grade) + " = " + str(plafon))
    print("You passed!")