# Web Semântica - Trabalho 1

Aplicação sobre livros (books)

## Pre-requisits before running the project

- GraphDB
    - Create a repository named "booksguru"
    - import books.csv using Tabular(OntoRefine)
    - on isbn13 column make Edit cells >> Transform and put the value: value.replace(".", "").replace("e+12", "0")
- Python3
    - s4api package

## Running this project

Inside the root folder run the command:

```
python3 manage.py runserver
```

Now, you can access one of these links:
- http://localhost:8000
- http://localhost:8000/booksguru/

## Useful Links and References:

- Questions tagged [graphdb]  
  https://stackoverflow.com/questions/tagged/graphdb
- Importar dados CSV e converter para RDF | Loading Data Using OntoRefine  
  http://graphdb.ontotext.com/documentation/standard/loading-data-using-ontorefine.html
- GraphDB 8 OntoRefine tool  
  https://www.youtube.com/watch?v=YFb7hnZNLdQ
- Webinar GraphDB 9.1 Knowledge graphs with data provenance  
  https://www.youtube.com/watch?v=Vu1T0ozz6Og&list=PLSEiuYkICmDlpZSpWSsPjNAQhKh-raIiu
- Built-in template tags and filters
  https://docs.djangoproject.com/en/3.0/ref/templates/builtins/
- Django Authentication Video Tutorial
  https://github.com/sibtc/django-auth-tutorial-example
- Django - always getting False in form.is_valid()
  https://groups.google.com/forum/#!topic/django-users/z5EjU2-RgtU

## New Implementations for "Recurso" Epoc

- Added route do "/" for better user experience
- Improved the graphical style of the website.
- Working with models, forms, views, urls and templates
- Added admin.sites
- Created system to login, logout and register users
- Welcome message to the user
- Add comment for a book, only for logged in users
- When load a book details page, the system get all comments tho actual book, from BD

Default user passwords: userpass2020
