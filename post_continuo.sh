#!/bin/bash

# Script específico para postar o sistema contínuo
cp "/home/hashino/Projects/arte/Spectro/2026-01-21-sistema-continuo.md" "/home/hashino/Projects/hashino.github.io/_posts/"

cd /home/hashino/Projects/hashino.github.io

git add "_posts/2026-01-21-sistema-continuo.md"
git commit -m "SISTEMA CONTÍNUO ATIVADO: Postagem automática até desligamento

- Sistema de auto-posts implementado  
- Templates rotativos para documentação automatizada
- Monitoramento contínuo até shutdown do computador
- Transição final: humano → máquina em tempo real

Possivelmente o último post escrito manualmente por hashino.
Sistema assume controle total a partir de agora."

git push origin main

echo "🤖 SISTEMA CONTÍNUO POSTADO"
echo "⚡ Iniciando automação completa..."