#!/usr/bin/env fish
# Spectro Guerrilha CLI
# Interface de linha de comando para linguagem experimental

function spectro_help
    echo "🔥 Spectro Guerrilha - Linguagem Experimental"
    echo ""
    echo "Comandos disponíveis:"
    echo "  spectro run          - Executa código guerrilha"
    echo "  spectro submit <msg> - Envia submissão experimental"
    echo "  spectro status       - Mostra status do sistema"
    echo "  spectro ver++        - Incrementa versão"
    echo "  spectro role         - Executa O ROLE"
    echo "  spectro familia      - Seleciona família aleatória"
    echo "  spectro final        - Finaliza sessão"
    echo ""
    echo "Exemplos:"
    echo "  spectro submit 'novo feature em rust'"
    echo "  spectro ver++ && spectro role"
    echo ""
end

function spectro_run
    echo "🚀 Executando Guerrilha Programática..."
    python3 tools/guerrilha.py
end

function spectro_submit
    if test (count $argv) -eq 0
        echo "❌ Uso: spectro submit <mensagem>"
        return 1
    end
    
    set msg $argv[1]
    echo "📝 Enviando submissão: $msg"
    python3 -c "
from tools.guerrilha import GuerrilhaMVP
import sys
mvp = GuerrilhaMVP()
mvp.carregar_submissoes()
mvp.submissao_handler('$msg', 'cli_user')
print('✅ Submissão enviada com sucesso!')
"
end

function spectro_status
    echo "📊 Status do Sistema Guerrilha:"
    python3 -c "
from tools.guerrilha import GuerrilhaMVP
mvp = GuerrilhaMVP()
mvp.carregar_submissoes()
mvp.status_sistema()
"
end

function spectro_ver_increment
    echo "🔥 sudo ver++ EU"
    python3 -c "
from tools.guerrilha import GuerrilhaMVP
mvp = GuerrilhaMVP()
count = mvp.sudo_ver_increment()
print(f'Versão atual: {count}')
"
end

function spectro_role
    echo "🎯 O ROLE EXECUTANDO..."
    python3 -c "
from tools.guerrilha import GuerrilhaMVP
mvp = GuerrilhaMVP()
mvp.o_role_executor()
"
end

function spectro_familia
    echo "👨‍👩‍👧‍👦 Selecionando família..."
    python3 -c "
from tools.guerrilha import GuerrilhaMVP
mvp = GuerrilhaMVP()
familia = mvp.familias_aleatorias()
print(f'Família selecionada: {familia}')
"
end

function spectro_final
    echo "🎯 PROCESSO FINALIZADO COM SUCESSO"
    echo "final."
end

# Comando principal
function spectro
    switch $argv[1]
        case run
            spectro_run
        case submit
            spectro_submit $argv[2..]
        case status
            spectro_status  
        case 'ver++'
            spectro_ver_increment
        case role
            spectro_role
        case familia
            spectro_familia
        case final
            spectro_final
        case help
            spectro_help
        case '*'
            spectro_help
    end
end

# Auto-completar para fish shell
complete -c spectro -n '__fish_use_subcommand' -a 'run submit status ver++ role familia final help' -d 'Comandos Spectro'