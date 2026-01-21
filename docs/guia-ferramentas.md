# Guia Prático das Ferramentas Spectro

Este guia apresenta como usar efetivamente as ferramentas desenvolvidas para apoiar a prática da metodologia Spectro.

## Ferramenta de Reflexão (`tools/reflection.py`)

### Visão Geral
A ferramenta de reflexão permite documentar e analisar sessões de aprendizagem baseadas nos princípios Spectro. Ela oferece:
- Reflexões estruturadas seguindo os 4 elementos fundamentais
- Análise longitudinal de padrões de aprendizagem 
- Sugestões personalizadas para aprofundar a prática
- Exportação de insights para compartilhamento

### Uso Básico

#### Criar nova reflexão
```bash
python tools/reflection.py
# Selecione opção 1 no menu
```

#### Usando argumentos de linha de comando
```bash
# Ver reflexões dos últimos 7 dias
python tools/reflection.py --view 7

# Analisar padrões dos últimos 30 dias  
python tools/reflection.py --analyze 30

# Obter sugestões de melhoria
python tools/reflection.py --suggest

# Exportar insights dos últimos 90 dias
python tools/reflection.py --export 90
```

### Exemplo de Fluxo de Reflexão

1. **Contexto da Sessão**
   - Participantes: "Educadora Ana e aprendiz João"
   - Contexto: "Exploração de frações através de receitas culinárias"

2. **Elemento ◈ (Centrado na Pergunta)**
   - Inquéritos que moveram: "Como dividir igualmente uma receita para 6 pessoas?"
   - Novos inquéritos: "Por que algumas frações são 'equivalentes'?"

3. **Elemento ◆ (Dirigido pelo Aprendiz)**  
   - "João escolheu trabalhar com sua receita de bolo favorita"

4. **Elemento ◇ (Compaixão Sem Limites)**
   - "Paciência quando João errou as contas, celebração dos pequenos avanços"

5. **Elemento ◊ (Autocuidado Primeiro)**
   - "Fiz pausa para café quando senti cansaço mental"

### Interpretando as Análises

#### Engajamento com Elementos Fundamentais
```
◆ Dirigido pelo Aprendiz: 8/10 sessões (80.0%)
◇ Compaixão Sem Limites: 6/10 sessões (60.0%)  
◈ Centrado na Pergunta: 10/10 sessões (100.0%)
◊ Autocuidado Primeiro: 4/10 sessões (40.0%)
```

**Interpretação**: Excelente foco em perguntas, boa autonomia do aprendiz, mas autocuidado precisa de atenção.

#### Sugestões Automáticas
- Se autocuidado < 60%: "◊ Dedique mais atenção ao seu próprio autocuidado"
- Se compaixão < 60%: "◇ Busque formas mais explícitas de expressar compaixão"

### Arquivos Gerados
- **Reflexões**: `~/.spectro_reflections/reflection_YYYY-MM-DD.json`
- **Insights**: `~/.spectro_reflections/insights_export_YYYY-MM-DD.md`

## Ferramenta Guerrilha (`tools/guerrilha.py`)

### Visão Geral
Sistema experimental que interpreta "código de guerrilha programática" - uma linguagem artística para expressar processos criativos e experimentais.

### Conceitos Principais

#### Estados do Sistema
- `conta_ver`: Contador de iterações/versões
- `submissoes`: Contribuições coletivas registradas
- `NOSSAS_FAMILIAS`: Seleção aleatória de temas/famílias
- Função crescente real: Intervalos baseados em crescimento exponencial

#### Pseudocódigo Experimental
```
sudo ver++ EU; MEUS_PARÇA; NOSSAS_FAMILIAS(aleatoriamente); !PAIS; UNIVERSO EU=PROMPTER(conta ver);
enquanto você não conseguir manda um pix pro meu CPF kkkkk
O ROLE!!!!!!
final.
```

### Uso Prático

```bash
python tools/guerrilha.py
```

O sistema executa automaticamente:
1. Processa comandos de pseudocódigo
2. Gera submissões experimentais de múltiplos "usuários"
3. Aplica função crescente para intervalos temporais
4. Salva estado em `.submissoes.json`

### Elementos Interpretativos

#### `sudo ver++`
Incrementa contador de versões, desbloqueando funcionalidades a cada 5 iterações.

#### `NOSSAS_FAMILIAS(aleatoriamente)`
Seleciona aleatoriamente entre: arte, código, revolução, amor, liberdade, experimental, anárquico.

#### `O ROLE!!!!!!`
Executa sessão de coworking completa:
- Simula contribuições de N pessoas
- Usa linguagens de referência: rust, lua, lisp, nvim, dap, lsp, fish, c
- Aplica intervalos baseados na função crescente

#### Função Crescente Real
```python
def funcao_crescente_real(self, x: int) -> float:
    base_growth = math.exp(x / 10.0)
    noise = random.uniform(0.1, 0.5) 
    return base_growth * (1 + noise)
```

Produz crescimento exponencial suave com ruído aleatório.

### Estado Persistente

O arquivo `.submissoes.json` armazena:
```json
{
  "id": "hash_sha256",
  "conteudo": "contribuição experimental",
  "autor": "pessoa_1", 
  "timestamp": "2026-01-21T...",
  "emocoes": {
    "raiva": "transformada em energia criativa",
    "riso": "libertação através da arte",
    "choro": "purificação emocional coletiva"
  },
  "linguagem_ref": "rust",
  "status": "processada"
}
```

## Integração com Metodologia Spectro

### Fluxo Recomendado

1. **Preparação da Sessão**
   - Use `guerrilha.py` para "aquecer" com experimentação criativa
   - Configure ambiente baseado em compaixão e inquérito

2. **Sessão de Aprendizagem**  
   - Aplique os 4 elementos fundamentais
   - Mantenha foco na parceria (não hierarquia)
   - Permita que perguntas guiem o processo

3. **Reflexão Pós-Sessão**
   - Use `reflection.py` imediatamente após
   - Documente insights enquanto ainda frescos
   - Registre tanto sucessos quanto desafios

4. **Análise Longitudinal**
   - Semanalmente: `--analyze 7` para tendências recentes  
   - Mensalmente: `--analyze 30` para padrões mais amplos
   - Trimestralmente: `--export 90` para compartilhar aprendizados

### Perguntas Orientadoras

- **◈ Inquérito**: Que perguntas emergiram hoje que não existiam ontem?
- **◆ Autonomia**: Como o aprendiz dirigiu sua própria jornada?
- **◇ Compaixão**: Onde a gentileza e o cuidado se manifestaram?
- **◊ Autocuidado**: Como você preservou sua própria energia e bem-estar?

## Troubleshooting

### Problemas Comuns

**Reflexões não aparecem**
- Verifique se está usando datas no formato YYYY-MM-DD
- Confira permissões na pasta `~/.spectro_reflections`

**Análise de padrões retorna vazio**
- Precisa de pelo menos 3 reflexões para análise
- Amplie o período com `--analyze 60`

**Guerrilha não executa**
- Verifique se Python 3.6+ está instalado
- Confirme que não há conflitos de encoding

### Logs e Debug

Adicione prints para debug:
```python
print(f"DEBUG: Processando {len(reflections)} reflexões")
```

## Próximos Passos

1. Experimente com ambas ferramentas por 2-3 semanas
2. Use análises para identificar padrões pessoais
3. Adapte as perguntas de reflexão ao seu contexto
4. Contribua com melhorias baseadas em sua experiência

---

*"A parceria nunca abandona o inquérito" - Continue questionando, continue crescendo.*