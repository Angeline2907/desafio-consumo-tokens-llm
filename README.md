# Desafio: Consumo de Tokens com Diferentes Prompts 🚀

Este repositório contém a resolução do desafio prático de análise de consumo de tokens em Modelos de Linguagem (LLMs). O objetivo é entender como a complexidade e o detalhamento de uma solicitação afetam diretamente os custos e o processamento da API.

## 📋 Objetivos do Desafio

1. Executar o programa utilizando um prompt curto.
2. Executar novamente utilizando um prompt mais detalhado.
3. Exibir os tokens de entrada, saída e o total em cada teste.
4. Compare os resultados e identifique qual solicitação consumiu mais tokens.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **OpenAI API SDK** (Modelo `gpt-4o-mini`)

## ⚙️ Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github="SEU_USUARIO"/desafio-consumo-tokens-llm.git
   ```

2. Instale a biblioteca necessária:
   ```bash
   pip install openai
   ```

3. Configure sua chave de API nas variáveis de ambiente:
   ```bash
   export OPENAI_API_KEY="sua_chave_aqui"
   ```

4. Execute o script:
   ```bash
   python analise_tokens.py
   ```

## 📊 Conclusão do Aprendizado

Os testes demonstraram que **prompts mais detalhados e contextualizados consomem significativamente mais tokens** (tanto na entrada, pelo tamanho do texto enviado, quanto na saída, pois geram respostas mais completas). Portanto, a engenharia de prompt deve equilibrar a precisão das instruções com a eficiência de custos.
