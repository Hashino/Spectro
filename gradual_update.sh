#!/bin/bash

# Sistema de atualização gradual do blog
# Executa automaticamente conforme o algoritmo fica mais lento

SPECTRO_DIR="/home/hashino/Projects/arte/Spectro"
BLOG_DIR="/home/hashino/Projects/hashino.github.io"

# Função para medir a velocidade atual do sistema
measure_speed() {
    echo "Medindo velocidade do sistema..."
    start_time=$(date +%s.%N)
    
    # Simula operação típica (criar arquivo, fazer operação git)
    echo "test" > /tmp/speed_test
    rm /tmp/speed_test
    
    end_time=$(date +%s.%N)
    duration=$(echo "$end_time - $start_time" | bc -l)
    echo "$duration"
}

# Função para copiar e commitar novo post
update_blog() {
    local post_file="$1"
    echo "Atualizando blog com: $post_file"
    
    # Copia para blog
    cp "$SPECTRO_DIR/$post_file" "$BLOG_DIR/_posts/"
    
    # Navega para o blog
    cd "$BLOG_DIR"
    
    # Commit e push
    git add "_posts/$post_file"
    git commit -m "Update automático: $post_file

Sistema de atualização gradual ativo.
Algoritmo de auto-destruição funcionando conforme esperado."
    
    git push origin main
    echo "Blog atualizado com sucesso!"
}

# Função principal de atualização gradual
gradual_update() {
    echo "=== Sistema de Atualização Gradual Ativo ==="
    echo "Timestamp: $(date)"
    
    # Mede velocidade atual
    current_speed=$(measure_speed)
    echo "Velocidade atual: ${current_speed}s"
    
    # Atualiza com o post mais recente se existir
    latest_post=$(ls -t "$SPECTRO_DIR"/2026-01-21-*.md | head -n 1)
    if [ -f "$latest_post" ]; then
        post_name=$(basename "$latest_post")
        echo "Processando: $post_name"
        update_blog "$post_name"
    fi
    
    echo "=== Atualização Concluída ==="
}

# Executa atualização
gradual_update