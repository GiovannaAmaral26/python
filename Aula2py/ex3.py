#1:
A = 10
B = 15
C = 4
print((A < B and A < C) or C != 0) # Resultado: True
#:
A = 10
B = 15
C = 4
print(A < B and (A < C or C != 0)) # Resultado: True
#3:
A = 1
B = 9
C = 0
print(not (A >= 0 and B == C)) # Resultado: True
#4:
A = 1
B = 9
C = 9
print(not (A >= 0) and not (B == C)) # Resultado: False
#5:
A = 1
B = 9
C = 0
print(A >= 0 or (B == C and B > A)) # Resultado: True
#6:
A = 0
B = 1
C = 0
print(A == 0 and B != 0 and C == 0) # Resultado: True
#7:
A = -2
B = 0
C = 2
print(not (A <= B) or C > B) # Resultado: True
#8:
A = -2
B = 0
C = 2
print(not (A <= 0 or C > B)) # Resultado: False
#9:
A = 5
B = 0
C = 0
print(A == 0 and B != 0 and C == 0) # Resultado: False
#10:
A = 5
B = 0
C = 0
print(A == 0 or B != 0 or C == 0) # Resultado: True