FastSeller API
==============

FastSeller XT - Release management system.  
Este projeto é sobre uma simples API para gerenciamento de release/versões
lançadas para clientes do Fast Seller app. Os principais recursos da API são:
* Customers: Que representa uma empresa/usuário/cliente do app (no caso, FastSeller XT);
* Releases: São as versões do app; Tem informações como código da verão, code name, e data do release;
* App Publishing: Representa um específico release do app disponibilizada para um cliente/usuário do app. Tem informações como a versão recebida pelo cliente, o próprio cliente e qaundo foi disponibilizada para ele.
 

Requirements
------------

**Principais requerimentos são:**

- Python 2.7+
- SQLite 3 - Isso deveria vir por padrão com o Python.
- pip
- virtualenv - Embora opcional, é interessante tê-lo não poluir o espaço global do sistema com pacotes deste projeto e ainda isolar o ambient.

As demais depêndencias estão listados no arquivo interno do projeto (requirements).

Instalação
----------

Clone esse projeto (ou extrai-o, se tiver recebido o arquivo comprimido) e entre para o diretório raiz do projeto e, opcionalmente, 
crie um [virtual environment](https://virtualenv.pypa.io/en/latest/):
  
`cd fastsellerxt; virtualenv virtualenv`  

Em seguida ative o virtual env que você criou:

`~$ source virtualenv/bin/activate`

Feito isso, o próximo passo é instalar as dependências do projeto.  

`~$ pip install -r requirements/prod.txt`  

Uma vez que e o Django, DRF e demais dependências foram instaladas, aplicaremos e sincronizaremos as migrations com a base de dados. Como estamos usando SQLite, você não precisa de nenhuma configuração adicional. Então:
  
`~$ python manage.py migrate`

-------
FAQ
---

Q: **Por que decidi usar Django Rest Framework ao invés de algo mais "lightweight"
como [Flask](http://flask.pocoo.org/), [Bottle](https://bottlepy.org) ou [responder](https://python-responder.org/)?**  
R: Primeiramente, deixe-me falar: Amo Flask e qualquer projeto do pocoo. Os projetos do Kennet Reitz são sempre inovadores e feitos com fito em experiência do desenvolvedor (DX).
[Armin Ronacher - AKA @mitsuhiko](https://twitter.com/mitsuhiko) e [Kenneth Reitz](https://twitter.com/kennethreitz) são programadores que admiro muito.
Agora, respondendo objetivamente, o projeto poderia ser escrito em qualquer uma das tecnologias citadas, mas devidos aos requerimentos e deadlines, optei pelo ferramenta que estou bem mais confortável, Django. 
O fato do DRF ter vários recursos out-of-box é um grande atrativo, além de estar em conformidade (ao menos em maior grau) 
com o design proposto na [dissertação](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) de [Roy Fielding](https://en.wikipedia.org/wiki/Roy_Fielding).
Em Flask eu teria de escrever a infraestrutura de serializadores e outros services antes mesmo de projetar a API propriamente dita.

Q: **Por que escolheu uma versão do Django da série 1.x se já existe a série 2?**  
R: Bem, a verdade é que ainda não tenho experiência com a série 2.x, algumas coisinhas mudaram.
Poderia tề-lo escolhido, mas com deadlines não queria arriscar. 
A experiência me mostrou algumas vezes (e de forma dolorosa) que aprender uma tecnologia em curso de um projeto com um prazo limitado é bem ruim.
