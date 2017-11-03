#coding: utf-8
from os import system as sys
import requests
import re

def main():
    op = ""
    while True:
        op = str(input(" 1 - GET url\n 2 - GET image by url\n 3 - get ALL links in URL\n q - quit -> "))
     
        if op == "1":
            get_url(str(input("url alvo -> ")))
        elif op == "2":
            get_image(str(input("url alvo -> ")))
        elif op == "3":
            get_links(str(input("url alvo -> ")))
        elif op == "q":
            break
        else:
            print("opção inválida")
            
        
       
        
def get_url(url):
    r = requests.get(url) 
    print ("  status: \ncodigo requisição:"+str((r.status_code))+" | versão HTTP: "+str(r.raw.version)+" | corpo:\n"+str(r.content))
    print ("\n cabeçalhos:\n" + str(r.headers))
    print ("\n tamanho do corpo:\n"+str(len(r.content)))


def get_image(url):
    nome_arquivo = url.split('/').pop()
    print (nome_arquivo)
    command = "curl --output "+nome_arquivo+" "+url
    sys(command) 
    
def get_links(url):
    r = requests.get(url)
    corpo = str(r.content)
    
    regex = "[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    
    
    print(corpo)
    
    print(re.sub(regex,"",corpo))

if __name__=="__main__":
    main()