FastSeller XT
=============

Este projeto é sobre um sistema que tem como finalidade fazer a gestão das
versões publicadas/disponibilizadas do aplicativo FastSeller XT para os
clientes/usuários deste sistema.  
Todas as ações principais para este gerenciamento é feita através dos endpoints da API.

**Documentação:**  

Há uma [documentação](http://felipsmartins.github.io/fastsellerxt/doc/) completa escrita para esse projeto.
A documentação cobre todo o processo de instação da aplicação
bem como descreve os endpoints da [API](http://felipsmartins.github.io/fastsellerxt/doc/api/).  
Link da doc: [http://felipsmartins.github.io/fastsellerxt/doc/](http://felipsmartins.github.io/fastsellerxt/doc/)


Instalação
----------

**Principais requerimentos são:**

- Python 2.7 (isso *deveria* ser compatível com Python 3, mas não foi testado)
- [GNU Make](https://www.gnu.org/software/make/)
- [pip](https://pypi.org/project/pip/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- Git (opcional) - Necessário se a obtenção so source-code é via `git clone` (que é o recomendado) 
- SQLite 3 - Isso *deveria* vir por padrão com o Python.

Siga o link para a documentação para mais detalhes:
[http://felipsmartins.github.io/fastsellerxt/doc/installation/](http://felipsmartins.github.io/fastsellerxt/doc/installation/)

-------
FAQ
---

**Q: Por que decidi usar Django Rest Framework ao invés de algo mais "lightweight"
como [Flask](http://flask.pocoo.org/), [Bottle](https://bottlepy.org) ou [responder](https://python-responder.org/)?**  
  
**R:** Primeiramente, deixe-me falar: Amo Flask e qualquer projeto do pocoo. Os projetos do Kennet Reitz são sempre inovadores e feitos com fito em experiência do desenvolvedor (DX).
[Armin Ronacher - AKA @mitsuhiko](https://twitter.com/mitsuhiko) e [Kenneth Reitz](https://twitter.com/kennethreitz) são programadores que admiro muito.
Agora, respondendo objetivamente, o projeto poderia ser escrito em qualquer uma das tecnologias citadas, mas devidos aos requerimentos e deadlines, optei pelo ferramenta que estou bem mais confortável, Django. 
O fato do DRF ter vários recursos out-of-box é um grande atrativo, além de estar em conformidade (ao menos em maior grau) 
com o design proposto na [dissertação](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) de [Roy Fielding](https://en.wikipedia.org/wiki/Roy_Fielding).
Em Flask eu teria de escrever a infraestrutura de serializadores e outros services antes mesmo de projetar a API propriamente dita.

**Q: Por que escolheu uma versão do Django da série 1.x se já existe a série 2?**
    
**R:** Bem, a verdade é que ainda não tenho experiência com a série 2.x, algumas coisinhas mudaram.
Poderia tề-lo escolhido, mas com deadlines não queria arriscar. 
A experiência me mostrou algumas vezes (e de forma dolorosa) que aprender uma tecnologia em curso de um projeto com um prazo limitado é bem ruim.

**Q: Onde estão os testes unitários e de integração?**
  
**R:** Sem desculpas aqui... A verdade é que uma documentação foi escrita em detrimento dos testes.
Testes serão adicionados mais tarde.
