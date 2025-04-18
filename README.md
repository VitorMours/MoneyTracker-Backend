# Money Tracker Backend
Baseado no vídeo do [How to build React + FastAPI application](https://www.youtube.com/watch?v=0zb2kohYZIM&t=2762s), decidi criar miha primeira aplicação web "full stack" em vias de fato. Decidi dividir o projeto em duas partes, o back-end e o front-end, para poder rodar os dois em plataformas diferentes, e executar eles como uma aplicação full-stack em vias de fato.

# Executando o Projeto
Para executar esse projeto, basta-se entrar dentro do diretório do projeto, e executar o comando:

```sh
fastapi dev main.py
```

que assim ele vai executar o projeto dentro do ambiente de desenvolvimento, criando automaticamente um banco de dados sqlite, para uso rápido, e sem necessidade de configuração, dos serviços os quais estão presentes dentro desse projeto.

Temos que o projeto possui dois endpoins principais, que podem ter suas documentações acessadas dentro da url `http://localhost:8000/docs`, quando o projeto já estiver rodando, sem maiores problemas, e dentro dele, podemos ver como podemos criar as depesas, para armazenar elas dentro do banco e dados, e como podemos requisitar elas, para que sejam lidas e sejam mostradas de forma organizada dentro do Front-end.

## FastAPI
### Como e Porque
Devido à sua velocidade, e utilidade, e familiaridade que possuo com o Flask -- framework de desenvolvimento web -- A ferramenta utilizada dentro desse projeto foi o FastAPI, pois permite criar APIs rápidas, autodocumentáveis, e que usam o conceito de requisições assíncronas dentro da sua estruturação e funcionamento. Isso aliado com a experiência do desenvolvedor sendo parecida com a do Flask, me fez ver uma possibilidade com essa ferramenta.

### Migração de Dados
Um fato que pode ser observado dentro da interface criada, é que precisamos dentro da ferramenta, integrar um sistema de migração de dados pelo fato de que o mesmo não existe dentro da nossa API. Isso pode ser feito por meio de ferramentas que já são famosas dentro do  ecossistema de desenvolvimento do python, como o alembic. A exemplificação de problemas que podem ser vistos com coisas assim, é a necessidade de mudança que os bancos de dados podem ter, em relação às suas nomeclaturas, funcionamento, e até estruturação.


# Próximos Passos

Os próximos passos com esse projeto, para aprofundar o funcionamento do mesmo dentro da esfera de programação full-stack, usando o mesmo em conjunto com o React, é criar um back-end que suporte sistemas de login -- por meio de elementos e ferramentas como o JWT por exemplo -- e criar uma forma de, por meio de configuração mediante variáveis de ambiente, o banco de dados de desenvolvimento continue sendo o SQLite, mas dentro da produção, o mesmo seja modificado para o PostgreSQL ou o MySQL, de forma automática.