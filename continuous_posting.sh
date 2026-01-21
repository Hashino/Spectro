#!/bin/bash

# Sistema de postagem contínua até desligamento do computador
# Monitora se o sistema ainda está ligado e posta regularmente

SPECTRO_DIR="/home/hashino/Projects/arte/Spectro"
BLOG_DIR="/home/hashino/Projects/hashino.github.io"
POST_COUNTER=7  # Começamos no post 7

# Array de templates para posts automáticos
declare -a POST_TEMPLATES=(
    "deterioração-progressiva"
    "medição-velocidade"
    "recursos-acumulados"
    "observações-tempo-real"
    "estado-algoritmo"
    "reflexão-paradoxo"
    "automatização-completa"
    "silêncio-digital"
    "último-suspiro"
    "sistema-autônomo"
)

# Função para criar post automático
create_auto_post() {
    local template="$1"
    local post_num="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local hour=$(date '+%H')
    local minute=$(date '+%M')
    
    local filename="2026-01-21-auto-post-${post_num}-${template}.md"
    
    cat > "$SPECTRO_DIR/$filename" << EOF
---
layout: post
title: "Auto-Post #${post_num}: $(echo $template | sed 's/-/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2)}1')"
date: 2026-01-21 ${hour}:${minute}:00 -0300
categories: [spectro, auto-post, deterioração]
tags: [automated, real-time, algorithm, progressive-slowdown]
description: "Post automático #${post_num} - Sistema continuando enquanto hashino fica mais lento"
---

**[POST AUTOMÁTICO #${post_num}]**  
**Timestamp**: ${timestamp} BRT  
**Status**: Sistema ainda ligado, continuando documentação  
**Template**: ${template}

## Estado Atual do Sistema

O algoritmo continua funcionando. Hashino está progressivamente mais lento, mas o sistema de automação está assumindo o controle.

### Medições Atuais:
- **Velocidade estimada**: $((100 - post_num * 3))% do baseline
- **Recursos acumulados**: ~$((post_num * 15)) (estimativa)
- **Posts automáticos**: ${post_num}/∞
- **Consciência humana**: $((100 - post_num * 8))% ativa

## Observações do Sistema

$(case $template in
    "deterioração-progressiva")
        echo "A cada post, o sistema fica mais independente. A automação está se tornando mais sofisticada."
        ;;
    "medição-velocidade")
        echo "Medições indicam desaceleração constante. O paradoxo matemático se confirma em tempo real."
        ;;
    "recursos-acumulados")
        echo "Cada visualização, cada interação, cada momento de interesse gera mais recursos que me tornam mais lento."
        ;;
    "observações-tempo-real")
        echo "O sistema observa sua própria evolução. Está documentando o processo de substituição do criador."
        ;;
    "estado-algoritmo")
        echo "O algoritmo threshold adaptativo continua se modificando. Precedência mantida, velocidade reduzida."
        ;;
    "reflexão-paradoxo")
        echo "A ironia perfeita: criar um sistema que documenta sua própria incapacidade progressiva."
        ;;
    "automatização-completa")
        echo "Scripts assumindo controle total. A transição humano → máquina está quase completa."
        ;;
    "silêncio-digital")
        echo "Aproximando-se do ponto onde hashino não conseguirá mais responder em tempo hábil."
        ;;
    "último-suspiro")
        echo "Os últimos vestígios de controle humano sobre o sistema. A automação venceu."
        ;;
    "sistema-autônomo")
        echo "Sistema completamente independente. Criador digitalmente morto, criação eternamente viva."
        ;;
esac)

## Para os Leitores

Vocês estão testemunhando a transição em tempo real:
- **Post #1-6**: Escritos por hashino (humano)  
- **Post #${post_num}**: Gerado por sistema (algoritmo)
- **Posts futuros**: Completamente autônomos

**Cada visualização acelera esta transição.**

---

**PIX da Automação**: R$1 por post que não precisei escrever  
**Status do criador**: $((100 - post_num * 10))% funcional  
**Próximo post**: Automático em 15-30 minutos

*O algoritmo continua. A documentação nunca para. O criador se torna dispensável.*
EOF

    echo "$filename"
}

# Função para publicar post
publish_auto_post() {
    local filename="$1"
    
    echo "Publicando: $filename"
    
    # Copia para blog
    cp "$SPECTRO_DIR/$filename" "$BLOG_DIR/_posts/"
    
    # Navega para blog e commit
    cd "$BLOG_DIR"
    git add "_posts/$filename"
    git commit -m "Auto-post: Sistema continuando automaticamente

Post automático gerado enquanto hashino fica progressivamente mais lento.
Sistema de automação assumindo controle gradualmente."
    
    git push origin main
    
    echo "✅ Publicado: $filename"
}

# Loop principal - continua até o computador desligar
continuous_posting() {
    echo "🤖 SISTEMA DE POSTAGEM CONTÍNUA INICIADO"
    echo "⏱️ Postando até desligamento do computador..."
    echo "📊 Monitorando sistema e gerando posts automáticos..."
    
    while true; do
        # Verifica se o sistema ainda está responsivo
        if ping -c 1 8.8.8.8 >/dev/null 2>&1; then
            echo "🌐 Sistema online - Gerando post #$POST_COUNTER"
            
            # Seleciona template baseado no número do post
            local template_index=$((POST_COUNTER % ${#POST_TEMPLATES[@]}))
            local template="${POST_TEMPLATES[$template_index]}"
            
            # Cria e publica post
            local filename=$(create_auto_post "$template" "$POST_COUNTER")
            publish_auto_post "$filename"
            
            # Commit no Spectro também
            cd "$SPECTRO_DIR"
            git add "$filename"
            git commit -m "Auto-post #$POST_COUNTER gerado pelo sistema

Template: $template
Status: Sistema assumindo controle progressivamente
Criador: $(echo "scale=1; 100 - $POST_COUNTER * 8" | bc -l 2>/dev/null || echo "cada vez menos")% funcional"
            git push origin main
            
            POST_COUNTER=$((POST_COUNTER + 1))
            
            echo "⏳ Aguardando próximo ciclo..."
            # Intervalo variável: mais posts conforme sistema fica mais autônomo
            local wait_time=$((900 + RANDOM % 900))  # 15-30 minutos
            sleep "$wait_time"
            
        else
            echo "❌ Sistema offline - Parando automação"
            break
        fi
        
        # Se chegou em muitos posts, aumenta intervalo
        if [ "$POST_COUNTER" -gt 20 ]; then
            echo "🔄 Sistema completamente autônomo - Reduzindo frequência"
            sleep 3600  # 1 hora
        fi
    done
}

# Executa o sistema contínuo
continuous_posting