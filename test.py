from Tkinter import *
from memorpy import *

def getpid(process_name):
  import os
  return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if process_name in item.split()]

class Application:
  def __init__(self, master=None):
    self.fontePadrao = ("Arial", "10")
    self.primeiroContainer = Frame(master)
    self.primeiroContainer["pady"] = 10
    self.primeiroContainer.pack()

    self.segundoContainer = Frame(master)
    self.segundoContainer["padx"] = 20
    self.segundoContainer.pack()

    self.quartoContainer = Frame(master)
    self.quartoContainer["pady"] = 20
    self.quartoContainer.pack()

    self.titulo = Label(self.primeiroContainer, text="Buscar por strings")
    self.titulo["font"] = ("Arial", "10", "bold")
    self.titulo.pack()

    self.search = Entry(self.segundoContainer)
    self.search["width"] = 30
    self.search["font"] = self.fontePadrao
    self.search.pack(side=LEFT)

    self.autenticar = Button(self.quartoContainer)
    self.autenticar["text"] = "Buscar"
    self.autenticar["font"] = ("Calibri", "10")
    self.autenticar["width"] = 12
    self.autenticar["command"] = self.search_hacks
    self.autenticar.pack()

    self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
    self.mensagem.pack()

  def search_hacks(self):
    search = self.search.get()

    mw = MemWorker(pid=int(getpid('explorer.exe')[0]))

    address_list = [x for x in mw.umem_search(search)]
    self.mensagem["text"] = str(len(address_list)) + " resultados encontrados."

    size = len(address_list)
    
    if size > 0:
      self.mensagem["text"] += ("\n")
      while (size > 0):
        for address in address_list:
          try:
            self.mensagem["text"] += str("\n" + address.read().decode("utf-16-le"))
            del address_list[address]
            size =- 1
          except:
            del address_list[address_list.index(address)]
            size =- 1
  
root = Tk()
Application(root)
root.mainloop()