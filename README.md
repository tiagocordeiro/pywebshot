# PyWebShot
## Crie capturas de tela de uma página web.

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/tiagocordeiro/pywebshot/blob/master/LICENSE)

### Importante
Você vai precisar do webdriver instalado no path do seu sistema.
Faça o download da versão equivalente ao seu navegador em `http://chromedriver.chromium.org/downloads`

    Obs: Você pode copiar o arquivo execultável para dentro da venv que será criado.


### Como rodar o projeto
* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode a aplicação.

```
git clone https://github.com/tiagocordeiro/pywebshot.git
cd pywebshot
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python pywebshot.py https://www.mulhergorila.com --metodo fullpage
```

