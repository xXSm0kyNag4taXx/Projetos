# 🎲 D20 simulator

**D20 simulator** é uma aplicação simples para rolar dados no formato comum de jogos de RPG, como `1d20+3`. É uma ferramenta prática para jogadores e mestres de jogo, permitindo calcular resultados de lançamentos com modificadores.

---

## 📋 Funcionalidades

- Rola um ou mais dados de diferentes tipos (ex: `1d6`, `2d20`, `3d8+5`).
- Suporte a modificadores positivos ou negativos (ex: `1d10-2`).
- Calcula e exibe a soma total dos lançamentos.
- Valida a entrada para evitar formatos incorretos.

---

## 🚀 Como Usar

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/xXSm0kyNag4taXx/rollmigas.git# Projetos
   
2. Navegue até a pasta do projeto
   
cd rollmigas

3. Execute o programa:

python3 rollmigas.py

4. Digite o lançamento desejado no formato:

XdY+Z:
X: Quantidade de dados.
Y: Número de faces do dado.
Z: Modificador opcional (+ ou -).
Exemplos válidos:
1d20+3
2d6
3d8-1
Para encerrar, digite "n" quando perguntado se deseja lançar novamente.

🛠️ Tecnologias Utilizadas

Python 3: Linguagem de programação principal.
Biblioteca random: Para gerar os números aleatórios.
Biblioteca re: Para validar e interpretar a entrada do usuário.

📚 Estrutura do Código

lancar_dado(tipo, quantidade): Realiza os lançamentos dos dados.
interpretar_entrada(entrada): Valida e interpreta a entrada do usuário.
main(): Gerencia o fluxo principal do programa.

📝 Melhorias Futuras

Adicionar suporte para rolagens com vantagens/desvantagens.
Implementar interface gráfica para facilitar o uso.
Registrar o histórico de lançamentos em um arquivo de log.

💡 Contribuições

Contribuições são bem-vindas! Se você tiver ideias ou encontrar problemas, abra uma issue ou envie um pull request.

🎮 Sobre o Autor

Feito com dedicação por um entusiasta de Python e RPGs!
Se tiver dúvidas ou sugestões, entre em contato:

GitHub: xXSm0kyNag4taXx
Email: Joaomiguelmonteiro33@gmail.com
