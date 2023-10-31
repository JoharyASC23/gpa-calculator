#intro

print('Utilize the list of class levels below to calculate your total GPA.')
print('------------')
print('AP+')
print('AP')
print('Honors')
print('CP')
print('------------')
# weighting
HAP = [5.5, 4.4, 3.5, 2.5, 1.5]
AP = [5, 4, 3, 2, 1]
HON = [4.5, 3.5, 2.5, 1.5, .5]
CPC = [4, 3, 2, 1, 0]

# questions
Q1 = ["What is your class level? Type 'x' to calculate. ", "What is your grade in that class? "]
BaseGPA = 0
NumOfClasses = 1

gpa1 = 0
gpa2 = 0
gpa3 = 0
gpa4 = 0
gpa5 = 0
gpa6 = 0
gpa7 = 0
gpa7 = 0
gpa8 = 0
gpa9 = 0
gpa10 = 0
gpa11 = 0
gpa12 = 0
gpa13 = 0
gpa14 = 0
gpa15 = 0
gpa16 = 0
gpa17 = 0
gpa18 = 0
gpa19 = 0
gpa20 = 0

#singular gpa calculation
while True:
  level=input(Q1[0])
  if level != 'x':
    grade=input(Q1[1])
  
  NumOfClasses += 1
  ActualNum = NumOfClasses-2
  

  if level == "AP+" and grade == "A":
    gpa1 = HAP[0]
    BaseGPA += gpa1
    gpa1 = 0

  if level == "AP+" and grade == "B":
    gpa2 = HAP[1]
    BaseGPA += gpa2
    gpa2 = 0
  if level == "AP+" and grade == "C":
    gpa3 = HAP[2]
    BaseGPA += gpa3
    gpa3 = 0
  if level == "AP+" and grade == "D":
    gpa4 = HAP[3]
    BaseGPA += gpa4
    gpa4 = 0
  
  if level == "AP+" and grade == "F":
    gp5 = HAP[4]
    BaseGPA += gpa5
    gpa5 = 0
  #AP ---

  if level == "AP" and grade == "A":
    gpa6 = AP[0]
    BaseGPA += gpa6
    gpa6 = 0
  if level == "AP" and grade == "B":
    gpa7 = AP[1]
    BaseGPA += gpa7
    gpa7 = 0
    
  if level == "AP" and grade == "C":
    gpa8 = AP[2]
    BaseGPA += gpa8
    gpa8 = 0

  if level == "AP" and grade == "D":
    gpa9 = AP[3]
    BaseGPA += gpa9
    gpa9 = 0
    

  if level == "AP" and grade == "F":
    gpa10 = AP[4]
    BaseGPA += gpa10
    gpa10 = 0

  
  #HON ---

  if level == "Honors" and grade == "A":
    gpa11 = HON[0]
    BaseGPA += gpa11
    gpa11 = 0

  if level == "Honors" and grade == "B":
    gpa12 = HON[1]
    BaseGPA += gpa12
    gpa12 = 0

  if level == "Honors" and grade == "C":
    gpa13 = HON[2]
    BaseGPA += gpa13
    gpa13 = 0

  if level == "Honors" and grade == "D":
    gpa14 = HON[3]
    BaseGPA += gpa14
    gpa14 = 0

  if level == "Honors" and grade == "F":
    gpa15 = HON[4]
    BaseGPA += gpa15
    gpa15 = 0

  #CP ---

  if level == "CP" and grade == "A":
    gpa16 = CPC[0]
    BaseGPA += gpa16
    gpa16 = 0

  if level == "CP" and grade == "B":
    gpa17 = CPC[1]
    BaseGPA += gpa17
    gpa17 = 0

  if level == "CP" and grade == "C":
    gpa18 = CPC[2]
    BaseGPA += gpa18
    gpa18 = 0

  if level == "CP" and grade == "D":
    gpa19 = CPC[3]
    BaseGPA += gpa19
    gpa19 = 0

  if level == "CP" and grade == "F":
    gpa20 = CPC[4]
    BaseGPA += gpa20
    gpa20 = 0

  if level == 'x' and ActualNum > 0:
    
    
    FinGPA = round(BaseGPA/ActualNum, 3)

    print('Your GPA is: ', FinGPA)
    break

  if level == 'x' and ActualNum == 0:


    

    print('Your GPA is: None')
    break



  # testing print('Your BaseGPA is: ', BaseGPA)   print('Your ActualNum is: ', ActualNum)

#HAP ---

