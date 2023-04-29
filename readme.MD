# Universidade Federal Fluminense - UFF
## Autor : Márcio Garrido
### marciogarrido@id.uff.br

## Versao AWS

[![N|Solid](https://upload.wikimedia.org/wikipedia/pt/thumb/4/47/UFF_bras%C3%A3o.png/200px-UFF_bras%C3%A3o.png)](http://www.ppgeet.uff.br/site/)

## API para consumo de dados de microntroladores ESP - Estacao Completa
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

### Documentação Django
https://docs.djangoproject.com/en/4.0/

### Documentação Python

https://www.python.org/doc/

Instale a versão atualizada do Python na sua máquina caso nao tenha.
## Instalando Python

        pip install Python 3.7.4

## Criando Ambientes de desenvolvimento
Para garantirmos que a versão do seu projeto não conflite com outros apps, o recomendado é criar ambientes isolados.
Para criar, há a parte "Creating virtual environments". Para organizar o projeto, crie um diretório e em sequencia vá para o local criado.


        mkdir -p ~/Users/marciogarrido/api-esp-2-aws
        cd ~/Users/marciogarrido/api-esp-2-aws

Com local já identificado, o próximo passo é virtualizar o ambiente de desenvolimento venv

        python3 -m venv ~/eb-virt

No decorrer da aplicação, editamos e alteramos o código usando o Visual Studio Code, mas outros editores como PyCharm, Sublime Text ou Atom também são eficientes. 

Abrindo-o, acessamos a pasta "aplicacao > venv" e abrimos o terminal com "Command + J". Na janela "Terminal", precisamos carregar o ambiente virtual digitando pwd para copiar e colar o caminho após escrever source na linha seguinte. 

        source ~/eb-virt/bin/activate

No meu caso, o retorno do comando pwd foi o meu perfil, que vai variar de acordo com as suas credenciais. Com seu perfil identificado, o próximo passo é criar de fato o ambiente. Escrevemos /venv/bin/activate na sequência do caminho para acessar a pasta e inicializar com "Enter". Temos confirmação quando aparece (venv) antes do diretório.

         source /Users/marciogarrido/API-ESP/venv/bin/activate

Para validar se o processo foi concluído com sucesso, seu terminal agora deve ter o nome venv no início do texto como abaixo:

        (eb-virt) (base) [api-esp-2-aws]  

# Instalando as dependências 
Abra seu terminal e digite a instrução abaixo:

        pip install - r requirements.txt

Para verificação se o Djanjo e suas dependências foram instaladas com exito, execute o comando abaixo para ver as versões do seu ambiente

        pip freeze
    
O resultado deve retornar os móodulos abaixo:

        asgiref==3.5.2
        Django==3.2.16
        django-filter==22.1
        djangorestframework==3.14.0
        importlib-metadata==5.1.0
        Markdown==3.4.1
        pytz==2022.6
        sqlparse==0.4.3
        zipp==3.11.0

# Instalando suporte a banco de PostgreSQL

O banco de dados utilizado nesse projeto é o banco relacional PostgreSQL

        pip install psycopg2

## Criar arquivo de dependencias 
Antes de subir o projeto, verifique as dependências e gere o arquivo de instalacão


        pip3 freeze > requirements.txt

## Definindo respositório remoto

        eb init -p python-3.8 EB-repo-api

### onde o nome do repositório é "EB-repo-api" usando a versão do Python 3

## Crie um ambiente e implante o aplicativo nele com eb create.


## Salvar e subir

        
## Atualizar tabelas 

        python manage.py migrate

## Criar super usuários

        python manage.py createsuperuser