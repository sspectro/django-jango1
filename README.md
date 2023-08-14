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

    - Criar repositório no github
    - Criar README básico
    - Criar e ativar ambiente virtual
        ```sh
        python3 -m venv myenv
        source venv/bin/activate
        ```
    - Instalação pip - se necessario
        ```sh
        sudo apt update
        sudo apt install python3-pip
        pip3 --version
        ```
    - Instalação Django
        ```sh
        sudo apt update
        pip3 install django
        ```
    - Criação arquivo requirements
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
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    Em `settings.py`
    ```python
    # Internationalization
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = 'pt-br'

    TIME_ZONE = 'America/Sao_Paulo'

    USE_I18N = True

    USE_TZ = True

    ```

    </p>

    </details> 

    ---
4. <span style="color:383E42"><b>Primeiras views, templates e arquivo de rotas</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criação dos métodos em `views.py`
        ```python
        from django.shortcuts import render


        def index(request):
            return render(request, 'index.html')


        def contato(request):
            return render(request, 'contato.html')
        ```
    - Adicionar arquivo `core/urls.py` em app core com as rotas
        Arquivo com as rotas referentes aos templates do app `core`
        ```python
        from django.urls import path

        from .views import index, contato

        urlpatterns = [
            path('', index),
            path('contato', contato)
        ]
        ```
    - Configurar rota para aquivo de rotas  `core/urls.py` de app core
        Indica que a rota raiz aponta para o arquivo de `core.urls.py`
        ```python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('core.urls'))
        ]
        ```
    - Criar diretório `core/templates` em app core
    - Criar templates
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
    - Testar
        ```sh
        python3 manage.py runserver
        ```

    </p>

    </details> 

    ---

5. <span style="color:383E42"><b>Passando parâmetro para o template `index.html`</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    Em `views.py`
    ```python
    def index(request):
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Programação Web com Django Framework'
    }
    return render(request, 'index.html',context)
    ```

    Em `index.html`
    ```html
    <body>
    <h1>Index</h1>
    <h2>{{curso}}</h2>
    <p>{{outro}}</p>
    </body>
    ```
    </p>

    </details> 

    ---

6. <span style="color:383E42"><b>Models - Primeiros modelos</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criar modelo/classe `Produto` e `Cliente` em `core/models`
        ```python
        from django.db import models

        class Produto(models.Model):
            nome = models.CharField('Nome', max_length=100)
            preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
            estoque = models.IntegerField('Quantidade em Estoque')

        class Cliente(models.Model):
            nome = models.CharField('Nome', max_length=100)
            sobrenome = models.CharField('Sobrenome', max_length=100)
            email = models.EmailField('Email', max_length=100)
        ```

    - Gerando migrations
        ```sh
        python3 manage.py makemigrations
        ```

    - Executando as migrations - Cria as tabelas no banco de dados
        ```sh
        python3 manage.py migrate
        ```

    - Testar
        ```sh
        python3 manage.py runserver
        ```
    </p>

    </details> 

    ---

7. <span style="color:383E42"><b>Área administrativa</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criando super usuário
        Podemos criar vários super usuários, caso precise
        ```sh
        python3 manage.py createsuperuser
        ```
    
    - Incluir modelos ao `core/admin.py`
        Para que seja exibido no painel admin da aplicação
        ```python
        from django.contrib import admin

        from .models import Produto, Cliente

        admin.site.register(Produto)
        admin.site.register(Cliente)
        ```

    - Inserir alguns produtos via painel admin
        Usar usuário e senha criado em passo anterior `http://127.0.0.1:8000/admin/`
    <br>

    - Definir o método `__str__` para os modelos criados
        Representação do objeto em um formato de string - Neste caso retorna apenas o valor da variável nome e no outro nome e sobrenome
        ```python
        from django.db import models

        class Produto(models.Model):
            nome = models.CharField('Nome', max_length=100)
            preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
            estoque = models.IntegerField('Quantidade em Estoque')

            def __str__(self) -> str:
                return self.nome

        class Cliente(models.Model):
            nome = models.CharField('Nome', max_length=100)
            sobrenome = models.CharField('Sobrenome', max_length=100)
            email = models.EmailField('Email', max_length=100)
            
            def __str__(self) -> str:
                return f'{self.nome} {self.sobrenome}'
        ```
    - Testar: Verificar resultado via painel admin
    <br>

    - Criar classes em core/admin.py que extendem modelAdmin
        Permite configurar exibição no painel admin, como quais colunas deseja exibir
        ```python
        from django.contrib import admin

        from .models import Produto, Cliente

        class ProdutoAdmin(admin.ModelAdmin):
            list_display = ('nome', 'preco', 'estoque')

        class ClienteAdmin(admin.ModelAdmin):
            list_display = ('nome', 'sobrenome', 'email')

        admin.site.register(Produto, ProdutoAdmin)
        admin.site.register(Cliente, ClienteAdmin)
        ```
    
    - Testar
    </p>

    </details> 

    ---

8. <span style="color:383E42"><b>Django Shell e Python Console</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Detalhes sobre o comando `manage.py`
        Listagem de comandos disponíveis
        ```sh
        python manage.py
        ```
    - Detalhes sobre o comando `manage.py` - `help`
        ```sh
        python manage.py help makemigrations
        ```
    - Console Python
        ```sh
        python manage.py shell
        ```
        Manipula objeto
        ```sh
        from core.models import Produto

        #Adicionar produto
        produto = Produto(nome="Atari 2600", preco=199,67, estoque=100)
        produto.save()

        # Visualizar propriedades e métdos do objeto
        dir(produto)
        produto.id
        ```
    </p>

    </details>

    ---

9. <span style="color:383E42"><b>Dados do banco de dados no Template</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Incluir rota para página/template `core/templates/produto.html`.
    ```python
    # Inclui nome para rota - nome que será usado ao criar url na página - pode gerar erro, caso não defina o parâmetro name
    path('produto/<int:pk>', produto, name='produto'), 
    ```

    - Cria lista de produtos e inclui no contexto para enviar ao template
        ```python
        from django.shortcuts import render
        from core.models import Produto


        def index(request):
            produtos = Produto.objects.all()
            context = {
                'curso': 'Programação Web com Django Framework',
                'outro': 'Programação Web com Django Framework',
                'produtos': produtos
            }
            return render(request, 'index.html',context)
        ```

    - Tabela para exibir lista de produtos no `core/templates/index.html`
        Cria `url` para produto com base no nome definido no arquivo de rotas `urls.py` com parâmetro id
        ```html
        <table>
        <thead>
            <tr>
                <th>Produto</th>
                <th>Preço</th>
            </tr>
        </thead>
        <tbody>
        {% for produto in produtos %}
            <tr>
                <td><a href="{% url 'produto' produto.id %}">{{ produto.nome }}</a></td>
                <td>{{ produto.preco }}</td>
            </tr>
        {% endfor %}
        </tbody>
        </table>
        ```

    - Criar template `core/templates/produto.html`
        Inclui url para retorno `core/templates/index.html`
        ```html
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Produto</title>
        </head>
        <body>

            <h1>Produto</h1>

            <table>
                <thead>
                    <tr>
                        <th>Produto</th>
                        <th>Preço</th>
                        <th>Estoque</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><a href="{% url 'index' %}">{{ produto.nome }}</a></td>
                        <td>{{ produto.preco }}</td>
                        <td>{{ produto.estoque }}</td>
                    </tr>
                </tbody>
            </table>

        </body>
        </html>
        ```

    - Criar método `produto` em `core/views`
        Retorna o produto para o template `core/templates/produto.html` com base no id passado como parâmetro
        ```python
        def produto(request, pk):
        prod = Produto.objects.get(id=pk)

        context = {
            'produto': prod
        }
        return render(request, 'produto.html', context)
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