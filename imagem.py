# Gabriel Remigio de Sá e Francisco Sales de Sá Neto
import sys
while True:
    lincol = []
    lincolg = input()
    lincol.append(lincolg.split())
    # print("")
    if int(lincol[0][0]) == 0 or int(lincol[0][1]) == 0:
        sys.exit()
    if int(lincol[0][0]) > 100 or int(lincol[0][1]) > 100:
        sys.exit()
    linhas = []
    for i in range(1, int(lincol[0][0])+1):
        linhag = input()
        linhas.append(linhag.split())
    print("")
    m = 1 
    l = 0
    for k in range(1, int(lincol[0][1])+1):
        while True:
            if m <= int(lincol[0][0]):
                print(linhas[int(lincol[0][0])-m][l], end=' ')
                m += 1
            else:
                print("")
                break
        m = 1
        l += 1
    print("")

