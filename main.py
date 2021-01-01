from pyri import Pyri
from functions import *
from threading import Thread

def main():
  pyri = Pyri()
  main_thread = Thread(target = use_pyri, args=[pyri])
  secondary_thread = Thread(target = check_reminders, args=[pyri])
  main_thread.start()
  secondary_thread.start()

if __name__ == '__main__':
  main() 