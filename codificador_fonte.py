import json

# ------------------------------------------------
#  TEXT → BITS
# ------------------------------------------------
def text_to_bits(text, encoding='utf-8'):
    """Converte texto para uma lista de bits (0/1)."""
    byte_data = text.encode(encoding)
    bits = []

    for byte in byte_data:
        for i in range(7, -1, -1):  # MSB → LSB
            bits.append((byte >> i) & 1)

    return bits


# ------------------------------------------------
#  BITS → TEXT
# ------------------------------------------------
def bits_to_text(bits, encoding='utf-8'):
    """Converte uma lista de bits para texto."""
    if len(bits) % 8 != 0:
        raise ValueError("Quantidade de bits inválida (não é múltiplo de 8).")

    byte_list = []

    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i+8]:
            byte = (byte << 1) | b
        byte_list.append(byte)

    return bytes(byte_list).decode(encoding)


# ------------------------------------------------
#  CODIFICAÇÃO DE FONTE (RAW)
# ------------------------------------------------
def encode_raw(bits):
    """Codificação de fonte simples (sem compressão)."""
    return bits.copy()


def decode_raw(data):
    """Decodifica RAW (simplesmente retorna os bits)."""
    return data.copy()


# ------------------------------------------------
#  SELETOR DE MÉTODO DE CODIFICAÇÃO (apenas RAW agora)
# ------------------------------------------------
def encode_source(bits):
    """Codifica usando RAW (único método exigido no trabalho)."""
    return {"method": "raw", "data": encode_raw(bits)}


def decode_source(encoded_struct):
    """Decodifica RAW."""
    if encoded_struct["method"] != "raw":
        raise ValueError("Método de codificação inválido. Apenas RAW é permitido.")

    return decode_raw(encoded_struct["data"])


# ------------------------------------------------
#  SALVAR / CARREGAR
# ------------------------------------------------
def save_encoded(filename, encoded_struct):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(encoded_struct, f, indent=2)


def load_encoded(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


# ------------------------------------------------
#  TESTE / DEMONSTRAÇÃO
# ------------------------------------------------
if __name__ == "__main__":
    texto = "Olá Mundo! Teste 123"

    print("Texto original:", texto)

    bits = text_to_bits(texto)
    print("\nBits gerados:", bits[:64], "...")

    enc = encode_source(bits)
    save_encoded("saida_raw.json", enc)
    print("\nArquivo salvo: saida_raw.json")

    dec_bits = decode_source(enc)
    texto_rec = bits_to_text(dec_bits)

    print("\nTexto reconstruído:", texto_rec)
