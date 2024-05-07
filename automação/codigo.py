
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
pyautogui.moveTo(x=92, y=150)

time.sleep(1)
pyautogui.click(x=92, y=150)

time.sleep(1)
pyautogui.click(x=467, y=442,clicks=2)

time.sleep(1)
pyautogui.click(x=501, y=185)
pyautogui.click(x=253, y=295)
pyautogui.write('impressora instala com sucesso na maquina do operador')
pyautogui.click(x=187, y=185)
pyautogui.click(x=594, y=571)
pyautogui.press('tab')
pyautogui.click(x=574, y=502)
pyautogui.click(x=1341, y=219)
pyautogui.scroll(-700) # barra de rolagem + vai rpa cima , - negativo pra baixo
pyautogui.click(x=706, y=313)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.click(x=1273, y=385)
pyautogui.click(x=1047, y=250)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

pyautogui.click(x=1152, y=665)


