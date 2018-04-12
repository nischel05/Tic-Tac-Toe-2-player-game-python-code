matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
zz = 0
xx = 0
cc = 0
vv = 0
bb = 0
nn = 0
mm = 0
ll = 0
kk = 0
z = 0
x = 0
c = 0
v = 0
b = 0
n = 0
m = 0
l = 0
k = 0
w = 0
q = 0
win = 0
nis = 0
moves = 0


def playerassignment():
    global q
    global w
    global moves
    if q % 2 == 0:
        print('its player Xs turn')
        w = 0
    if q % 2 != 0:
        print('its player Os turn')
        w = 1
    q = q + 1
    moves = moves + 1


def takeinput():
    global zz
    global xx
    global cc
    global vv
    global bb
    global nn
    global mm
    global ll
    global kk
    global z
    global x
    global c
    global v
    global b
    global n
    global m
    global l
    global k
    qq = int(input("please enter the position of your marker from 1-9, left to right "))
    if qq == 1 and zz != 2:
        z = 1
        zz = 2

    elif qq == 2 and xx != 2:
        x = 1
        xx = 2

    elif qq == 3 and cc != 2:
        c = 1
        cc = 2

    elif qq == 4 and vv != 2:
        v = 1
        vv = 2

    elif qq == 5 and bb != 2:
        b = 1
        bb = 2

    elif qq == 6 and nn != 2:
        n = 1
        nn = 2

    elif qq == 7 and mm != 2:
        m = 1
        mm = 2

    elif qq == 8 and ll != 2:
        l = 1
        ll = 2

    elif qq == 9 and kk != 2:
        k = 1
        kk = 2

    if qq > 9:
        print('Wrong input, only enter numbers between 1-9')
    if qq < 1:
        print('Wrong input, only enter numbers between 1-9')


def addtogame():
    global zz
    global xx
    global cc
    global vv
    global bb
    global nn
    global mm
    global ll
    global kk
    global z
    global x
    global c
    global v
    global b
    global n
    global m
    global l
    global k
    global w
    global matrix
    if z == 1 and w == 0:
        matrix[0] = 'x'
        z = 0

    if z == 1 and w == 1:
        matrix[0] = 'o'
        z = 0

    if x == 1 and w == 0:
        matrix[1] = 'x'
        x = 0

    if x == 1 and w == 1:
        matrix[1] = 'o'
        x = 0

    if c == 1 and w == 0:
        matrix[2] = 'x'
        c = 0

    if c == 1 and w == 1:
        matrix[2] = 'o'
        c = 0

    if v == 1 and w == 0:
        matrix[3] = 'x'
        v = 0

    if v == 1 and w == 1:
        matrix[3] = 'o'
        v = 0

    if b == 1 and w == 0:
        matrix[4] = 'x'
        b = 0

    if b == 1 and w == 1:
        matrix[4] = 'o'
        b = 0

    if n == 1 and w == 0:
        matrix[5] = 'x'
        n = 0

    if n == 1 and w == 1:
        matrix[5] = 'o'
        n = 0

    if m == 1 and w == 0:
        matrix[6] = 'x'
        m = 0

    if m == 1 and w == 1:
        matrix[6] = 'o'
        m = 0

    if l == 1 and w == 0:
        matrix[7] = 'x'
        l = 0

    if l == 1 and w == 1:
        matrix[7] = 'o'
        l = 0

    if k == 1 and w == 0:
        matrix[8] = 'x'
        k = 0

    if k == 1 and w == 1:
        matrix[8] = 'o'
        k = 0


def showgame():
    global matrix
    print(matrix[0], '   ', matrix[1], '   ', matrix[2])
    print(matrix[3], '   ', matrix[4], '   ', matrix[5])
    print(matrix[6], '   ', matrix[7], '   ', matrix[8])


def checkwin():
    global win
    global matrix
    global nis
    global moves
    if matrix[0] == matrix[1] == matrix[2]:
        if matrix[0] == 'x':
            print('x PLAYER WON')
            showgame()
        if matrix[0] == 'o':
            print('o PLAYER WON')
            showgame()
        win = 1
        nis = 1
        moves = moves + 1
    if matrix[3] == matrix[4] == matrix[5]:
        if matrix[3] == 'x':
            print('x PLAYER WON')
            showgame()
        if matrix[3] == 'o':
            print('o PLAYER WON')
            showgame()
        win = 1
        nis = 1
        moves = moves + 1
    if matrix[6] == matrix[7] == matrix[8]:
        if matrix[6] == 'x':
            print('x PLAYER WON')
            showgame()
        if matrix[6] == 'o':
            print('o PLAYER WON')
            showgame()
        win = 1
        nis = 1
        moves = moves + 1
    if matrix[0] == matrix[4] == matrix[8]:
        if matrix[0] == 'x':
            print('x PLAYER WON')
            showgame()
        if matrix[0] == 'o':
            print('o PLAYER WON')
            showgame()
        win = 1
        nis = 1
        moves = moves + 1
    if matrix[2] == matrix[4] == matrix[6]:
        if matrix[2] == 'x':
            print('o PLAYER WON')
            showgame()
        if matrix[2] == 'o':
            print('o PLAYER WON')
            showgame()
        win = 1
        nis = 1
        moves = moves + 1
    if matrix[0] == matrix[3] == matrix[6]:
        if matrix[0] == 'x':
            print('o PLAYER WON')
            showgame()
        if matrix[0] == 'o':
            print('o PLAYER WON')
            showgame()
        win = 1
        nis = 1
        moves = moves + 1
    if matrix[1] == matrix[4] == matrix[7]:
        if matrix[1] == 'x':
            print('x PLAYER WON')
            showgame()
        if matrix[1] == 'o':
            print('y PLAYER WON')
            showgame()
        win = 1
        nis = 1
        moves = moves + 1
    if matrix[2] == matrix[5] == matrix[8]:
        if matrix[2] == 'x':
            print('x PLAYER WON')
            showgame()
        if matrix[2] == 'o':
            print('y PLAYER WON')
            showgame()
        win = 1
        nis = 1
        moves = moves + 1
    if moves == 9:
        if win == 0:
            nowin()


def nowin():
    global matrix
    global zz
    global xx
    global cc
    global vv
    global bb
    global nn
    global mm
    global ll
    global kk
    global z
    global x
    global c
    global v
    global b
    global n
    global m
    global l
    global k
    global w
    global q
    print('no one won, its a draw!')
    matrix[0] = 1
    matrix[1] = 2
    matrix[2] = 3
    matrix[3] = 4
    matrix[4] = 5
    matrix[5] = 6
    matrix[6] = 7
    matrix[7] = 8
    matrix[8] = 9
    zz = 0
    xx = 0
    cc = 0
    vv = 0
    bb = 0
    nn = 0
    mm = 0
    ll = 0
    kk = 0
    z = 0
    x = 0
    c = 0
    v = 0
    b = 0
    n = 0
    m = 0
    l = 0
    k = 0
    w = 0
    q = 0


while win != 1:
    showgame()
    playerassignment()
    takeinput()
    addtogame()
    checkwin()






