# ==========================================================
#  CODIFICADOR DE FONTE (RAW) + CODIFICAÇÃO MANCHESTER
# ==========================================================
# Este programa:
# 1) Converte um texto para bits (fonte RAW)
# 2) Codifica os bits usando Manchester
# 3) Decodifica Manchester de volta para bits
# 4) Reconstrói o texto original
# ==========================================================

# ----------------------------------------------------------
# 1) Codificação de Fonte (RAW)
# ----------------------------------------------------------
def encode_raw(texto):
    """
    Converte cada caractere UTF-8 em seu valor binário.
    Ex: 'A' -> 01000001
    """
    bits = "".join(f"{byte:08b}" for byte in texto.encode("utf-8"))
    return bits


def decode_raw(bits):
    """
    Converte uma sequência binária para texto UTF-8.
    Os bits são agrupados em bytes (8 bits).
    """
    bytes_list = []

    # processa 8 bits por vez
    for i in range(0, len(bits), 8):
        byte_str = bits[i:i+8]
        if len(byte_str) == 8:  # só decodifica bytes completos
            bytes_list.append(int(byte_str, 2))

    return bytes(bytes_list).decode("utf-8", errors="ignore")


# ----------------------------------------------------------
# 2) Codificação Manchester
# ----------------------------------------------------------
# Regras:
# bit '1' → alta-baixa = 10
# bit '0' → baixa-alta = 01
# ----------------------------------------------------------
def manchester_encode(bits):
    manchester = ""

    for b in bits:
        if b == "1":
            manchester += "10"
        else:  # b == "0"
            manchester += "01"

    return manchester


# ----------------------------------------------------------
# 3) Decodificação Manchester
# ----------------------------------------------------------
def manchester_decode(bits_manch):
    """
    Recebe bits em pares:
    "10" → 1
    "01" → 0
    """
    decoded = ""

    # processa 2 bits por vez
    for i in range(0, len(bits_manch), 2):
        par = bits_manch[i:i+2]

        if par == "10":
            decoded += "1"
        elif par == "01":
            decoded += "0"
        else:
            decoded += "?"  # erro detectado

    return decoded


# ----------------------------------------------------------
# 4) Teste completo (pipeline)
# ----------------------------------------------------------
if __name__ == "__main__":
    texto = "Olá Gustavo!"

    print("\n TEXTO ORIGINAL:", texto)

    # 1) Codificação RAW
    bits_raw = encode_raw(texto)
    print("\n [RAW] Bits da fonte:")
    print(bits_raw)

    # 2) Manchester
    bits_manchester = manchester_encode(bits_raw)
    print("\n [MANCHESTER] Codificado:")
    print(bits_manchester[:120], "...")  # só printa começo

    # 3) Decodificação Manchester
    bits_decoded = manchester_decode(bits_manchester)
    print("\n [MANCHESTER] Decodificado (bits):")
    print(bits_decoded)

    # 4) Reconstrói o texto
    texto_final = decode_raw(bits_decoded)
    print("\n TEXTO RECONSTRUÍDO:", texto_final)
