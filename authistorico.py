from selenium.webdriver.common.by import By
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import time
import tabula
import os
from selenium.webdriver.firefox.options import Options

############### dando erroooOO""""$#%¨&*()@@@@@@@#$###########
matricula = input("Digite a matricula: ")

senha = input("Digite a senha: ")

#options = Options()
#options.add_argument('-headless')
nav = webdriver.Firefox()


'''
 #testando modulo de gerenciamento#
service = ChromeService(executable_pathChromeDriverManager().install())
driver = webdriver.Chrome(serice=service)
'''

nav.get('https://uespi.br/')

nav.find_element(By.XPATH,'/html/body/div[1]/div[2]/section/div/div/div/div/div/div/section[1]/div/div/div/div[1]/div/div/div[1]/ul/li[4]/a').click()

nav.find_element(By.XPATH,'/html/body/div[1]/div[2]/section/div/div/div/div/div/div/section[1]/div/div/div/div[1]/div/div/div[1]/ul/li[4]/ul/li[1]/a').click()

nav.find_element(By.XPATH,'//*[@id="inputMatricula"]').send_keys(matricula)

nav.find_element(By.XPATH,'//*[@id="inputPassword"]').send_keys(senha)

nav.find_element(By.XPATH,'/html/body/div[4]/form/table/tbody/tr[4]/td/input').click()

nav.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/a').click()

#nav.find_element(By.XPATH,'/html/body/div[2]/nav/div/div[2]/ul[1]/li[3]/a').click()

elemento = nav.find_element(By.XPATH,'/html/body/div[2]/nav/div/div[2]/ul[1]/li[4]/a')
nav.execute_script("arguments[0].click();", elemento)

'''
testando scroll falho..
curric = nav.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[1]/div[2]/div[2]/form/input[3]')

rolada(nav)\
    .rolar(curric)\
    .perform()
'''
#time.sleep(3)
elemento1 = nav.find_element(By.XPATH,'/html/body/div[2]/nav/div/div[2]/ul[1]/li[4]/ul/li[1]/a')
nav.execute_script("arguments[0].click();", elemento1)

time.sleep(3)
nav.find_element(By.XPATH,'/html/body/div[5]/div/div/p[2]/a').click()

#nav.quit()
#baixar arquivo dando erro
#time.sleep(3)
#nav.find_element(By.XPATH, '//*[@id="download"]').click()

'''
#mostrar link no terminal n funciona

link = nav.current_url

print(f"Curriculo matricula: {link}")
'''

'''
testando explorar arquivos na maquina
arquivos = os.listdir("/home/rmg/Downloads")

os.rename

'''
#path_dir = "/home/rmg/Downloads/historico.pdf"
#os.startfile(path_dir)

#implementação de leitura e transcrição do pdf historico em arquivo.txt usando tabula-py

#lista_tabel = tabula.read_pdf("historico.pdf", pages="all")

#for i in lista_tabel:
    #print(i)

'''
g = open("notas.txt", "w")
g.write(str(lista_tabel[0]))
g.close()
'''

