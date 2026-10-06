# Event Tech 🤖

## Equipe👥

- Nome: Sophia Silveira dos Santos | RM: 571932
- Nome: Renato da Silva Tenorio | RM: 572928
- Nome: Renato Ruiz Ferreira Fonseca Scolamieri | RM: 568667 (❁´◡`❁)
- Nome: Matheus Ferreira Antônio | RM: 570933
- Nome: João Vitor Cruz de Lima  | RM: 571277

## Objetivo📋

O objetivo da Event Tech é produzir uma página viável para o cadastro, alteração, listagem e deleção de dados referentes aos eventos que a Event Tech cedia, ou promove. Queremos fazer o sistema com base o Python, em orientação a objetos, para melhor compreenção e segurança do banco de dados.

## Tecnologias 🧑‍💻

- Python (Programação Orientada a Objetos)
- APIs
- Banco de Dados (OracleDB)
- HTML, CSS

## Como Executar? 🤔

1. Faça o download do zip, ou dê um cone direto do github;
2. Abra o arquivo no VSCode e execute o script App.py;
3. Copie e cole o localhost que aparecer no terminal;
4. Aproveite.

## Script SQL

```
CREATE TABLE EVENTOS (
ID_EVENTO NUMBER PRIMARY KEY,
NOME_EVENTO VARCHAR2(100) NOT NULL,
CATEGORIA VARCHAR2(50) NOT NULL,
DATA_EVENTO DATE NOT NULL,
LOCAL_EVENTO VARCHAR2(100) NOT NULL,
CAPACIDADE NUMBER NOT NULL,
VALOR_INGRESSO NUMBER(10,2),
RESPONSAVEL VARCHAR2(100) NOT NULL,
STATUS VARCHAR2(20) DEFAULT 'ATIVO',
DATA_CADASTRO DATE DEFAULT SYSDATE
);
```

## API usada



## Estrutura do Projeto



## Uso de IA

Foram usadas IAs do "GitHub Copilot" e "Claude" para prever possíveis erros e aprendizado do uso da programação orientada à objetos no Python.
