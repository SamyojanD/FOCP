# The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. A lab group is 24 students, since this is the number of PCs in a lab. Write a program that calculates how many groups are needed for the following number of students: 113, 175, 12. Display how many full groups there will be, and how many students will be in the smaller "left over" group.

grp_s = 24
class_s = [113, 175, 12]
for stu in class_s:
    full_grp = stu // grp_s
    left_overs = stu % grp_s
    print ("For", stu, "no. of students:")
    print ("No. of full groups: ", full_grp)
    print ("No. left over students: ", left_overs)


