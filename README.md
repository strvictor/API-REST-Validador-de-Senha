## Desafio Senha Segura

Este projeto foi desenvolvido como solução para o desafio "Senha Segura", proposto no repositório [desafios](https://github.com/backend-br/desafios/tree/master) do perfil [backend-br](https://github.com/backend-br) no GitHub.

O objetivo do desafio é criar um endpoint do tipo `POST` no formato `"{host}/validate-password/"`, onde o corpo da requisição deve conter o campo `password`. O endpoint realiza as validações necessárias e retorna informações sobre a conformidade da senha com os critérios estabelecidos.
<hr>


## Tecnologias Utilizadas

- **Linguagem**: Python 3.12
- **Framework**: FAST API

## Como Executar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/strvictor/API-REST-Validador-de-Senha.git
    cd API-REST-Validador-de-Senha
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate # Linux/Mac
    venv\Scripts\activate # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o servidor:
    ```bash
    flask run
    ```

5. Acesse o endpoint no navegador ou via ferramenta como Postman:
    ```
    POST http://localhost:8000/api/v1/validate-password/
    ```

## Exemplos de Requisição

### Regras

- Verificar se a senha possui pelo menos 08 caracteres.
- Verificar se a senha contém pelo menos uma letra maiúscula.
- Verificar se a senha contém pelo menos uma letra minúscula.
- Verificar se a senha contém pelo menos um dígito numérico.
- Verificar se a senha contém pelo menos um caractere especial (e.g, !@#$%).

### Requisição
```json
POST api/v1/validate-password/
Content-Type: application/json

{
  "password": "Ex@mple123"
}
```

### Resposta
```json
{
	"valid": False,
	"reason": "Password must contain at least one lowercase letter."

```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).