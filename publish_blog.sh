#!/bin/bash

# Script para commitar e fazer push dos posts para o blog

cd /home/hashino/Projects/hashino.github.io

echo "Commitando posts para o blog..."

# Adiciona todos os novos posts
git add _posts/2026-01-21-*.md

# Commit com mensagem detalhada
git commit -m "Adiciona posts do Spectro: algoritmo paradoxal e guias técnicos

- Algoritmo que Me Consumiu: paradoxo do sistema auto-sabotador
- Manifesto da Meta Programação: metodologia educacional completa  
- I did it: reflexão sobre implementar própria destruição
- Como Vencer em Tech: guia prático para sucesso técnico

Posts integram filosofia periférica com estratégia técnica real.
Sistema PIX ativo para monetização da felicidade gerada."

# Push para GitHub Pages
git push origin main

echo "Posts publicados no blog!"
echo "Acesse: https://hashino.github.io"