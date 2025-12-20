# Resposta da questão 6

A falha está sendo causada pela ausência da configuração WALLET_X_TOKEN_MAX_AGE no ambiente de Homologação/Produção. 
O código depende dessa variável, que provavelmente está definida apenas no ambiente local.
Isso indica um problema de configuração entre ambientes, e não de infraestrutura ou lógica da aplicação.