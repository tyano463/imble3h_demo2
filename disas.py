#!/usr/bin/env python3

import sys
import os
from functools import cmp_to_key

KB = 1024

init_opcode = None
INSTRUCTION_SIZE = 14
program_size = 16 * KB


def prepare():
    global init_opcode
    global INSTRUCTION_SIZE
    global program_size

    # init_opcode = init_opcode12f683
    init_opcode = init_opcode18f26q84

    # INSTRUCTION_SIZE = 14     # 12f683
    INSTRUCTION_SIZE = 16       # 18F26Q84

    # program_size = 16 * KB    # 12f683
    program_size = 128 * KB   # 18F26Q84


def usage():
    explain = """usage:
    ./disas.py <file>
"""
    print(explain, end="")


def get_file_path():
    if len(sys.argv) != 2:
        return None
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        return None
    return file_path


class HexRecord:
    def __init__(self, address, data):
        self.address = address
        self.data = (data[1] << 8) | data[0]

    def __str__(self):
        data_str = "{:04x}".format(self.data)
        return f"{self.address:04X}: {data_str}"


class IntelHexParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.records = []

    def get_extend_addr(self, data) -> int:
        extend = 0
        if len(data) == 2:
            extend = (data[0] << 8 | data[1]) << 16
        return extend

    def parse(self):
        last_data = None
        extend_addr = 0
        with open(self.filepath, "r") as file:
            for line in file:
                if not line.startswith(":"):
                    continue

                byte_count = int(line[1:3], 16)
                address = int(line[3:7], 16)
                address = address + extend_addr
                record_type = int(line[7:9], 16)
                data = [
                    int(line[i : i + 2], 16) for i in range(9, 9 + byte_count * 2, 2)
                ]

                if last_data:
                    address = address - 1
                    byte_count = byte_count + 1
                    data = data.append(last_data)
                    last_data = None

                # データレコードのみ追加
                if record_type != 0x00:
                    if record_type == 0x04:
                        extend_addr = self.get_extend_addr(data)
                    continue
                if address > program_size:
                    continue
                if (byte_count % 2) != 0:
                    last_data = data.pop()
                    byte_count = byte_count - 1

                pairs = list(zip(data[::2], data[1::2]))

                for x in pairs:
                    record = HexRecord(address, x)
                    self.records.append(record)
                    address = address + 2

    def get_records(self):
        return self.records


class Instruction:
    disas_str = ""

    def __init__(
        self, mnemonic, operands, description, bits, size=1, prev=None, next=None
    ):
        self.mnemonic = mnemonic
        self.operands = operands
        self.description = description
        self.bits = bits
        self.size = size
        self.prev = prev
        self.next = next

    def __str__(self):
        p = f"p:{self.prev.mnemonic}" if self.prev is not None else ""
        n = f"n:{self.next.mnemonic}" if self.next is not None else ""

        return f"{self.mnemonic}({self.size}) {self.description} {self.bits} {p} {n}"

    def __repr__(self):
        return self.__str__()

    def disas(self, i, data) -> int:
        if self.size == 1:
            # print(f"size1:{self.size} {data[i].data:x} {self.operands} {self.bits}")
            desc = self.check_operands(data[i].data, self.operands, self.bits)
            multiplier = 2 if self.mnemonic in ("GOTO", "CALL") else 1
            desc_str = ",".join([f"{k}: {v * multiplier:X}" for k, v in desc.items()])
            # print(f"desc:{desc_str}")
            self.disas_str = (
                f"{self.mnemonic} {desc_str} {self.description} {self.bits}"
            )
        else:
            size = self.get_size()
            if size != self.size:
                raise Exception(
                    f"size not much {data[i].address:x}: {data[i].data:x} {size},{self.size}\n{self}"
                )

            inst = self
            bits = ""
            operands = {}
            shift = {}
            for j in range(size):
                desc = self.check_operands(data[i + j].data, inst.operands, inst.bits)
                for k, v in desc.items():
                    sh = shift.get(k, 0)
                    operands[k] = operands.get(k, 0) + (v << sh)
                    shift[k] = sh + inst.bits.count(k)

                bits = f"{bits} {inst.bits}"
                inst = inst.next
                # desc_str = ",".join([f"{k}: {v:X}" for k, v in desc.items()])
                # print(f"#### desc:{desc_str}")

            multiplier = 2 if self.mnemonic in ("GOTO", "CALL") else 1
            desc_str = ",".join([f"{k}: {v * multiplier:X}" for k, v in operands.items()])

            self.disas_str = f"{self.mnemonic} {desc_str} {self.description} {bits}"
            # if data[i].data == 0xef13:
            #     raise Exception(f"stop {self}")
        return self.size - 1

    def get_size(self):
        inst = self
        count = 1
        while inst.next:
            inst = inst.next
            count = count + 1
        return count

    def check_operands(self, value: int, operands: str, bit_mask: str) -> dict:
        value_bits = f"{value:0{INSTRUCTION_SIZE}b}"

        operand_list = operands.split(", ")

        result = {}

        # print(f"list:{operand_list} value:{value_bits}")
        for operand in operand_list:
            operand_bits = []

            if operand not in bit_mask:
                break

            l = len(bit_mask)
            if len(value_bits) != l:
                print(f"#### Error v:{value_bits} m:{bit_mask}")
                break

            bit_index = 0
            found = False
            for i in range(l):
                if operand == bit_mask[i]:
                    operand_bits.append(value_bits[i])
                    found = True
                else:
                    if found:
                        break
                    continue

                bit_index += 1

            # print(operand_bits)
            if operand_bits:
                result[operand] = int("".join(operand_bits), 2)

        return result


_instructions12f683 = [
    "ADDWF	f, d	Add W and f	00	0111	dfff	ffff",
    "ANDWF	f, d	AND W with f	00	0101	dfff	ffff",
    "CLRF	f	Clear f	00	0001	lfff	ffff",
    "CLRW	–	Clear W	00	0001	0xxx	xxxx",
    "COMF	f, d	Complement f	00	1001	dfff	ffff",
    "DECF	f, d	Decrement f	00	0011	dfff	ffff",
    "DECFS	f, dZ	Decrement f, Skip if 0	00	1011	dfff	ffff",
    "INCF	f, d	Increment f	00	1010	dfff	ffff",
    "INCFS	f, dZ	Increment f, Skip if 0	00	1111	dfff	ffff",
    "IORWF	f, d	Inclusive OR W with f	00	0100	dfff	ffff",
    "MOVF	f, d	Move f	00	1000	dfff	ffff",
    "MOVWF	f	Move W to f	00	0000	lfff	ffff",
    "NOP	–	No Operation	00	0000	0xx0	0000",
    "RLF	f, d	Rotate Left f through Carry	00	1101	dfff	ffff",
    "RRF	f, d	Rotate Right f through Carry	00	1100	dfff	ffff",
    "SUBWF	f, d	Subtract W from f	00	0010	dfff	ffff",
    "SWAPF	f, d	Swap nibbles in f	00	1110	dfff	ffff",
    "XORWF	f, d	Exclusive OR W with f	00	0110	dfff	ffff",
    "BCF	f, b	Bit Clear f	01	00bb	bfff	ffff",
    "BSF	f, b	Bit Set f	01	01bb	bfff	ffff",
    "BTFSC	f, b	Bit Test f, Skip if Clear	01	10bb	bfff	ffff",
    "BTFSS	f, b	Bit Test f, Skip if Set	01	11bb	bfff	ffff",
    "ADDLW	k	Add literal and W	11	111x	kkkk	kkkk",
    "ANDLW	k	AND literal with W	11	1001	kkkk	kkkk",
    "CALL	k	Call Subroutine	10	0kkk	kkkk	kkkk",
    "CLRWDT	–	Clear Watchdog Timer	00	0000	0110	0100",
    "GOTO	k	Go to address	10	1kkk	kkkk	kkkk",
    "IORLW	k	Inclusive OR literal with W	11	1000	kkkk	kkkk",
    "MOVLW	k	Move literal to W	11	00xx	kkkk	kkkk",
    "RETFIE	–	Return from interrupt	00	0000	0000	1001",
    "RETLW	k	Return with literal in W	11	01xx	kkkk	kkkk",
    "RETURN	–	Return from Subroutine	00	0000	0000	1000",
    "SLEEP	–	Go into Standby mode	00	0000	0110	0011",
    "SUBLW	k	Subtract W from literal	11	110x	kkkk	kkkk",
    "XORLW	k	Exclusive OR literal with W	11	1010	kkkk	kkkk",
]

_instructions18f26q84 = [
    # Mnemonic	Operands	説明	p	word	サイクル	16ビット命令ワード	影響を受けるステータス	備考"
    "ADDWF	f, d, a	WREG と f を加算		1	1	0010 01da ffff ffff	C, DC, Z, OV, N	1",
    "ADDWFC	f, d, a	WREG とキャリービットを f に加算		1	1	0010 00da ffff ffff	C, DC, Z, OV, N	1",
    "ANDWF	f, d, a	WREG と f を AND		1	1	0001 01da ffff ffff	Z, N	1",
    "CLRF	f, a	f をクリア		1	1	0110 101a ffff ffff	Z	",
    "COMF	f, d, a	f を反転		1	1	0001 11da ffff ffff	Z, N	1",
    "DECF	f, d, a	f をデクリメント		1	1	0000 01da ffff ffff	C, DC, Z, OV, N	1",
    "INCF	f, d, a	f をインクリメント		1	1	0010 10da ffff ffff	C, DC, Z, OV, N	1",
    "IORWF	f, d, a	WREG と f を OR		1	1	0001 00da ffff ffff	Z, N	1",
    "MOVF	f, d, a	f を WREG または f に移動		1	1	0101 00da ffff ffff	Z, N	1",
    "MOVFF	s, d	12ビット fs を 12ビット fd に移動	1	2	2	1100 ssss ssss ssss	なし	1, 3, 4",
    "MOVFF	s, d	12ビット fs を 12ビット fd に移動	2	2	2	1111 dddd dddd dddd	なし	1, 3, 4",
    "MOVFFL	s, d	Move fs (14-bit source) to fd (14-bit destination)	1	3	3	0000 0000 0110 ssss	なし	1, 3",
    "MOVFFL	s, d	Move fs (14-bit source) to fd (14-bit destination)	2	3	3	1111 ssss ssss ssdd	なし	1, 3",
    "MOVFFL	s, d	Move fs (14-bit source) to fd (14-bit destination)	3	3	3	1111 dddd dddd dddd	なし	1, 3",
    "MOVWF	f, a	WREG を f に移動		1	1	0110 111a ffff ffff	なし	",
    "MULWF	f, a	WREG と f を乗算		1	1	0000 001a ffff ffff	なし	1",
    "NEGF	f, a	f を負数に変換		1	1	0110 110a ffff ffff	C, DC, Z, OV, N	1",
    "RLCF	f, d, a	f を左ローテート (キャリー経由)		1	1	0011 01da ffff ffff	C, Z, N	1",
    "RLNCF	f, d, a	f を左ローテート (キャリーなし)		1	1	0100 01da ffff ffff	Z, N	1",
    "RRCF	f, d, a	f を右ローテート (キャリー経由)		1	1	0011 00da ffff ffff	C, Z, N	1",
    "RRNCF	f, d, a	f を右ローテート (キャリーなし)		1	1	0100 00da ffff ffff	Z, N	1",
    "SETF	f, a	f をセット		1	1	0110 100a ffff ffff	なし	",
    "SUBFWB	f, d, a	Subtract f from WREG with Borrow		１	1	0101 01da ffff ffff	C, DC, Z, OV, N	1",
    "SUBWF	f, d, a	Subtract WREG from f		１	1	0101 11da ffff ffff	C, DC, Z, OV, N	1",
    "SUBWFB	f, d, a	Subtract WREG from f with Borrow		１	1	0101 10da ffff ffff	C, DC, Z, OV, N	1",
    "SWAPF	f, d, a	Swap nibbles in f		１	1	0011 10da ffff ffff	None	1",
    "XORWF	f, d, a	Exclusive OR WREG with f		１	1	0001 10da ffff ffff	Z, N	1",
    "CPFSEQ	f, a	Compare f with WREG, skip if =		１	1 – 4	0110 001a ffff ffff	None	1, 2",
    "CPFSGT	f, a	Compare f with WREG, skip if >		１	1 – 4	0110 010a ffff ffff	None	1, 2",
    "CPFSLT	f, a	Compare f with WREG, skip if <		１	1 – 4	0110 000a ffff ffff	None	1, 2",
    "DECFSZ	f, d, a	Decrement f, Skip if 0		１	1 – 4	0010 11da ffff ffff	None	1, 2",
    "DCFSNZ	f, d, a	Decrement f, Skip if Not 0		１	1 – 4	0100 11da ffff ffff	None	1, 2",
    "INCFSZ	f, d, a	Increment f, Skip if 0		１	1 – 4	0011 11da ffff ffff	None	1, 2",
    "INFSNZ	f, d, a	Increment f, Skip if Not 0		１	1 – 4	0100 10da ffff ffff	None	1, 2",
    "TSTFSZ	f, a	Test f, skip if 0		１	1 – 4	0110 011a ffff ffff	None	1, 2",
    "BCF	f, b, a	Bit Clear f		１	1	1001 bbba ffff ffff	None	1",
    "BSF	f, b, a	Bit Set f		１	1	1000 bbba ffff ffff	None	1",
    "BTG	f, b, a	Bit Toggle f		１	1	0111 bbba ffff ffff	None	1",
    "BTFSC	f, b, a	Bit Test f, Skip if Clear		１	1 – 4	1011 bbba ffff ffff	None	1, 2",
    "BTFSS	f, b, a	Bit Test f, Skip if Set		1	1 – 4	1010 bbba ffff ffff	なし	1, 2",
    "BC	n	Branch if Carry		1	1 – 2	1110 0010 nnnn nnnn	なし	2",
    "BN	n	Branch if Negative		1	1 – 2	1110 0110 nnnn nnnn	なし	2",
    "BNC	n	Branch if Not Carry		1	1 – 2	1110 0011 nnnn nnnn	なし	2",
    "BNN	n	Branch if Not Negative		1	1 – 2	1110 0111 nnnn nnnn	なし	2",
    "BNOV	n	Branch if Not Overflow		1	1 – 2	1110 0101 nnnn nnnn	なし	2",
    "BNZ	n	Branch if Not Zero		1	1 – 2	1110 0001 nnnn nnnn	なし	2",
    "BOV	n	Branch if Overflow		1	1 – 2	1110 0100 nnnn nnnn	なし	2",
    "BRA	n	Branch Unconditionally		1	2	1101 0nnn nnnn nnnn	なし	2",
    "BZ	n	Branch if Zero		1	1 – 2	1110 0000 nnnn nnnn	なし	2",
    "CALL	k, s	Call subroutine	1	2	2	1110 110s kkkk kkkk	なし	2, 3",
    "CALL	k, s	Call subroutine	2	2	2	1111 kkkk kkkk kkkk	なし	2, 3",
    "CALLW	—	Call subroutine using WREG		1	2	0000 0000 0001 0100	なし	2",
    "GOTO	k	Go to address	1	2	2	1110 1111 kkkk kkkk	なし	3",
    "GOTO	k	Go to address	2	2	2	1111 kkkk kkkk kkkk	なし	3",
    "RCALL	n	Relative Call		1	2	1101 1nnn nnnn nnnn	なし	2",
    "RETFIE	s	Return from interrupt enable		1	2	0000 0000 0001 000s	INTCONx STAT bits	2",
    "RETLW	k	Return with literal in WREG		1	2	0000 1100 kkkk kkkk	なし	2",
    "RETURN	s	Return from Subroutine		1	2	0000 0000 0001 001s	なし	2",
    "CLRWDT	—	Clear Watchdog Timer		1	1	0000 0000 0000 0100	TO, PD	",
    "DAW	—	Decimal Adjust WREG		1	1	0000 0000 0000 0111	C	",
    "NOP	—	No Operation		1	1	0000 0000 0000 0000	なし	",
    "POP	—	Pop top of return stack (TOS)		1	1	0000 0000 0000 0110	なし	",
    "PUSH	—	Push top of return stack (TOS)		1	1	0000 0000 0000 0101	なし	",
    "RESET	—	Software device Reset		1	1	0000 0000 1111 1111	全て	",
    "SLEEP	—	Go into Standby mode		1	1	0000 0000 0000 0011	TO, PD	",
    "ADDFSR	n, k	Add FSR(fn) with literal (k)		1	1	1110 1000 nnkk kkkk	なし	",
    "ADDLW	k	Add literal and WREG		1	1	0000 1111 kkkk kkkk	C, DC, Z, OV, N	",
    "ANDLW	k	AND literal with WREG		1	1	0000 1011 kkkk kkkk	Z, N	",
    "IORLW	k	Inclusive OR literal with WREG		1	1	0000 1001 kkkk kkkk	Z, N	",
    "LFSR	n, k	Load FSR(fn) with a 14-bit literal (k)	1	2	2	1110 1110 00nn kkkk	なし	",
    "LFSR	n, k	Load FSR(fn) with a 14-bit literal (k)	2	2	2	1111 00kk kkkk kkkk	なし	",
    "MOVLB	k	Move literal to BSR<5:0>		1	1	0000 0001 00kk kkkk	なし	",
    "MOVLW	k	Move literal to WREG		1	1	0000 1110 kkkk kkkk	なし	",
    "MULLW	k	Multiply literal with WREG		1	1	0000 1101 kkkk kkkk	なし	",
    "RETLW	k	Return with literal in WREG		1	2	0000 1100 kkkk kkkk	なし	",
    "SUBFSR	n, k	Subtract literal (k) from FSR(fn)		1	1	1110 1001 nnkk kkkk	なし	",
    "SUBLW	k	Subtract WREG from literal		1	1	0000 1000 kkkk kkkk	C, DC, Z, OV, N	",
    "XORLW	k	Exclusive OR literal with WREG		1	1	0000 1010 kkkk kkkk	Z, N	",
    "TBLRD*	—	Table Read		1	2	0000 0000 0000 1000	なし	",
    "TBLRD*+	—	Table Read with post-increment		1	2	0000 0000 0000 1001	なし	",
    "TBLRD*-	—	Table Read with post-decrement		1	2	0000 0000 0000 1010	なし	",
    "TBLRD+*	—	Table Read with pre-increment		1	2	0000 0000 0000 1011	なし	",
    "TBLWT*	—	Table Write		1	2	0000 0000 0000 1100	なし	",
    "TBLWT*+	—	Table Write with post-increment		1	2	0000 0000 0000 1101	なし	",
    "TBLWT*-	—	Table Write with post-decrement		1	2	0000 0000 0000 1110	なし	",
    "TBLWT+*	—	Table Write with pre-increment		1	2	0000 0000 0000 1111	なし	",
]

instructions = []

_init_opcode = False


def custom_strcmp(a: str, b: str) -> int:
    la = sum(1 for char in a if char in {"0", "1"})
    lb = sum(1 for char in b if char in {"0", "1"})

    if la != lb:
        return lb - la
    for x, y in zip(a, b):
        if x == y:
            continue
        if x == "1":
            return -1
        if y == "1":
            return 1
        if x == "0":
            return -1
        if y == "0":
            return 1
    return 0


def compare_inst(a, b) -> int:
    val = custom_strcmp(a.bits, b.bits)
    return val


def to_int(a):
    try:
        return int(a)
    except ValueError:
        return 0


def to_int2(a, b):
    return [to_int(a), to_int(b)]


def compare_inst18f26q84(a: Instruction, b: Instruction) -> int:
    if a.next and (not a.prev):
        if b.next and (not b.prev):
            return custom_strcmp(a.bits, b.bits)
        else:
            return -1
    elif b.next and (not b.prev):
        return 1
    else:
        return custom_strcmp(a.bits, b.bits)


def init_opcode18f26q84():
    global _init_opcode
    global instructions
    prev = None
    if not _init_opcode:
        _init_opcode = True
        for inst in _instructions18f26q84:
            cols = inst.split("\t")
            iset = Instruction(
                cols[0], cols[1], cols[2], cols[6].replace(" ", ""), to_int(cols[4])
            )
            prio = to_int(cols[3])
            if prio > 0:
                if prio != 1:
                    prev.next = iset
                    iset.prev = prev
                prev = iset
            else:
                prev = None

            # print(f"add:{iset}")
            instructions.append(iset)

        instructions.sort(key=cmp_to_key(compare_inst18f26q84))
        # for inst in instructions:
        #     print(inst)


def init_opcode12f683():
    global _init_opcode
    global instructions
    if not _init_opcode:
        _init_opcode = True
        for inst in _instructions12f683:
            cols = inst.split("\t")
            iset = Instruction(cols[0], cols[1], cols[2], "".join(cols[3:]))
            instructions.append(iset)
        instructions.sort(key=cmp_to_key(compare_inst))


#        for inst in instructions:
#            print(inst)


def check_bits_match(value: int, pattern: str) -> bool:
    value_bits = f"{value:0{INSTRUCTION_SIZE}b}"

    for bit, char in zip(value_bits, pattern):
        if char == "1" and bit != "1":
            return False
        if char == "0" and bit != "0":
            return False
        if char not in "01":
            continue
    return True


def get_opcode(r) -> Instruction:
    global instructions
    global init_opcode
    init_opcode()

    for inst in instructions:
        if check_bits_match(r, inst.bits):
            return inst
    print(f"#### not found {r:x}")
    return None


def analyze(data):
    skip = 0
    for i in range(len(data)):
        if skip > 0:
            skip = skip - 1
            continue
        x = data[i]
        # print(f"{i}: {x.address:x} {x.data:x}")
        inst = get_opcode(x.data)
        skip = inst.disas(i, data)

        print(f"{x} {inst.disas_str}")


def main():
    prepare()
    file_path = get_file_path()
    if not file_path:
        usage()
        exit()
    hex_parser = IntelHexParser(file_path)
    hex_parser.parse()

    analyze(hex_parser.records)


if __name__ == "__main__":
    main()
