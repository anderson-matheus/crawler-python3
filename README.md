# crawler-python3
O crawler-python3 é uma API que através de uma url de um site informado retorna uma resposta contendo um json com a quantidade de ocorrências de uma palavra informada.


## Requisitos
Pyton3.6

## Documentação da api
https://documenter.getpostman.com/view/1164449/RWTspF2C

## Instalação

git clone https://github.com/anderson-matheus/crawler-python3.git<br />
virtualenv venv<br />
source venv/bin/activate<br />
pip3 install -r requirements.txt<br />
hug -f app.py<br />


## Exemplo de retorno da api
###### Quando todas as urls possuírem um padrão válido será retornado uma resposta como essa

```
{
  "data":
    [
      {
        "url": "http://uol.com.br", //url em que foi pesquisa a palavra
        "searched_word": "para", //palavra desejada
        "occurrence": 102, //quantidade de vezes em que a palavra foi encontrada na url
        "success": true //retorna false se ocorrer algum erro na requisição
      },
      {
        "url": "ig.com.br",
        "searched_word": "para",
        "occurrence": 68,
        "success": true
      }
    ]
 }
```

###### Se alguma url possuir um padrão inválido será retornado uma resposta como essa

```
{
  "error": "Send valid urls"
}

```
