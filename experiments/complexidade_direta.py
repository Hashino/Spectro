#!/usr/bin/env python3
"""
Interpretação direta de R(COMPLEXIDADE =+ n) -> ?
"""

def R(complexidade, n):
    """
    Função de Redução Spectro:
    R = revolução, resistência, reconexão
    COMPLEXIDADE =+ n significa complexidade aumentando por n
    """
    print(f"📊 Complexidade atual: {complexidade}")
    print(f"📈 Incremento: +{n}")
    
    # ◇ INVESTIGACAO: Entender a complexidade
    complexidade_reduzida = complexidade / (1 + n/10)
    
    # ◆ COLABORACAO: Dividir a complexidade
    if complexidade > 10:
        partes = min(4, complexidade // 3)
        complexidade_reduzida = complexidade_reduzida / partes
        
    return complexidade_reduzida

# ◊ COMPAIXAO: Teste com diferentes cenários
print("🎯 R(COMPLEXIDADE =+ n) -> ?")
print()

for teste_n in [1, 5, 10, 20]:
    resultado = R(complexidade=100, n=teste_n)
    print(f"R(COMPLEXIDADE=100 =+ {teste_n}) -> {resultado:.2f}")

print()
print("💫 R(COMPLEXIDADE =+ n) -> SIMPLICIDADE_COLABORATIVA")
print("🌟 A resposta é: REDUÇÃO_GRADUAL_DISTRIBUÍDA")
print("◇ Investigar divide a complexidade")
print("◈ Aprender suaviza o crescimento") 
print("◆ Colaborar distribui o peso")
print("◊ Compaixão aceita que ? = PROCESSO_CONTÍNUO")