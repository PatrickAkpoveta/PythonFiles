import itertools

grades1 = {"H8(0-29)": 0,
          "H7(30-39)": 37,
          "H6(40-49)": 46,
          "H5(50-59)": 56,
          "H4(60-69)": 66,
          "H3(70-79)": 77,
          "H2(80-89)": 88,
          "H1(90-100)": 100
            }
   
grades2 = {"H8(0-29)": 0,
          "H7(30-39)": 37,
          "H6(40-49)": 46,
          "H5(50-59)": 56,
          "H4(60-69)": 66,
          "H3(70-79)": 77,
          "H2(80-89)": 88,
          "H1(90-100)": 100
            }
   
grades3 = {"H8(0-29)": 0,
          "H7(30-39)": 37,
          "H6(40-49)": 46,
          "H5(50-59)": 56,
          "H4(60-69)": 66,
          "H3(70-79)": 77,
          "H2(80-89)": 88,
          "H1(90-100)": 100
            }
   
grades4 = {"H8(0-29)": 0,
          "H7(30-39)": 37,
          "H6(40-49)": 46,
          "H5(50-59)": 56,
          "H4(60-69)": 66,
          "H3(70-79)": 77,
          "H2(80-89)": 88,
          "H1(90-100)": 100
            }
   
grades5 = {"H8(0-29)": 0,
          "H7(30-39)": 37,
          "H6(40-49)": 46,
          "H5(50-59)": 56,
          "H4(60-69)": 66,
          "H3(70-79)": 77,
          "H2(80-89)": 88,
          "H1(90-100)": 100
            }
   
grades6 = {"H8(0-29)": 0,
          "H7(30-39)": 37,
          "H6(40-49)": 46,
          "H5(50-59)": 56,
          "H4(60-69)": 66,
          "H3(70-79)": 77,
          "H2(80-89)": 88,
          "H1(90-100)": 100
            }
   

print("Do you do higher level maths?")
answer = input()
while True:
    print("How many points do you need?")
    hope = input()
    if answer.lower() == "yes":
        total = 25
    else:
        total = 0

    result = list(itertools.product(grades1.items(), grades2.items(), grades3.items(), grades4.items(), grades5.items(), grades6.items()))
    grades = []
    gradesOrd = []
    prevTotal = 626
    buffer = 0
    totalAct = 625
    gradesAct = ["H1", "H1", "H1", "H1", "H1", "H1"]
    for x in result:
        if answer.lower() == "yes":
            total = 25
        else:
            total = 0 
        grades = []
        points = 0
        for i in range(6):
            points = x[i][1]
            grade = x[i][0]
            total += points
            grades.append(grade)
        if total == 625:
            print("Done. These grades add up to " + str(totalAct) + " Here are the lowest possible grades you need to get your course(I believe in you):")
            for h in gradesAct:
                print(h)
        if total >= int(hope):
            if total <= prevTotal:
                prevTotal = total
                if total == prevTotal:
                    gradesAct = grades
                    totalAct = total
                
    
