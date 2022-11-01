# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def suma():
    # Use a breakpoint in the code line below to debug your script.
    print(f'introduceti primul numar, a')  # Press Ctrl+F8 to toggle the breakpoint.
    a = input()
    print('a=', a)
    print(f'introduceti al 2-lea  numar, a')  # Press Ctrl+F8 to toggle the breakpoint.
    b = input()
    print('b=', b)
    print('a+b=', int(a)+int(b))


def scadere():
    # Use a breakpoint in the code line below to debug your script.
    print(f'introduceti primul numar, a')  # Press Ctrl+F8 to toggle the breakpoint.
    a = input()
    print('a=', a)
    print(f'introduceti al 2-lea  numar, a')  # Press Ctrl+F8 to toggle the breakpoint.
    b = input()
    print('b=', b)
    print('a-b=', int(a)-int(b))


def inmultire():
    # Use a breakpoint in the code line below to debug your script.
    print(f'introduceti primul numar, a')  # Press Ctrl+F8 to toggle the breakpoint.
    a = input()
    print('a=', a)
    print(f'introduceti al 2-lea  numar, a')  # Press Ctrl+F8 to toggle the breakpoint.
    b = input()
    print('b=', b)
    print('a*b=', int(a)*int(b))


def impartire():
    # Use a breakpoint in the code line below to debug your script.
    print(f'introduceti primul numar, a')  # Press Ctrl+F8 to toggle the breakpoint.
    a = input()
    print('a=', a)
    print(f'introduceti al 2-lea  numar, a')  # Press Ctrl+F8 to toggle the breakpoint.
    b = input()
    print('b=', b)
    print('a/b=', int(a)/int(b))

def arietd():
     # Use a breakpoint in the code line below to debug your script.
    print(f'introduceti prima cateta, (ab)')  # Press Ctrl+F8 to toggle the breakpoint.
    a = input()
    print('ab=', a)
    print(f'introduceti al 2-cateta, (ac)')  # Press Ctrl+F8 to toggle the breakpoint.
    b = input()
    print('ac=', b)
    print('aria unui triunghi dreptunghic este c1*c2/2 =', int(a) * int(b) / 2)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('suma')
    suma()
    print('scadere')
    scadere()
    print('inmultire')
    inmultire()
    print('impartire')
    impartire()
    print('arietd')
    arietd()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
