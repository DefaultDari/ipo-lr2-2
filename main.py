
students = int(input("Введите количество школьников: "));
apples = int(input("Введите количество яблок: "));
apples_to_students = apples // students;
leftover_apples = apples % students;
print("Количество яблок для каждого школьника: ", apples_to_students);
print("Количество оставшихся в корзинке яблок: ", leftover_apples);