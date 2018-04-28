from num2words import num2words
from random import randint
from sympy import *
# print(num2words(213, lang='de'))


def generate_type_1():
    rand1 = randint(1, 1000)
    rand2 = randint(1, 1000)
    q = "Gesucht sind 3 Zahlen x, y und z. Die Summe der 3 Zahlen beträgt {}. Addiert man zu der zweiten Zahl das doppelter der dritten Zahl, so erhält man {}. Die dritte Zahl ist vier. Finde die Werte der Variablen.".format(rand1, rand2)
    z = 4
    y = rand2-z
    x = rand1 - y - z
    a = (x, y, z)
    return q, a


def generate_type_2():
    rand_a_c1 = randint(1, 1000)
    rand_a_c2 = randint(1, 1000)
    rand_a_d = randint(1, 1000)
    rand_b_c1 = randint(1, 1000)
    rand_b_c2 = randint(1, 1000)
    rand_b_d = randint(1, 1000)
    q = "Vereinfache a) {}*sqrt({})-{}*sqrt({}) b) {}*sqrt({})+{}*sqrt({})".format(
        rand_a_c1, rand_a_d, rand_a_c2, rand_a_d,
        rand_b_c1, rand_b_d, rand_b_c2, rand_b_d
    )
    q_solve = q[15:len(q)]
    q_solve_split = q_solve.split(' b) ')
    pt1 = simplify(q_solve_split[0])
    pt2 = simplify(q_solve_split[1])

    return q, (pt1, pt2)


file = open("test_questions_1_1000.txt", 'w')
for i in range(0, 1000):
    q, a = generate_type_1()
    file.write(str(q) + "\n" + str(a) + "\n")

file = open("test_questions_2_1000.txt", 'w')
for i in range(0, 1000):
    q, a = generate_type_2()
    file.write(str(q) + "\n" + str(a) + "\n")

"""
q3 = "Löse die gradratischen Gleichungen rechnerisch a) 0,5x^2+2x-6 = 0 b) -(x-3)^2 = -4 c) x^2-4x+4 = -9",
q4 = "Ermittle die Schnittpunkte der Parabeln mit den Funktionsgleichungen f(x)=40x-2x^2 und g(x)=x^2-5x+150",
q5 = "In einem Stall leben Hühner und Kaninchen. Alfred zählt 171 Köpfe und 498 Beine. Wie viele Hühner und wie viele Kaninchen wohnen in diesem Stall?",
q6 = "Ein leeres Schwimmbecken kann durch die Zuflussleitung in 15 Stunden gefüllt werden. Ist das Becken voll, so dauert es 20 Stunden, um das Wasser wieder ablaufen zu lassen.Das Becken ist leer. Die Besitzerin will es füllen, vergisst jedoch, den Ablauf zu schliessen. Wie lange dauert es, bis das Schwimmbecken trotzdem voll ist?",
q7 = "Eine zweiziffrige Zahl hat die Quersumme 12. Werden die Ziffern vertauscht, so wird die Zahl 1.75-Mal so gross. Welche Zahl hat diese Eigenschaft?"
"""