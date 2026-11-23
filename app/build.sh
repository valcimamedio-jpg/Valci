#!/bin/sh
# Gera index.html (arquivo completo, abre direto no navegador) a partir de app/orcamento.html
cd "$(dirname "$0")/.."
{ printf '<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>\n'; cat app/orcamento.html; printf '\n</body></html>\n'; } > index.html
