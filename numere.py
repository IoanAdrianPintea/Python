def adunare2():
    print("introduceti va rog un numar de 2 cifre:")
    a = int(input())
    z = a // 10
    u = a % 10
    print("Numarul rezultat prin adunarea zecilor si unitatilor este:", z+u)


def adunare3():
    print("introduceti va rog un numar de 3 cifre:")
    a = int(input())
    s = a // 100
    z = a // 10 % 10
    u = a % 10
    print("Numarul rezultat prin adunarea sutelor, zecilor si unitatilor este:", s+z+u)



def capetesipicioare():
    print("introduceti va rog un numar de oi si gaini:")
    o = int(input())
    print("introduceti va rog numarul de gani:")
    g = int(input())
    print("Numarul de capete:", g+o, ", iar numarul de picioare este:", 2*g+4*o)



def numerereale():
    print("introduceti va rog un numar de 3 cifre:")
    a = int(input())
    s = a // 100
    z = a // 10 % 10
    u = a % 10
    print("Numarul rezultat prin eliminarea cifrei zecilor este:", s*10+U)
    print("Numarul rezultat prin eliminarea cifrei zecilor este:", str(s)+str(u))


def gauss():
    print("Introduceti numarul pentru care se doreste calcularea sumeu lui Gauss:")
    n = int(input())
    print("Suma lui gauss:", n+(n+1)/2)


def ora():
    print("introduceti ora:")
    h = int(input())
    print("Introdeuceti mintele")7
    m = int(input())
    print("Introduceti numarul de minute care se vor aduna la ora si minutele anterior:")
    x = int(input())
    ov = h*60+m+x #ora viitoare exprimata in minute
    print("ora va fi ", ov//60, " si minute", ov%60)
if __name__ == "__main__":
    ora()







