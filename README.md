# Sistema de Monitoramento de Reservatório de Água

Este projeto é uma simulação de um sistema de controle de níveis de água para um reservatório, desenvolvido como atividade para a disciplina de Desenvolvimento de Sistemas de Informação (DSI). 

O sistema utiliza a biblioteca **Colorama** para exibir alertas visuais coloridos no terminal, facilitando a identificação rápida do status do reservatório.

## Funcionalidades

- **Tabela de Referência:** Exibe todos os níveis possíveis, suas descrições e cores correspondentes.
- **Leitura em Tempo Real:** Simula a leitura de um sensor utilizando valores aleatórios.
- **Alertas Coloridos:** 
  - 🔴 **Nível 1:** Muito baixo (crítico)
  - 🟡 **Nível 2:** Baixo
  - 🟢 **Nível 3:** Médio
  - 🔵 **Nível 4:** Alto
  - 🟣 **Nível 5:** Muito alto (alerta)

## Tecnologias Utilizadas

- **Python 3**
- **Biblioteca Colorama:** Para estilização do terminal.

## Pré-requisitos

Antes de rodar o projeto, você precisará ter o Python instalado e a biblioteca `colorama`. Você pode instalá-la via terminal com o comando:
```bash
pip install colorama
