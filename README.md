# mananciais_rmsp
<br><br>

O projeto "mananciais_rmsp " tem como finalidade informar diarimanete o volume total de água armazenado na região metropolitana de São Paulo.

As informações são atualizadas diariamente https://mananciais.sabesp.com.br/Situacao

O código foi programado para rodar em dias úteis às 11:00h e a coleta da informação do volume total de água é realizada através de uma api e transmitida por recurso de áudio.
<br><br>

**INSTALAÇÃO**

Instalar o ambiente virtual:<br>
    $ python -m venv venv

Ativar o venv(Windows):<br>
    $ venv\Scripts\activate

Na sequência instalar o requirements:<br>
    $ pip install -r requirements.txt

<br><br>

**ESTRUTURA DO REPOSITÓRIO**
```
mananciais_rmsp/
├── src/
│   ├── app.py
│   ├── audio.py
|   └── sabesp.py
├── readme.md
└── requirements.txt
```

**requirements.txt**
```
    gTTS==2.2.3
    playsound==1.2.2
    Flask==2.0.2
    workadays==2021.6.10
```
