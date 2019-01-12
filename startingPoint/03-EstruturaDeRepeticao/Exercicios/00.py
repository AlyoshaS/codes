# Imprima na tela de 1 a 25 em ordem crescente e em ordem decrescente.

for x in range(1, 26):
    print("n° %d " % x)
    
for x in reversed(range(1, 26)):
    print("n° %d REVERSED" % x)

for x in range(9)[::-1]:
    print("n° %d slice" % x)

for x in range(25, -1, -1):
    print("n° %d " % x)

for x in range(25)[:1:-1]:
    print("n° %d slice1" % x)

for x in range(25)[25:1:-2]:
    print("n° %d slice2" % x)

for x in range(25)[25:10:-1]:
    print("n° %d slice3" % x)
