# Web Semântica - Trabalho 1

Aplicação sobre livros (books)

## Prerequisits before running the project

- GraphDB
    - import books.csv using Tabular(OntoRefine)
    - on isbn13 column make Edit cells >> Transform and put the value: value.replace(".", "").replace("e+12", "0")
- Python3
    - s4api package

## Running this project

Inside the root folder run the command:

```
python3 manage.py runserver
```

Now, you can access:
- http://localhost:8000
- http://localhost:8000/booksguru/

## Udeful Links:

- Questions tagged [graphdb]  
  https://stackoverflow.com/questions/tagged/graphdb
- Importar dados CSV e converter para RDF | Loading Data Using OntoRefine  
  http://graphdb.ontotext.com/documentation/standard/loading-data-using-ontorefine.html
- GraphDB 8 OntoRefine tool  
  https://www.youtube.com/watch?v=YFb7hnZNLdQ
- Webinar GraphDB 9.1 Knowledge graphs with data provenance  
  https://www.youtube.com/watch?v=Vu1T0ozz6Og&list=PLSEiuYkICmDlpZSpWSsPjNAQhKh-raIiu
