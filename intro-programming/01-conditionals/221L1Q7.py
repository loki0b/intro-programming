city1 = input()
grade1 = float(input())
distance1 = int(input())

city2 = input()
grade2 = float(input())
distance2 = int(input())

city3 = input()
grade3 = float(input())
distance3 = int(input())

if grade1 < 4 and grade2 < 4 and grade3 < 4:
    print('Nota mínima não atingida')
elif grade1 > grade2 and grade1 > grade3:
    print(city1)
elif grade2 > grade3:
    print(city2)
elif grade3 > grade2:
    print(city3)
elif (grade1 == grade2 and grade1 == grade3) or (grade1 == grade2) or (grade2 == grade3) or (grade3 == grade1):
    if distance1 < distance2 and distance1 < distance3:
        print(city1)
    elif distance2 < distance3:
        print(city2)
    else:
        print(city3)
