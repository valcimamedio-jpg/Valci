"""Gera um QR Code Pix estático (padrão BR Code do Banco Central).

Uso:
    pip install "qrcode[pil]"
    python3 gerar_pix.py              # QR Code sem valor (o cliente digita o valor)
    python3 gerar_pix.py 25.90        # QR Code com valor fixo de R$ 25,90
"""
import sys
import unicodedata

import qrcode
from PIL import Image, ImageDraw, ImageFont

# ---- Configuração ----------------------------------------------------------
CHAVE_PIX = "+5595981297185"   # chave do tipo telefone: (95) 98129-7185
NOME = "ANA CLARA ALVARENGA"        # até 25 caracteres
CIDADE = "BOA VISTA"           # até 15 caracteres
TXID = "***"                   # "***" = sem identificador específico
# ---------------------------------------------------------------------------


def _limpa(texto, limite):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return texto.upper()[:limite]


def _campo(id_, valor):
    return f"{id_}{len(valor):02d}{valor}"


def _crc16(payload):
    crc = 0xFFFF
    for byte in payload.encode():
        crc ^= byte << 8
        for _ in range(8):
            crc = ((crc << 1) ^ 0x1021) if crc & 0x8000 else (crc << 1)
            crc &= 0xFFFF
    return f"{crc:04X}"


def gerar_payload(valor=None):
    conta = _campo("00", "br.gov.bcb.pix") + _campo("01", CHAVE_PIX)
    payload = (
        _campo("00", "01")
        + _campo("26", conta)
        + _campo("52", "0000")
        + _campo("53", "986")
        + (_campo("54", f"{valor:.2f}") if valor else "")
        + _campo("58", "BR")
        + _campo("59", _limpa(NOME, 25))
        + _campo("60", _limpa(CIDADE, 15))
        + _campo("62", _campo("05", TXID))
        + "6304"
    )
    return payload + _crc16(payload)


def gerar_imagem(payload, arquivo, valor=None):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,
                       box_size=12, border=4)
    qr.add_data(payload)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    w, h = img_qr.size
    topo, rodape = 90, 110
    img = Image.new("RGB", (w, h + topo + rodape), "white")
    img.paste(img_qr, (0, topo))
    d = ImageDraw.Draw(img)
    try:
        grande = ImageFont.truetype("DejaVuSans-Bold.ttf", 40)
        pequena = ImageFont.truetype("DejaVuSans.ttf", 24)
    except OSError:
        grande = pequena = ImageFont.load_default()

    def centro(y, texto, fonte, cor="black"):
        largura = d.textlength(texto, font=fonte)
        d.text(((w - largura) / 2, y), texto, font=fonte, fill=cor)

    centro(30, "Pague com Pix", grande, "#32BCAD")
    linha = f"Valor: R$ {valor:.2f}".replace(".", ",") if valor else "Escaneie e digite o valor"
    centro(topo + h + 5, linha, pequena)
    centro(topo + h + 40, "Chave (celular): (95) 98129-7185", pequena)
    centro(topo + h + 72, NOME, pequena, "#555555")
    img.save(arquivo)


if __name__ == "__main__":
    valor = float(sys.argv[1].replace(",", ".")) if len(sys.argv) > 1 else None
    payload = gerar_payload(valor)
    arquivo = f"pix_qrcode_{valor:.2f}.png".replace(".", "_", 1) if valor else "pix_qrcode.png"
    gerar_imagem(payload, arquivo, valor)
    print("Pix Copia e Cola:")
    print(payload)
    print(f"\nImagem salva em: {arquivo}")
