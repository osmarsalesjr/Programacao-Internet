#coding: utf-8
from os import system as sys
from bs4 import BeautifulSoup
import requests

def main():
    op = ""
    while True:
        op = str(input(" 1 - GET url info\n 2 - GET image by url\n 3 - get ALL links in URL\n q - quit -> "))
     
        if op == "1":
            get_url(str(input("url alvo -> ")))
        elif op == "2":
            get_image(str(input("url alvo -> ")))
        elif op == "3":
            get_links(str(input("url alvo -> ")))
        elif op.upper() == "q":
            break
        else:
            print("opção inválida")
            
def get_url(url):
    r = requests.get(url) 
    print ("    STATUS:\ncodigo requisição:"+str((r.status_code))+" | versão HTTP: "+str(r.raw.version)+" | tamanho corpo:"+str(len(r.content)))
    print ("\n CABEÇALHOS:\n\n" + str(r.headers))
    print ("\n CORPO: \n\n"+str(r.content))

def get_image(url):
    nome_arquivo = url.split('/').pop()
    print (nome_arquivo)
    command = "curl --output "+nome_arquivo+" "+url
    sys(command)
    print("feito!")
def get_links(url):
    page = requests.get(url).content
    soup = BeautifulSoup(page)
    links = soup.find_all('a')
       
    saida = ("      LINKS ENCONTRADOS EM \n   %s:\n\n"%url) 
    counter = 1
    for tag in links:
        link = tag.get('href',None)
        if link is not None and len(link) > 3:
            saida+= ("%d - %s\n"%(counter,link))
            counter += 1
    print(saida)
    sys ('echo "'+saida+'" >> '+url.split("/").pop()+'.txt')
    print("feito!")
    
if __name__=="__main__":
    main()