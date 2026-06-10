# criar um programa que leia uma variável nota com input e mostre na tela:
# > 90 "conceito A"
# entre 89 e 71 "conceito B"
# entre 70 e 61 "conceito C"
# entre 60 e 50 "conceito D"
# < 49 "conceito E"

nota = int(input("digite uma nota:"))
if nota > 90:
    print("conceito A")
elif nota <= 89 and nota >= 71:
    print("conceito B")
elif nota <= 70 and nota >= 61:
    print("conceito C")
elif nota <= 60 and nota >= 50:
    print("conceito D")
else:
    print("conceito E")
