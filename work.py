day = int(input('Введите день недели: '))
if day > 7 or day < 1:
 print('Попробуй еще раз: ')
elif day == 6 or day == 7:
 print("Ура, выходной!")
else:
 print("Упс, не выходной!")