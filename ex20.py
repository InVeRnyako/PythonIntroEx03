# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Пример:
# Ввод:
# ноутбук
# Вывод:
# 12

points_eng = {1: "aeioulnstr", 2: "dg", 3: "bcmp", 4: "fhvwy", 5: "k", 8: "jx", 10: "qz"}
points_rus = {1: "авеинорст", 2: "дклмпу", 3: "бгёья", 4: "йы", 5: "жзчцч", 8: "шэю", 10: "фщъ"}

score = 0
word = input().lower()

for i in word:
    if i in "aeioulnstrdgbcmpfhvwykjxqz":
        for j in points_eng:
            if i in points_eng[j]:
                score += j
    else:
        for j in points_rus:
            if i in points_rus[j]:
                score += j

print(score)