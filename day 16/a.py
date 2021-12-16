lines = [line.rstrip() for line in open('input.txt')]

binary = bin(int(lines[0], 16))[2:]

ver = int(''.join(bit for bit in binary[0:3]), 2)
packet_id = int(''.join(bit for bit in binary[3:6]), 2)
print(ver, packet_id)