import sys
import re

def parse_bdf(filename):
    chars = {}
    current = None
    bitmap = []
    encoding = None
    in_bitmap = False

    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()

            if line.startswith("STARTCHAR"):
                current = line.split()[1]
                bitmap = []
                encoding = None
                in_bitmap = False

            elif line.startswith("ENCODING"):
                encoding = int(line.split()[1])

            elif line == "BITMAP":
                in_bitmap = True

            elif line == "ENDCHAR":
                if encoding is not None:
                    chars[encoding] = bitmap
                current = None
                bitmap = []
                encoding = None
                in_bitmap = False

            elif in_bitmap:
                if re.fullmatch(r"[0-9A-Fa-f]+", line):
                    bitmap.append(int(line, 16))

    return chars


def build_font(chars):
    font = [[0x00] * 16 for _ in range(256)]

    for code in range(256):
        if code in chars:
            data = chars[code]

            # ajusta para 16 linhas
            for i in range(min(16, len(data))):
                font[code][i] = data[i]

    return font


def write_bin(font, outname="font.bin"):
    with open(outname, "wb") as f:
        for ch in range(256):
            f.write(bytes(font[ch]))


def write_c_header(font, outname="font.h"):
    with open(outname, "w") as f:
        f.write("#ifndef FONT_H\n")
        f.write("#define FONT_H\n\n")
        f.write("#include <stdint.h>\n\n")
        f.write("const uint8_t font[256][16] = {\n")

        for ch in range(256):
            f.write(f"  /* char {ch} */ {{")
            f.write(",".join(f"0x{b:02X}" for b in font[ch]))
            f.write("},\n")

        f.write("};\n\n")
        f.write("#endif\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python bdf_to_font.py fonte.bdf")
        sys.exit(1)

    bdf_file = sys.argv[1]

    chars = parse_bdf(bdf_file)
    font = build_font(chars)

    write_bin(font, "font.bin")
    write_c_header(font, "font.h")

    print("OK!")
    print("Gerado: font.bin (4096 bytes)")
    print("Gerado: font.h (uint8_t font[256][16])")

