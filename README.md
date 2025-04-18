# Backend




## FastAPI
### Migração de Dados
Um fato que pode ser observado dentro da interface criada, é que precisamos dentro da ferramenta, integrar um sistema de migração de dados pelo fato de que o mesmo não existem dentro da nossa base de dados. Isso pode ser feito por meio de ferramentas que já são famosas dentro do  ecossistema de desenvolvimento do python, tipo o alembic. A exemplificação de problemas que podem ser vistos com coisas assim, é o fato que  dentro do sistema construído no estudo, os campos possuem nomes diferentes dos que foram em práticas, e quando houve a necessidade de haver  uma mudança desses nomes, houve certa dificuldade do mesmo ser feito.