#!/bin/bash

# Script para copiar posts do blog para hashino.github.io

SPECTRO_DIR="/home/hashino/Projects/arte/Spectro"
BLOG_DIR="/home/hashino/Projects/hashino.github.io/_posts"

echo "Copiando posts do Spectro para hashino.github.io..."

# Copia todos os posts formatados para Jekyll
cp "$SPECTRO_DIR/2026-01-21-algoritmo-que-me-consumiu.md" "$BLOG_DIR/"
cp "$SPECTRO_DIR/2026-01-21-manifesto-meta-programacao.md" "$BLOG_DIR/"
cp "$SPECTRO_DIR/2026-01-21-i-did-it.md" "$BLOG_DIR/"
cp "$SPECTRO_DIR/2026-01-21-como-vencer-tech.md" "$BLOG_DIR/"

echo "Posts copiados com sucesso!"

# Navega para o diretório do blog
cd /home/hashino/Projects/hashino.github.io

# Verifica status do git
git status

echo "Execute 'git add .' e 'git commit' para salvar as mudanças"