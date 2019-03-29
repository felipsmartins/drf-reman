Bem-vindo a documentação do FastSeller XT
=========================================

Se você quer uma visão geral do projeto ou código-fonte, visite [github](https://mkdocs.org).

Introdução
----------

Este projeto é sobre um sistema que tem como finalidade fazer a gestão das
versões publicadas/disponibilizadas do aplicativo **FastSeller XT** para os
clientes/usuários deste sistema.  
Todas as ações principais para este gerenciamento é feita através dos endpoints
da [API](/api).

**Para onde ir agora?**
  
Para começar a interagir com a API, siga com as intruções de
[instalação](/installation) na página a seguir.
 
 > **Nota**:  
 > É interessante ler a seção a seguir para familiarizar-se com a 
 terminologia usada durante a leitura da documentação.

Terminologia
------------
- **Customer: ** Um cliente, parceiro, empresa ou qualquer usuário que recebe um release.  
- **Release: ** Isso pode ter às vezes o mesmo valor semântico de "versão" (ver abaixo). Estritamente 
falando, release diz respeito a um lançamento, que pode ter coomo atributo *data do release*, 
*code name*, *código da versão (ex.: 1.2.3)*, etc.
- **Versão**: É um identificador "numérico" ou código da versão do release, algo como `0.2.3`. 
Nesse projeto, tomamos como inspiração o [Semantic Versioning](https://semver.org/).
- **App Publishing**: Representa um específico release disponibilizado
para um usuário do app.
Tem informações como a versão recebida pelo cliente, o próprio cliente e quando
este recebeu o update/release.

*Customer*, *cliente*, *usuário*, *empresa*, *parceiro* são termos intercambiáveis aqui.


