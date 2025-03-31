# Seguidores do Instagram

Este projeto em Python permite que você verifique quais seguidores do Instagram não te seguem de volta. 

⚠️ Utiliza dados obtidos diretamente da sua conta do Instagram. ⚠️

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas: `json`, `datetime` (já incluídas na biblioteca padrão do Python)

## Como Usar

### 1. Obtenha suas informações do Instagram

1. Acesse a **Central de Contas** do Instagram.
2. Selecione a opção **Suas informações e permissões**.
3. Clique em **Baixar suas informações**.
4. Em seguida, escolha **Baixar ou transferir informações** e selecione **Algumas das suas informações**.
5. Procure pela opção **Seguidores e seguindo** e baixe as informações no seu dispositivo.
6. Em **Intervalo de datas**, selecione **Desde o início**.
7. Escolha o formato **JSON** e aguarde o download (pode levar alguns minutos ou horas — a Meta te avisará por e-mail quando estiver disponível).
8. Extraia o arquivo ZIP e mova a pasta **followers_and_following** para o diretório da aplicação.

### 2. Executando a Aplicação

Para rodar a aplicação, abra o terminal e navegue até a pasta onde a aplicação está localizada. Em seguida, execute o seguinte comando:

```bash
python main.py
```

### 3. Resultado

A aplicação irá gerar uma lista de seguidores que você está seguindo, mas que não te seguem de volta. Os resultados serão salvos em um arquivo de texto dentro da pasta _output_.

## Contribuições 🫱🏽‍🫲🏽

Contribuições são bem-vindas! Se você deseja adicionar recursos ou fazer melhorias, sinta-se à vontade para abrir um pull request.