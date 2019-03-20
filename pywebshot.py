# stdlib imports
import datetime
import re
# third-party imports
import click
from selenium import webdriver

def save_screenshot(url:str, width:int, height:int, metodo:str, filename:str):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    # start chrome browser
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(width, height)
    browser.get(url)

    if metodo == 'fullpage':
        scroll_height = browser.execute_script('return document.body.parentNode.scrollHeight')
        browser.set_window_size(width, scroll_height)
    elif metodo == 'window':
        pass
    else:
        click.echo("Os métodos permitidos são 'window' e 'fullpage'")

    print(browser.current_url)
    browser.save_screenshot(filename)
    browser.fullscreen_window
    print("Salvo")
    browser.quit()

def filename_gen(url:str):
    now = datetime.datetime.now()
    date = now.strftime('%Y%m%d')
    time = now.strftime('%H%M%S')
    clean_url = re.split('://|://www.', url)[1].replace('.','-')

    return f'screenshot-{clean_url}-{date}-{time}.png'


@click.command()
@click.option('--metodo', default='window', help='window or fullpage')
@click.option('--width', default=1280, help='Largura da tela. Padrão 1280')
@click.option('--height', default=800, help='Altura da tela. Padrão 800')
@click.argument('url')
def main(url:str, width:int, height:int, metodo:str):
    url = url
    filename = filename_gen(url)

    save_screenshot(url, width, height, metodo, filename)
 
    return


if __name__ == '__main__':
    main()
