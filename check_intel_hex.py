#!/usr/bin/env python3

import sys

def verify_intel_hex(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.strip()
        if not line.startswith(':'):
            print(f"Error on line {i+1}: Does not start with ':'")
            return False
        
        try:
            byte_count = int(line[1:3], 16)
            address = int(line[3:7], 16)
            record_type = int(line[7:9], 16)
            data = bytes.fromhex(line[9:-2])
            checksum = int(line[-2:], 16)
        except ValueError:
            print(f"Error on line {i+1}: Invalid HEX format")
            return False

        if len(data) != byte_count:
            print(f"Error on line {i+1}: Byte count mismatch ({byte_count} expected, {len(data)} found)")
            return False

        checksum_calc = byte_count + (address >> 8) + (address & 0xFF) + record_type + sum(data)
        checksum_calc = (-checksum_calc) & 0xFF  # 2's complement
        if checksum != checksum_calc:
            print(f"Error on line {i+1}: Checksum mismatch (Expected: {checksum_calc:02X}, Found: {checksum:02X})")
            return False

    print("Intel HEX file is valid.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_hex.py <filename.hex>")
        sys.exit(1)
    
    verify_intel_hex(sys.argv[1])

