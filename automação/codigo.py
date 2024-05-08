
import pyautogui
import time
#vamos usar a biblioteca time pra coloca tempo
pyautogui.PAUSE = 0.5
# coloca o como pra executar em o.5 segundos , pq por padrao ele executado tudo mais rapido possivel

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
# como o python quer fazer mais rapido possivel ele vai executando tudo ao mesmo tempo
pyautogui.write('https://orvengenharia.milldesk.com/login')
pyautogui.press('enter')
#aqui depois do enter quero que demorar a executar o proximo comando depois de 3 segundos
time.sleep(6)#ele vai pausa o codigo por 3 segundo
#aqui no click é personalizado = pyautogui.click(y=233,xy272, clicks = 2(clicar uma ou duas vezes, button = 'left ou right'))
#pyautogui.click(x=648, y=440)
#usa o tab pra pular um formulario
pyautogui.moveTo(x=116, y=189)

time.sleep(1)
pyautogui.click(x=108, y=180)

time.sleep(1)
pyautogui.click(x=587, y=562,clicks=2)

time.sleep(1)
pyautogui.click(x=829, y=235)
pyautogui.click(x=797, y=397)
pyautogui.write('procedimento concluido com sucesso ')
pyautogui.click(x=431, y=233)
pyautogui.click(x=1110, y=723)
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.click(x=1882, y=295)
pyautogui.scroll(-700) # barra de rolagem + vai rpa cima , - negativo pra baixo
#pyautogui.click(x=706, y=313)
#pyautogui.press('tab')
#pyautogui.press('tab')
#pyautogui.press('enter')

pyautogui.click(x=1829, y=476)
#pyautogui.click(x=1047, y=250)
#pyautogui.press('tab')
#pyautogui.press('tab')
#pyautogui.press('enter')

pyautogui.click(x=1638, y=969)


