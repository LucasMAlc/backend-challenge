# Resposta da questão 8

Para normalizar serviços de terceiros que possuem interfaces diferentes, como provedores de e-mail ou SMS, o principal padrão que eu utilizaria é o Adapter. Esse padrão permite criar uma interface padrão para a aplicação e adaptar cada serviço externo para essa interface, sem precisar alterar o código que consome o serviço. Dessa forma, a aplicação não fica dependente da forma como cada fornecedor implementa sua API.

Além disso, eu utilizaria o Strategy para encapsular as diferentes estratégias de envio e permitir a troca do fornecedor de forma simples, seja por configuração ou por regra de negócio. Isso facilita a manutenção e a evolução do sistema, pois novos fornecedores podem ser adicionados sem impacto significativo no código existente.

Por fim, o Factory pode ser usado para centralizar a criação dessas estratégias/adapters, evitando condicionais espalhadas pelo sistema e deixando o código mais limpo e organizado.

Essa combinação de padrões melhora a legibilidade, facilita testes e torna a aplicação mais flexível para mudanças futuras.