import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', int(sys.argv[1])))    #int(sys.argv[1])
s.listen(1)
conn, addr = s.accept()

print("Connected to client!")

C = 5
B = 4
R = 3
S = 3
D = 2


while C != 0 or R != 0 or S != 0 or D != 0 or B != 0:
    #Read board in
    file = sys.argv[2]   #sys.argv[2]
    f = open(file, "r")
    i = 0
    while i < 10:
        print(i, end =" ")
        print(f.readline(), end ="")
        i += 1
    with open(file) as f:
        board = f.readlines()
    board = [row.rstrip('\n') for row in board]
    f.close
    print('  0123456789')

    #Get data
    data = conn.recv(200)
    xi = data.decode('utf-8')
    yi = data.decode('utf-8')
    x = int(xi)
    y = int(yi)


    row = list(board[y])
    if board[y][x] == '_':
        row[x] = 'X'
        conn.send('Miss'.encode('utf-8'))
    elif board[y][x] == 'R':
        row[x] = 'O'
        conn.send('Hit'.encode('utf-8'))
        if R == 0:
            conn.send('Sunk Cruiser'.encode('utf-8'))
    elif board[y][x] == 'C':
        row[x] = 'O'
        conn.send('Hit'.encode('utf-8'))
        if C == 0:
            conn.send('Sunk Carrier'.encode('utf-8'))
    elif board[y][x] == 'D':
        row[x] = 'O'
        conn.send('Hit'.encode('utf-8'))
        if D == 0:
            conn.send('Sunk Destroyer'.encode('utf-8'))
    elif board[y][x] == 'S':
        row[x] = 'O'
        conn.send('Hit'.encode('utf-8'))
        if S == 0:
            conn.send('Sunk Submarine'.encode('utf-8'))
    elif board[y][x] == 'B':
        row[x] = 'O'
        conn.send('Hit'.encode('utf-8'))
        if B == 0:
            conn.send('Sunk Battleship'.encode('utf-8'))
    elif board[y][x] == 'X':
        conn.send('Already fired upon.'.encode('utf-8'))
    else:
        conn.send('Error'.encode('utf-8'))

    print (board)
    #Write board to storage
    g = open(file, "w")
    g.write("")
    for x in board:
        g.write(x + '\n')
    g.close()


conn.send('You won!'.encode('utf-8'))
conn.close()