# Django Framework Básico - django1

>Desenvolvimento Web com Python e Django Framework.
> 
>>Projeto desenvolvido no curso da Geek University - Udemy [Programação Web com Python e Django Framework: Essencial](https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/)

## Ambiente de Desenvolvimento
Linux
## Desenvolvimento:
1. <span style="color:383E42"><b>Preparando ambiente</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    1. Criar repositório no github
    2. Criar README básico
    3. Criar e ativar ambiente virtual
        ```sh
        python3 -m venv myenv
        source venv/bin/activate
        ```
    4. Instalação pip - se necessario
        ```sh
        sudo apt update
        sudo apt install python3-pip
        pip3 --version
        ```
    5. Instalação Django
        ```sh
        sudo apt update
        pip3 install django
        ```
    6. Criação arquivo requirements
    Contém informaçẽos sobre todas as bibliotecas utilizadas no projeto. Para atualizar o arquivo, basta executar o comando novamente após instalar outras bibliotecas.
        ```sh
        pip freeze > requirements.txt
        ```
    </p>

    </details> 

    ---

2. <span style="color:383E42"><b>Criação de projeto django1 e app core</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    Criar app no mesmo diretório/pasta que está o projeto
    ```sh
    django-admin startproject django1 .
    django-admin startapp core
    ```
    Incluir app em Installed apps - settings
    ```python
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    ]
    ```
    Informar diretório de templates no settings
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

    Testar
    ```sh
    python3 manage.py runserver
    ```
    </p>

    </details> 

    ---
3. <span style="color:383E42"><b>Definindo timezone</b></span>
    Em `settings.py`
    ```python
    # Internationalization
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = 'pt-br'

    TIME_ZONE = 'America/Sao_Paulo'

    USE_I18N = True

    USE_TZ = True

    ```
4. <span style="color:383E42"><b>Primeiras views, templates e arquivo de rotas</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    1. Criação dos métodos em `views.py`
        ```python
        from django.shortcuts import render


        def index(request):
            return render(request, 'index.html')


        def contato(request):
            return render(request, 'contato.html')
        ```
    2. Adicionar arquivo `core/urls.py` em app core com as rotas
        Arquivo com as rotas referentes aos templates do app `core`
        ```python
        from django.urls import path

        from .views import index, contato

        urlpatterns = [
            path('', index),
            path('contato', contato)
        ]
        ```
    3. Configurar rota para aquivo de rotas  `core/urls.py` de app core
        Indica que a rota raiz aponta para o arquivo de `core.urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('core.urls'))
        ]
        ```
    4. Criar diretório `core/templates` em app core
    5. Criar templates
        `templates/index.html`
        ```html
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Django 1 - Index</title>
        </head>
        <body>
            <h1>Index</h1>
        </body>
        </html>
        ```
        `templates/contato.html`
        ```html
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Django 1 - Contato</title>
        </head>
        <body>
            <h1>Contato</h1>
        </body>
        </html>
        ```
    6. Testar
        ```sh
        python3 manage.py runserver
        ```

    </p>

    </details> 

    ---

## Meta
><span style="color:383E42"><b>Cristiano Mendonça Gueivara</b> </span>
>
>>[<img src="readmeImages/githubIcon.png">](https://github.com/sspectro "Meu perfil no github")
>
>><a href="https://linkedin.com/in/cristiano-m-gueivara/"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
>
>>[Minha Página Github - <img src="readmeImages/favicon.ico">](https://sspectro.github.io/#home "Minha Página no github")<br>



><span style="color:383E42"><b>Licença:</b> </span> Distribuído sobre a licença `Software Livre`. Veja Licença **[ISC](https://opensource.org/license/isc-license-txt/)**. para mais informações.