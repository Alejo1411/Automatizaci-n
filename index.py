import time  # Importar la libreria time
from selenium import webdriver  # Importar la biblioteca webdriver
from selenium.webdriver.common.by import By  # Importar la biblioteca By
from selenium.webdriver.common.keys import Keys  # Importar la biblioteca Keys
from selenium.webdriver.chrome.service import Service  # Importar la biblioteca Service
from selenium.webdriver.support.ui import WebDriverWait  # Importar la biblioteca WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Importar la biblioteca expected_conditions

def obtener_xpath(indice):
    return f'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[{indice}]/div/div/div[2]/div/div[1]/div/p[1]/span[2]'

# Configurar el webdriver de Chrome

servicio = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=servicio)
bot.get("https://www.viajesexito.com")

# Navegar a la sección de "Paquetes"

paquetes = bot.find_element(By.XPATH, "/html/body/form/header/div[2]/div/div/nav/div[4]")
paquetes.click()
time.sleep(1)

# Seleccionar el origen del vuelo

origen_vuelo = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input")
origen_vuelo.click() 
time.sleep(1) 

# Ingresar la ubicación de origen del vuelo

origen_vuelo_select = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input")
origen_vuelo_select.send_keys("Jose María Cordova") # Ingresar la ubicación de origen del vuelo
origen_vuelo_select.send_keys(Keys.ENTER)

# Seleccionar el destino del vuelo

destino_vuelo = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input")
destino_vuelo.click() # Clickea
time.sleep(1)

# Ingresar la ubicación de destino del vuelo

destino_vuelo_select = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input")
destino_vuelo_select.send_keys("Punta Cana") # Ingresar la ubicación de destino del vuelo
destino_vuelo_select.send_keys(Keys.ENTER)
time.sleep(1)

# Seleccionar el input para la fecha del vuelo

fecha = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input")
fecha.click()
time.sleep(1)

# Ingresar el rango de fechas del vuelo

fecha_inicio = bot.find_element(By.XPATH, "/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[4]/div[4]/div[2]/div[1]")
fecha_inicio.click()
fecha_fin = bot.find_element(By.XPATH, "/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[7]/div[2]/div[1]")
fecha_fin.click()
time.sleep(1)

# Aceptar la fecha de vuelo seleccionada

aceptar_fecha_vuelo = bot.find_element(By.XPATH, "/html/body/div[11]/div[2]/div[2]/div[2]/button[2]")
aceptar_fecha_vuelo.click()
time.sleep(1)

# Seleccionar información del vuelo

opciones_vuelo = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p")
opciones_vuelo.click()
time.sleep(1)

# Agregar información del vuelo

opciones_nuevas = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]")
opciones_nuevas.click() # Hacer clic en el botón de agregar
time.sleep(1)

# Aceptar la información del vuelo

opciones_aceptar = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button")
opciones_aceptar.click() # Hacer clic en el botón de aceptar
time.sleep(1)

# Iniciar la búsqueda de vuelos

buscar = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a")
buscar.click() # Hacer clic en el botón de búsqueda
time.sleep(1)

# Cambiar a la nueva ventana abierta
ventana_nueva = bot.window_handles[1] # Obtener la nueva ventana
bot.switch_to.window(ventana_nueva) # Cambiar a la nueva ventana

# El bot esperará 40 segundos para que no saque error al cargar la pagina
WebDriverWait(bot, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]'))) 
time.sleep(5) # para que no unda click en cualquier lado

elementos_precios = bot.find_elements(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div')

# Iterar sobre los primeros 10 precios de los paquetes
for i, elemento in enumerate(elementos_precios, start=1):
    xpath_paquete = obtener_xpath(i)  # Obtener el XPath para el paquete actual
    precio_paquete = bot.find_element(By.XPATH, xpath_paquete)  # Obtener el elemento del precio
    print(f"Precio del paquete {i}: {precio_paquete.text}")  # Imprimir el precio del paquete

# Acceder a las opciones avanzadas
avanzadas = bot.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a")
avanzadas.click() # Hacer clic en el botón de opciones avanzadas
time.sleep(1)

# Seleccionar la aerolínea
aerolinea = bot.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input")
aerolinea.click()
aerolinea.send_keys("LATAM Airlines (LA)") # Se ingresa el nombre de la aerolínea
time.sleep(1)
aerolinea.send_keys(Keys.ENTER) # Se acepta el nombre de la aerolínea
time.sleep(1)

# Aceptar la aerolínea seleccionada
aerolinea_aceptar = bot.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input")
aerolinea_aceptar.click() # Hacer clic en el botón de aceptar
time.sleep(1)

# El bot esperará 40 segundos a que cargue la pagina para que no saque error
WebDriverWait(bot, 40).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')))

# Acceder a la sección de "Contáctenos"
contactanos = bot.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p/a")
contactanos.click()
time.sleep(2)

#programa finalizado
print("El programa ha finalizado")
bot.quit()