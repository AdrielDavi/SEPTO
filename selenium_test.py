import pyautogui
from selenium.webdriver import Chrome
import os

caminho_imagem = os.path.abspath('ex3.png')
driver = Chrome()
driver.maximize_window()

driver.get('https://images.google.com/')



botao_pesquisa_imagem = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[4]')
botao_pesquisa_imagem.click()
driver.implicitly_wait(2)
abrir_pasta = driver.find_element('xpath', '//*[@id="ow6"]/div[3]/c-wiz/div[2]/div/div[3]/div[2]/div/div[2]/span')
abrir_pasta.click()
pyautogui.sleep(2)
pyautogui.write(caminho_imagem)
pyautogui.press('enter')
driver.implicitly_wait(30)
text = driver.find_element('xpath', '//*[@id="ucj-4"]/span[1]')
text.click()
selecionar_todo_texto = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/div/div/div/div[1]/div/div/div[2]/div/button/span')
selecionar_todo_texto.click()
ouvir = driver.find_element('xpath','//*[@id="ucc-3"]/span[1]')
ouvir.click()

input()
