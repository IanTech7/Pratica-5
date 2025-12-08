# Prática 5: Configuração do SystemD e Versionamento com Git

**Disciplina:** SEL0337 - Projetos em Sistemas Embarcados  
**Alunos:** 
Ian Henrique Moronte Tech - 6958142
Hélio Arthur Molina - 14781401

## Resumo do Projeto
Esta prática teve como objetivo configurar a inicialização automática de serviços (scripts) no Linux embarcado (Raspberry Pi OS) utilizando o **SystemD**. Além disso, foi utilizado o **Git** e **GitHub** para versionamento e documentação dos códigos.

O projeto consiste em dois serviços principais que iniciam automaticamente no boot (inicialização) da placa:
1. Um script em Bash para controle de GPIO.
2. Um script em Python para execução de tarefa automatizada.

## Parte 1: Serviço com Bash Script
### Descrição
Foi criado um serviço chamado `piscar.service` que executa um script shell (`piscar.sh`). Este script acessa diretamente os diretórios do sistema (`/sys/class/gpio`) para configurar o pino GPIO 18 como saída e realizar o "blink" (piscar) de um LED.
