import math

lines = [line.rstrip() for line in open('input.txt')]

binary = bin(int(lines[0], 16))[2:]
while len(binary) % 4 != 0:
    binary = '0'+binary


def decodePacket(binaryStr):
    packet_length = 0
    if ''.join(bit for bit in binaryStr[packet_length: packet_length + 3]) == "":
        return 0, None
    packet_length += 3
    packet_id = int(''.join(bit for bit in binaryStr[packet_length: packet_length + 3]), 2)
    packet_length += 3
    is_literal = packet_id == 4

    if is_literal:
        loop = True
        num = ''
        while loop:
            if binaryStr[packet_length] == '0':
                loop = False
            num += ''.join(bit for bit in binaryStr[packet_length+1: packet_length + 5])
            packet_length += 5
        return packet_length, int(num, 2)
    else:
        values = []
        length_id = int(binaryStr[packet_length: packet_length + 1])
        packet_length += 1
        if length_id == 0:
            length_sub_packs = int(''.join(bit for bit in binaryStr[packet_length: packet_length + 15]), 2)
            packet_length += 15
            max_length = packet_length + length_sub_packs
            while packet_length < max_length:
                packet_len, packet_val = decodePacket(binaryStr[packet_length:])
                packet_length += packet_len
                values.append(packet_val)
        else:
            num_sub_packs = int(''.join(bit for bit in binaryStr[packet_length: packet_length + 11]), 2)
            packet_length += 11
            pack_count = 0
            while pack_count < num_sub_packs:
                packet_len, packet_val = decodePacket(binaryStr[packet_length:])
                packet_length += packet_len
                pack_count += 1
                values.append(packet_val)
        if packet_id == 0:
            return packet_length, sum(values)
        elif packet_id == 1:
            return packet_length, math.prod(values)
        elif packet_id == 2:
            return packet_length, min(values)
        elif packet_id == 3:
            return packet_length, max(values)
        elif packet_id == 5:
            return packet_length, 1 if values[0] > values[1] else 0
        elif packet_id == 6:
            return packet_length, 1 if values[0] < values[1] else 0
        elif packet_id == 7:
            return packet_length, 1 if values[0] == values[1] else 0



_, value = decodePacket(binary)
print(value)
