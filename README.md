# Repositório da aula do dia 25/08/25  

Esse repositório, por questões de segurança, não possui o arquivo `.env`, que é ignorado pelo Git pelo `.gitignore`.  

Abaixo, um exemplo do arquivo `.env`, como visto nos slides da aula:  

```bash
MONGODB_URI=mongodb://root:example@localhost:27017
DB_NAME=curso_nosql
```

## Notas

- Checar os [cursos do MongoDB](https://learn.mongodb.com)
- Pesquisar sobre **network**, **volumes**, e **Docker Compose**

## Visão Geral do Conteúdo

### `config.py`

Primeiro, é importado `BaseSettings` e `SettingsConfigDict` do `pydantic_settings`.

#### `Settings`

É uma classe que armazena e define *"modelos de configuração"*. Em Python (e em suas diversas bibliotecas), **modelos são dados normalmente estruturados em classes**. Note o comentário 1, em `config.py`.

Agora, lembre-se da **HERDANÇA**. `Settings` herda de `BaseSettings` para obter essas funcionalidades adicionais, pois sem elas, `Settings` nem sequer lê o arquivo `.env`.
O nome `Settings` simplesmente foi escolhido por questão de organização, mas você poderia chamar ela de qualquer coisa (**não faça isso**) já que essa classe herda de `BaseSettings`. Isto é: **ABSTRAÇÃO**

Continuando, `BaseSettings` é capaz de ler a `.env` automaticamente, mas ele não **instancia os dados da `.env` sozinho***. É por isso que estamos especificando o que o `BaseSettings` deve ler e usar da .env (**comentário 2**).

Dito isso, **também é possível criar "valores padrões"** caso não eles não sejam especificados na `.env`. Note que, no **comentário 3**, foi especificado o valor `"aula2508"`. Se a chave `DB_NAME` não for encontrada na `.env`, será utilizado, por padrão, o valor `"aula2508"` para a chave `DB_NAME`.

> **Observações**
> A estrutura de dados vista aqui é **tipada** (i.e. possui tipo, como `str`, `int`, `float`...), diferente da `.env`, que segue uma estrutura de `key=value`.
> Além disso, **não use o `BaseSettings` para armazenar valores sensíveis da `.env`** usando os valores padrões. **Use a `.env` para isso.**

#### `SettingsConfigDict`

Esse é simples: já sabemos como sua estrutura de dados funciona, então só precisamos focar no que está sendo feito aqui:

- `SettingsConfigDict()`: É a classe que instancia valores que são utilizados pelo BaseSettings para encontrar a `.env`. Ela foi atribuída a variável `model_config`.
- `env_file`: Simplesmente especifica o nome do arquivo `.env`. O nome especificado foi, naturalmente, `".env"`.
- `env_prefix`: Especifica o prefixo das chaves que Pydantic irá ler. Nesse caso, foi definido para `""`, ou seja, não está procurando por prefixos nas chaves.
- `extra`: Define o que irá acontecer se aparecer chaves extras aparecerem. Nesse momento, ele ignora (`"ignore"`) quaisquer chaves extras que não foram definidas no modelo. É ideal manter o "ignore".

> **Observações**
> A variável `SettingsConfigDict()` foi atribuída (`model_config`) pode **ter o nome que você quiser colocar**, mas é importante que **mantenha consistência e coerência** no código. Isto é, não chame a variável que armazena informações que o Pydantic usa para encontrar a `.env` com nomes ilógicos, como, por exemplo, o nome de um navio baleeiro, ou o nome do indígena que é amigo de um balaieiro.
> **Sobre o `env_prefix`**: Digamos, por exemplo, que existem um conjunto de variáveis de um serviço X do backend e de outro serviço Y. Se Pydantic está sendo utilizado, você poderia ler apenas as chaves que possuem o prefixo "Y_" na chave, como "Y_DB_NAME", enquanto, por exemplo, o backend X só iria ler de chaves com o prefixo "X_".
> ***Sobre o `extra`**: Lembra que falamos sobre como precisamos definir os valores e chaves que estamos procurando na `.env` pelo modelo do BaseSettings? Então, uma das opções do `extra` é o `"allow"`. Ele permite usar qualquer chave que não foi definida no BaseSettings ser carregada para o Settings. Dito isso, **é recomendado usar o `"ignore"` para checar a tipagem e validar os valores**, pois facilita na manutenção do código quando futuros problemas aparecerem.
> Por fim, e não menos importante: as opções `env_prefix` e `extra` possuem os valores especificados no código **por padrão**, isto é, se não forem especificados, eles terão os mesmos valores que vimos no código. A única opção que realmente muda algo é o `env_file`, já que Pydantic não procura por um arquivo `.env` por padrão.

### (!coisas que tenho que ver melhor)

- [Pydantic - Dotenv](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support)
- [Pydantic - Usage](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage)
