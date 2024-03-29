lines = [line.rstrip() for line in open('input.txt')]

binary = bin(int(lines[0], 16))[2:]
while len(binary) % 4 != 0:
    binary = '0'+binary
versions = []


def decodePacket(binaryStr):
    packet_length = 0
    if ''.join(bit for bit in binaryStr[packet_length: packet_length + 3]) == "":
        return 0
    ver = int(''.join(bit for bit in binaryStr[packet_length: packet_length + 3]), 2)
    versions.append(ver)
    packet_length += 3
    packet_id = int(''.join(bit for bit in binaryStr[packet_length: packet_length + 3]), 2)
    packet_length += 3
    is_literal = packet_id == 4

    if is_literal:
        loop = True
        while loop:
            if binaryStr[packet_length] == '0':
                loop = False
            packet_length += 5
    else:
        length_id = int(binaryStr[packet_length: packet_length + 1])
        packet_length += 1
        if length_id == 0:
            length_sub_packs = int(''.join(bit for bit in binaryStr[packet_length: packet_length + 15]), 2)
            packet_length += 15
            max_length = packet_length + length_sub_packs
            while packet_length < max_length:
                packet_length += decodePacket(binaryStr[packet_length:])
        else:
            num_sub_packs = int(''.join(bit for bit in binaryStr[packet_length: packet_length + 11]), 2)
            packet_length += 11
            pack_count = 0
            while pack_count < num_sub_packs:
                packet_length += decodePacket(binaryStr[packet_length:])
                pack_count += 1
    return packet_length



decodePacket(binary)
print(sum(versions))
