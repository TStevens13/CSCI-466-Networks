import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
x = int(sys.argv[3])
y = int(sys.argv[4])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
print("Connected to server!")

#Read board in
file = 'opponent_board.txt'
with open(file) as f:
    board = f.readlines()
board = [row.rstrip('\n') for row in board]

xs = chr(x)
ys = chr(y)
s.send(xs.encode('utf-8'))
s.send(ys.encode('utf-8'))

#Get output
data = s.recv(200)
output = data.decode('utf-8')
row = list(board[y])
if (output == 'You won!'):
    print(output)
elif (output == 'Miss'):
    row[x] = 'X'
    print(output)
elif (output == 'Hit'):
    row[x] = 'O'
    print(output)
else:
    print(output)

#Write board to storage
g = open(file, "w")
g.write("")
for x in board:
    g.write(x + '\n')
g.close()

#Print current board
f = open(file, "r")
i = 0
while i < 10:
    print(i, end =" ")
    print(f.readline(), end ="")
    i += 1
f.close
print('')
print('  0123456789')

s.close()