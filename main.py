from pyri import Pyri
import pystray
from pystray import MenuItem as item
from PIL import Image
from functions import *
from threading import Thread

def main():
  pyri = Pyri()
  main_thread = Thread(target = use_pyri, args=[pyri])
  secondary_thread = Thread(target = check_reminders, args=[pyri])
  main_thread.daemon = True
  secondary_thread.daemon = True
  main_thread.start()
  secondary_thread.start()
  image = Image.open('./assets/image/icon.png')
  menu = (item('Empezar', close), item('Salir', close))
  icon = pystray.Icon('Pyri', image, 'Pyri', menu)
  icon.run()

if __name__ == '__main__':
  main()