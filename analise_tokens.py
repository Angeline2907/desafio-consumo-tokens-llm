import os
from openai import OpenAI

# Inicializa o cliente da API
# Certifique-se de configurar a variável de ambiente OPENAI_API_KEY
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def executar_teste(nome_teste, prompt_texto):
    print(f"\n=== {nome_teste} ===")
    print(f"Prompt enviado: '{prompt_texto}'")
    
    # Executa a chamada para o modelo
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_texto}]
    )
    
    # 3. Extraindo os tokens de entrada, saída e total
    tokens_entrada = resposta.usage.prompt_tokens
    tokens_saida = resposta.usage.completion_tokens
    tokens_total = resposta.usage.total_tokens
    
    print(f"-> Tokens de Entrada (Prompt): {tokens_entrada}")
    print(f"-> Tokens de Saída (Resposta): {tokens_saida}")
    print(f"-> Total de Tokens Consumidos: {tokens_total}")
    
    return tokens_entrada, tokens_saida, tokens_total

# 1. Executando com prompt curto
prompt_curto = "Me dê uma dica rápida de estudo."
entrada_1, saida_1, total_1 = executar_teste("Teste 1: Prompt Curto", prompt_curto)

# 2. Executando com prompt detalhado
prompt_detalhado = (
    "Aja como um mentor de estudos experiente focado em programação. "
    "Me dê uma dica detalhada de estudo para quem está aprendendo Python do zero, "
    "incluindo um método prático e como organizar o tempo na semana."
)
entrada_2, saida_2, total_2 = executar_teste("Teste 2: Prompt Detalhado", prompt_detalhado)

# 4. Comparação dos resultados
print("\n" + "="*40)
print("=== 4. COMPARAÇÃO DE RESULTADOS ===")
print("="*40)
print(f"Prompt Curto     | Entrada: {entrada_1} | Saída: {saida_1} | Total: {total_1}")
print(f"Prompt Detalhado  | Entrada: {entrada_2} | Saída: {saida_2} | Total: {total_2}")
print("-"*40)

if total_2 > total_1:
    print(f"Resultado: O **Prompt Detalhado** consumiu mais tokens no total (Diferença de {total_2 - total_1} tokens).")
else:
    print(f"Resultado: O **Prompt Curto** consumiu mais tokens no total.")
