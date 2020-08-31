#!/usr/bin/env python3
"""
CCTOOLS - Multi Tools of Carding, EDUCATIONAL PURPOSES.
Copyright (C) 2020  Lanniscaf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: Telegram @lanniscaf
         Email: chichipapa3344@gmail.com
"""

from time   import sleep
from bs4    import BeautifulSoup
from random import randint
import requests, json, re, time, os, sys, datetime

ccgenlogo="  ____ ____ ____                           _\n / ___/ ___/ ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __\n| |  | |  | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|\n| |__| |__| |_| |  __/ | | |  __/ | | (_| | || (_) | |\n \____\____\____|\___|_| |_|\___|_|  \__,_|\__\___/|_|\n"
#---------------------------------------------------
#---------------------------------------------------
#EXTRAPOLADOR
class extrapola:
  def __init__(self,bin1,bin2):
    self.bin1=bin1
    self.bin2=bin2
    self.ccout=''

  #Extrapolacion por similitud
  def simpleE(self):
    if(len(self.bin1)!=16 or len(self.bin2)!=16):
      return 'FORMATO INCORRECTO P SimpleE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      if(self.bin1[:6] != self.bin2[:6]):
        return 'FORMATO INCORRECTO P SimpleE'
      for letter in range(len(self.bin1)):
        if(self.bin1[letter] == self.bin2[letter]):
          self.ccout += self.bin1[letter]
        else:
          self.ccout +='x'
    else:
      self.ccout = False
    return self.ccout
    self.ccout = ''
  #Extrapolacion por lugar Banco
  def compleE(self):
    if(not len(self.bin1)==16 or not len(self.bin2)==16):
      return 'FORMATO INCORRECTO P CompleE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      if(self.bin1[:6] != self.bin2[:6]):
        return 'FORMATO INCORRECTO P CompleE'
      cuerpo1 = self.bin1[:8]
      cuerpo2 = self.bin2[8:]
      #multiplica
      ccmult=''
      for num in range(len(cuerpo1)):
        ccmult = ccmult + str(int(cuerpo1[num])*int(cuerpo2[num]))
      #extragenerado
      cuerpo1+=ccmult[:8]
      #comparacion
      for letter in range(len(self.bin1)):
        if(self.bin1[letter] == cuerpo1[letter]):
          self.ccout += self.bin1[letter]
        else:
          self.ccout +='x'
      if(self.ccout[15:]=='x'):
        self.ccout = self.ccout[:15]+'1'
      return(self.ccout)
      self.ccout = ''
  #Extrapolacion Avanzada
  def avanE(self):
    if(not len(self.bin1)==16 or not len(self.bin2)==16):
      return 'FORMATO INCORRECTO P AvanE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      if(self.bin1[6:8] != self.bin2[6:8]):
        return 'FORMATO INCORRECTO P AvanE'
      elif(self.bin1[:6] != self.bin2[:6]):
        return 'FORMATO INCORRECTO P AvanE'
      cuerpo1 = self.bin1[:8]
      mul1 = self.bin1[9:11]
      mul2 = self.bin2[9:11]
      #se suman
      mul1= str(int(mul1[0:1]) + int(mul1[1:]))
      mul2= str(int(mul2[0:1]) + int(mul2[1:]))
      #Re suman dobles
      while True:
        if(len(mul1) >= 2):
          mul1= str(int(mul1[0:1]) + int(mul1[1:]))
          continue
        elif(len(mul2) >= 2):
          mul2= str(int(mul2[0:1]) + int(mul2[1:]))
        else:
          break
      #Division
      mul1 = str(int(mul1) / 2)
      mul2 = str(int(mul2) / 2)
      #Multiplicacion
      mul1 = str(round(float(mul1)*5,))
      mul2 = str(round(float(mul2)*5,))
      #suma
      cuerpo1+=str(int(mul1)+int(mul2))
      self.ccout= cuerpo1
      for i in range(6):
        self.ccout+='x'
      return(self.ccout)
      self.ccout = ''
        
    else:
      return 'Invalid Format'
  #Extrapolacion 343
  def grupE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout = self.bin1[:6]+self.bin1[6:7]+'x'+self.bin1[8:9]+self.bin1[9:10]+'xx'+self.bin1[12:13]+self.bin1[13:14]+'x'+self.bin1[15:]
      value=self.ccout
      return value
      

    else:
      return 'Invalid Format'
  #Extrapolacion 5
  def fivE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:11]
      for i in range(5):
        self.ccout= self.ccout +"x"
      return(self.ccout)
    else:
      return "Invalid Format"
  #Extrap X
  def xiE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:6]+'xxxx'+self.bin1[10:14]+'xx'
      return(self.ccout)
    else:
      return "Invalid Format"
  #Extrapolacion X
  def xiiE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:10]
      for i in range(6):
        self.ccout= self.ccout +"x"
      return(self.ccout)
    else:
      return "Invalid Format"
  #Extrapolacion X
  def xiiiE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:7]+'x'+self.bin1[8:9]+'xxx'+self.bin1[12:14]+'xx'
      return(self.ccout)
    else:
      return "Invalid Format"
  #Extrapolacion X
  def xiiiiE(self):
    if(not len(self.bin1)==16):
      return 'Invalid Format grupE'
    if(self.bin1[:1] != "3" or self.bin2[:1] != "3"):
      self.ccout=self.bin1[:7]+'xx'+self.bin1[10:11]+'x'+self.bin1[12:13]+'xxxx'
      return(self.ccout)
    else:
      return "Invalid Format"
def extrapolar(bin1,bin2=' '):
    try:
      message='\n'
      if(bin2!= ' ' and bin2!='' and bin2!=False):
        message+= 'Similitud -->' + extrapola(bin1,bin2).simpleE() +'\n'
        message+= 'Banco     -->' + extrapola(bin1,bin2).compleE() +'\n'
        message+= 'Avan      -->' + extrapola(bin1,bin2).avanE() +'\n'
      message+= 'XB1       -->' + extrapola(bin1,bin2).grupE() +'\n'
      message+= 'XB2       -->' + extrapola(bin1,bin2).fivE() +'\n'  
      message+= 'XB3       -->' + extrapola(bin1,bin2).xiiiiE() + "\n"
      message+= 'XB4       -->' + extrapola(bin1,bin2).xiiiE() + "\n"
      message+= 'XB5       -->' + extrapola(bin1,bin2).xiE() + '\n'
      message+= 'XB6       -->' + extrapola(bin1,bin2).xiiE() + "\n"
      return(message)
    except:
      return('Error: BAD FORMAT')

#---------------------------------------------------
#---------------------------------------------------
#BINCHECK
def alternateS(bino):
  if(len(str(bino))<6):
    return 'Invalid Bin'
  if(len(str(bino))>6):
    bino=bino[:6]
  url="http://www.bins.su/"
  data={
    "action":"searchbins",
    "bins":bino,
    "bank":"",
    "country":""
  }
  try:
      page = requests.post(url, data=data)
      page.raise_for_status()
  except:
    return 'Server Error. Try again'
  page =BeautifulSoup(page.content,"html.parser")

  result=page.find("div", attrs={"id":"result"}).table
  try:
    result=result.find_all("tr")
  except:
    #error no existe
    return 'Invalid Bin'
  try:
    hed=result[0]
    hed=hed.find_all("td")
    dat=result[1]
    dat=dat.find_all("td")
    cabeceras=[]
    datos=[]
    for i in range(len(hed)):
        cabeceras.append(hed[i].text)
    for i in range(len(dat)):
        datos.append(dat[i].text)
    date='Valid '
    for i in range(len(datos)):
      if(datos[i] != '' and datos[i]!=' '):
        date+= '{}: {}\n'.format(cabeceras[i],datos[i])
      else:
        date+= '{}: {}\n'.format(cabeceras[i],'None')
    return date
  except:
    return 'Error desconocido'
def checkear(bin):
    bin= str(bin)
    try:
        bin= bin.replace("x","")
        bin= bin.replace("X","")
        bin= bin.split("|")[0]
    except:
        pass
    bin = str(re.sub('([a-zA-Z]){1,}', '', bin))
    lenLuhn=len(str(bin))
    sinccheck=bin[:16]
    bin = str(bin)
    bin = re.sub('([a-zA-Z]){1,}', '', bin)
    try:
        unks = 0
        url='https://lookup.binlist.net/'+str(bin)
        try:
            page = requests.get(url)
            page.raise_for_status()
        except:
            return alternateS(bin)
        
        
        page= page.content.decode()
        dic = json.loads(page)
        try:
            luhn = dic['number']['luhn']
        except:
            luhn = 'Unk'
            unks+=1
        try:
            luhnLen = dic['number']['length']
        except:
            luhnLen = 'Unk'
            unks+=1
       
        brand = dic['scheme']
        
        try:
            brand2 = dic["brand"]
        except:
            brand2 = ''
            unks+=1
        try:
            tipe = dic["type"]
        except:
            tipe = 'Unk'
            unks+=1
        try:
            prepaid = dic["prepaid"]
        except:
            prepaid = 'Unk'
        country= dic["country"]["name"]
        try:
            emoji = dic["country"]["emoji"]
        except:
            emoji = ""
        try:
            bank = dic["bank"]['name']
        except:
            bank = 'Unk'
            unks+=1
        try:
            urlBank = dic["bank"]["url"]
        except:
            urlBank = 'Unk'
            unks+=1
        try:
            phoneBank = dic["bank"]["phone"]
        except:
            phoneBank = 'Unk'
            unks+=1
        try:
            city = dic["bank"]["city"]
        except:
            city = 'Unk'
            unks+=1
        datosS = """Valid Bin:{}
Brand: {} - {}
Type: {}
Prepaid: {}
Country: {}
Bank: {}
Telefono del banco: {}
Ciudad: {}
Url del banco: {}
""".format(bin,brand,brand2,tipe,prepaid,country,bank,phoneBank,city,urlBank)
        
        if(unks<=7):
            return datosS
        else:
            return alternateS(bin)
        
    except:
        return('Invalid Bin')
#---------------------------------------------------
#---------------------------------------------------
#CCGEN PATCHED
especial= False
version = "2.3.1"
def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )
def ccgen(bin_format):
  permiso = True
  while permiso:
    out_cc = ""
    global especial
    completo = 0
    #Iteration over the bin
    if(bin_format[:1]=="3"):
        especial = True
        for i in range(14):
            try:
                if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    out_cc = out_cc + bin_format[i]
                    continue
                elif bin_format[i] in ("x", "X" ):
                    out_cc = out_cc + str(randint(0,9))
                    continue
            except:
                largo = 13 - len(bin_format)
                for x in range(largo):
                    bin_format += 'x'
                out_cc = out_cc + str(randint(0,9))
            else:
                return(False)
        if(completo>=14):
            return('Favor extrapole el bin')
            break
            
    else:    
        especial=False
        for i in range(15):
            try:
                if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    out_cc = out_cc + bin_format[i]
                    completo+=1
                    continue
                elif bin_format[i] in ("x", "X" ):
                    out_cc = out_cc + str(randint(0,9))
                    continue
                
            except:
                largo = 15 - len(bin_format)
                for x in range(largo):
                    bin_format += 'x'
                out_cc = out_cc + str(randint(0,9))
            else:
                return(False)
                break
        if(completo>=15):
            return('Favor extrapole')
    #compare common numbers
    numberC=0
    for i in range(len(bin_format)):
      try:
        if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            numberC+=1
            continue
        elif bin_format[i] in ("x", "X" ):
            continue
      except:
          return('ERRORFATAL')
    #Generate checksum (last digit) -- IMPLICIT CHECK
    for i in range(10):
        checksum_check = out_cc
        if(bin_format[15:]=="" or bin_format[15:] in ("x","X")):
            checksum_check = checksum_check + str(i)    
        else:
            checksum_check = checksum_check + bin_format[15:]
        
        #control numbers common
        respect=0
        if(especial):
          #///
          #Generate checksum (last digit) -- IMPLICIT CHECK
          for i in range(10):
              checksum_check = out_cc
              checksum_check = checksum_check + str(i)

              if cardLuhnChecksumIsValid(checksum_check):
                  out_cc = checksum_check
                  break
              else:
                  checksum_check = out_cc
          return(checksum_check)
          #///
        else:

          for i in range(len(bin_format)):
            
            if(bin_format[i]==checksum_check[i]):
              respect+=1
            else:
              continue
          if (cardLuhnChecksumIsValid(checksum_check) and numberC==respect):
              out_cc = checksum_check
              permiso= False
              break
          else:
              checksum_check = out_cc
            

  return(out_cc)
def ccvgen():
    global especial
    if(especial==False):
        ccv = ""
        num = randint(10,999)

        if num < 100:
            ccv = "0" + str(num)
        else:
            ccv = str(num)
    else:
        ccv = ""
        num = randint(100,9999)

        if num < 1000:
            ccv = "0" + str(num)
        else:
            ccv = str(num)
    
    return(ccv)
def dategen():
    now = datetime.datetime.now()
    date = ""
    month = str(randint(1, 12))
    if(int(month) < 10):
        month = "0"+month
    current_year = str(now.year)
    year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
    date = month + "|" + year

    return date
def monthonly():
    month= str(randint(1,12))
    if(int(month) < 10):
        month = "0"+month
    return month
def yearonly():
    now = datetime.datetime.now()
    date = ""
    current_year = str(now.year)
    year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
    return year
def generadorr(bins, month=False, year=False, codigocvv=False):
    bin_list = []
    #get arg data
    (bin_format) = bins
    if bin_format:
        for i in range(int(5)):
            if bins:
                tewasf = ccgen(bin_format)
                if(tewasf=='Favor extrapole el bin'):
                    return tewasf
                    break
                elif(tewasf):
                    juxs=tewasf 
                else:
                    break
                if(not month and not year and not codigocvv):
                    bin_list.append(
                        juxs 
                        + "|" 
                        + dategen() 
                        + "|" 
                        + ccvgen())
                elif(month or year):
                    if(month and not year):
                        fecha= month + "|" + yearonly()
                    elif(year and not month):
                        fecha= monthonly()+"|"+year
                    elif(year and month):
                        fecha = month+"|"+year
                    if(codigocvv):
                        cv=codigocvv
                    else:
                        cv=ccvgen()
                    bin_list.append(
                        juxs 
                        + "|" 
                        + fecha
                        + "|"
                        + cv)
                elif(not month and not year and codigocvv):
                    bin_list.append(
                        juxs 
                        + "|" 
                        + dategen() 
                        + "|" 
                        + codigocvv)
                tarje = bin_list[i]
                
            
        if not bin_list:
            return False
        else:
            pass
            return bin_list
#---------------------------------------------------
#---------------------------------------------------
#-----------------BANNER----------------------------
ban = """\033[1;32m          ``         T O O L S       ``            
          -h-`                        -           
          dMMy     `::`     ```      :N-           
         `MMMm`.:+shMNy+-./ohNd+:.` /NM/           
         .MMMmdNMMMMMMMh/-yMMMMMMNdsyMM+           
         `NMM+yMMMMMMMm/+o:dMMMMMMMNoNM+           
          yMm`-dNMNNmNNMMMMdhmNMMMm/`dM+          
          +MN-``:++/oNMMMMMMh/+oo/-``hM/           
          `dMm/::hmNMMNMMMMMMNmho-../hm`           
         ` /MMMMNmMMMmdmmmmmNMMNNNmmMM: `          
    `-+ydmo.dMMMMMMmhy/---:ohdNMMMMMMm:hmhs/-      
./shmNMMMMMd+dMMMMMms-.-.-..:hmMMMMMddNMMMMMNdy+: 
:hNMMMMMMMMMNNMMNMMNo-.-----/dNMNNMMNMMMMMMMMMMNs 
 -sMMMMMmyys+dMMNmMNNhyo+oydNmhNmNNMsoyyyNMMMMN+`  
  :dNs::o.`:dNMMNNmNmhhyyhyyydmNNMMMNy.`:o:/hMo-   
   +do-.ym+NMMMMd.`:mNmmddmNNs.`/MMMMMhsN/`/hh.   
    -ddmMMNNMMMMM/ :hMMMMMMMNs. hMMMMMdMMNdds      
     ..yMMMMMMMMd+ -mMMMdNMMMs``yNMMMMMMMM-.       
       .mMMMdy/.                  `-ohNMMMs`       
       `+y+.                         `-sy:                             
       
\033[91m  Este script esta hecho con fines educativos
"""
def banner():
  a="\033[0;32m          ``         T O O L S       ``"
  for i in a:
    print(i,end="",flush=True)
    sleep(0.005)
  a="\n          -h-`                        -"
  for i in a:
    print(i,end="",flush=True)
    sleep(0.005)
  a="\n          dMMy     `::`     ```      :N-"
  for i in a:
    print(i,end="",flush=True)
    sleep(0.005)
  a="\n         `MMMm`.:+shMNy+-./ohNd+:.` /NM/"
  for i in a:
    print(i,end="",flush=True)
    sleep(0.005)
  a="\n         .MMMmdNMMMMMMMh/-yMMMMMMNdsyMM+"
  for i in a:
    print(i,end="",flush=True)
    sleep(0.005)
  a="\n         `NMM+yMMMMMMMm/+o:dMMMMMMMNoNM+"
  for i in a:
    print(i,end="",flush=True)
    sleep(0.005)
  a="\n          yMm`-dNMNNmNNMMMMdhmNMMMm/`dM+"
  for i in a:
    print(i,end="",flush=True)
    sleep(0.005)
  a="\n          +MN-``:++/oNMMMMMMh/+oo/-``hM/"
  for i in a:
    print(i,end="",flush=True)
    sleep(0.005)
  a="\n          `dMm/::hmNMMNMMMMMMNmho-../hm`"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n         ` /MMMMNmMMMmdmmmmmNMMNNNmmMM: `"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n    `-+ydmo.dMMMMMMmhy/---:ohdNMMMMMMm:hmhs/-"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n./shmNMMMMMd+dMMMMMms-.-.-..:hmMMMMMddNMMMMMNdy+:"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n:hNMMMMMMMMMNNMMNMMNo-.-----/dNMNNMMNMMMMMMMMMMNs"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n -sMMMMMmyys+dMMNmMNNhyo+oydNmhNmNNMsoyyyNMMMMN+`"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n  :dNs::o.`:dNMMNNmNmhhyyhyyydmNNMMMNy.`:o:/hMo-"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n   +do-.ym+NMMMMd.`:mNmmddmNNs.`/MMMMMhsN/`/hh."
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n    -ddmMMNNMMMMM/ :hMMMMMMMNs. hMMMMMdMMNdds"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n     ..yMMMMMMMMd+ -mMMMdNMMMs``yNMMMMMMMM-."
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n       .mMMMdy/.                  `-ohNMMMs`"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)
  a="\n       `+y+.                         `-sy:"
  for i in a:
    print(i, end="", flush=True)
    sleep(0.005)

#---------------------------------------------------
#--------------------COMANDOS INLINE----------------
def generarB():
  try:
    os.system('clear')
    print('\033[1;32m'+ccgenlogo,end='\033[0m')
    print()
    print('\033[1;31m'+'OBS: Dejar en blanco para generar aleatorio!')
    print('\033[0m')
    binomio= input('\033[1;33m'+'BIN --> '+'\033[0m')
    mes= input('\033[1;33m'+'MES --> '+'\033[0m')
    ano= input('\033[1;33m'+'AÃ‘O --> '+'\033[0m')
    cvv=     input('\033[1;33m'+'CVV --> '+'\033[0m')
    print('\n-------------------------------------------------------')
    tarjetas = generadorr(binomio, mes, ano, cvv)
    for i in tarjetas:
      print("\033[1;32m"+i.center(50,' '),end='\n')
    print()
    input('\033[1;33m'+'Presione ENTER para continuar...'+'\033[0m')

  except:
    input('\033[1;33m'+'Presione ENTER para continuar...'+'\033[0m')
    print('\033[0m',end='')
def checkearB():
  os.system('clear')
  print('\033[1;32m'+"  ____ _               _    ____  _\n / ___| |__   ___  ___| | _| __ )(_)_ __\n| |   | '_ \ / _ \/ __| |/ /  _ \| | '_ \ \n| |___| | | |  __/ (__|   <| |_) | | | | |\n \____|_| |_|\___|\___|_|\_\____/|_|_| |_|\n",end='\033[0m'+'\n\n')
  print('\033[1;31m'+'OBS: ESTE PROCESO REQUIERE DE INTERNET!'.center(80,' '),end='\033[0m'+'\n')
  binomio= input('\033[1;33m'+'Bin a Buscar --> '+'\033[0m')
  print()
  print(checkear(binomio),end='\n')
  input('\033[1;33m'+'Presione ENTER para continuar...'+'\033[0m')
def extrapolatodoB():
  os.system('clear')
  print('\033[1;32m'+" _____      _                         _           _\n| ____|_  _| |_ _ __ __ _ _ __   ___ | | __ _  __| | ___  _ __\n|  _| \ \/ / __| '__/ _` | '_ \ / _ \| |/ _` |/ _` |/ _ \| '__|\n| |___ >  <| |_| | | (_| | |_) | (_) | | (_| | (_| | (_) | |\n|_____/_/\_\\__|_|  \__,_| .__/ \___/|_|\__,_|\__,_|\___/|_|\n",end='\033[0m'+'\n\n')
  print('\033[1;31m'+'OBS: ESTE PROCESO REQUIERE DOS TARJETAS!'.center(75,' '),end='\033[0m'+'\n')
  tarjeta1=input('\033[1;35m'+'TARJETA 1 --> '+'\033[0m')
  tarjeta2=input('\033[1;35m'+'TARJETA 2 (OPCIONAL) --> '+'\033[0m')
  if(tarjeta2=='' or tarjeta2==' '):
    tarjeta2=False
  print('\033[1;32m',"\t",extrapolar(tarjeta1,tarjeta2),end='\n')
  print()
  input('\033[1;31m'+'Presione ENTER para continuar...'+'\033[0m')

def direccionGen():
  os.system('clear')
  print('\033[1;32m'+'    _    ____  ____  ____  _____ ____ ____\n   / \  |  _ \|  _ \|  _ \| ____/ ___/ ___|\n  / _ \ | | | | | | | |_) |  _| \___ \___ \ \n / ___ \| |_| | |_| |  _ <| |___ ___) |__) |\n/_/   \_\____/|____/|_| \_\_____|____/____/\n\n  ____ _____ _   _ _____ ____      _  _____ ___  ____\n / ___| ____| \ | | ____|  _ \    / \|_   _/ _ \|  _ \ \n| |  _|  _| |  \| |  _| | |_) |  / _ \ | || | | | |_) |\n| |_| | |___| |\  | |___|  _ <  / ___ \| || |_| |  _ <\n \____|_____|_| \_|_____|_| \_\/_/   \_\_| \___/|_| \_\ \n'+'\n'+'\033[0m')
  enlaces={"United States":"http://www.fakeaddressgenerator.com/usa_address_generator","algeria":"http://www.fakeaddressgenerator.com/All_countries/address/country/Algeria","albania":"http://www.fakeaddressgenerator.com/All_countries/address/country/Albania","armenia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Armenia","argentina":"http://www.fakeaddressgenerator.com/All_countries/address/country/Argentina","austria":"http://www.fakeaddressgenerator.com/World/Austria_address_generator","azerbaijan":"http://www.fakeaddressgenerator.com/All_countries/address/country/Azerbaijan","barbados":"http://www.fakeaddressgenerator.com/All_countries/address/country/Barbados","bangladesh":"http://www.fakeaddressgenerator.com/All_countries/address/country/Bangladesh","bahrain":"http://www.fakeaddressgenerator.com/All_countries/address/country/Bahrain","belgium":"http://www.fakeaddressgenerator.com/World/Belgium_address_generator","belarus":"http://www.fakeaddressgenerator.com/World_more/Belarus_address_generator","brunei":"http://www.fakeaddressgenerator.com/All_countries/address/country/Brunei","bolivia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Bolivia","bahamas":"http://www.fakeaddressgenerator.com/All_countries/address/country/Bahamas","botswana":"http://www.fakeaddressgenerator.com/All_countries/address/country/Botswana","brazil":"http://www.fakeaddressgenerator.com/World/Brazil_address_generator","canada":"https://www.fakeaddressgenerator.com/World/ca_address_generator","cayman":"http://www.fakeaddressgenerator.com/All_countries/address/country/Cayman","chile":"http://www.fakeaddressgenerator.com/All_countries/address/country/Chile","china":"http://www.fakeaddressgenerator.com/World_more/china_address_generator","cambodia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Cambodia","cameroon":"http://www.fakeaddressgenerator.com/All_countries/address/country/Cameroon","colombia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Colombia","croatia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Croatia","costaRica":"http://www.fakeaddressgenerator.com/All_countries/address/country/Costa%20Rica","cuba":"http://www.fakeaddressgenerator.com/All_countries/address/country/Cuba","cyprus":"http://www.fakeaddressgenerator.com/All_countries/address/country/Cyprus","czech":"http://www.fakeaddressgenerator.com/World/Czech_address_generator","denmark":"http://www.fakeaddressgenerator.com/World/Denmark_address_generator","dominicanRepublic":"http://www.fakeaddressgenerator.com/All_countries/address/country/Dominican%20Republic","drCongo":"http://www.fakeaddressgenerator.com/All_countries/address/country/DR%20Congo","ecuador":"http://www.fakeaddressgenerator.com/All_countries/address/country/Ecuador","elSalvador":"http://www.fakeaddressgenerator.com/All_countries/address/country/El%20Salvador","egypt":"http://www.fakeaddressgenerator.com/All_countries/address/country/Egypt","emirates":"http://www.fakeaddressgenerator.com/All_countries/address/country/Emirates","estonia":"http://www.fakeaddressgenerator.com/World/Estonia_address_generator","ethiopia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Ethiopia","finland":"http://www.fakeaddressgenerator.com/World/Finland_address_generator","fiji":"http://www.fakeaddressgenerator.com/All_countries/address/country/Fiji","france":"http://www.fakeaddressgenerator.com/World/France_address_generator","gabon":"http://www.fakeaddressgenerator.com/All_countries/address/country/Gabon","georgia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Georgia","germany":"http://www.fakeaddressgenerator.com/World/Germany_address_generator","ghana":"http://www.fakeaddressgenerator.com/All_countries/address/country/Ghana","guatemala":"http://www.fakeaddressgenerator.com/All_countries/address/country/Guatemala",
  "hongkong":"http://www.fakeaddressgenerator.com/All_countries/address/country/Hongkong","honduras":"http://www.fakeaddressgenerator.com/All_countries/address/country/Honduras","hungary":"http://www.fakeaddressgenerator.com/World/Hungary_address_generator","iceland":"http://www.fakeaddressgenerator.com/World/Iceland_address_generator","india":"http://www.fakeaddressgenerator.com/World_more/India_address_generator","indonesia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Indonesia","ireland":"http://www.fakeaddressgenerator.com/All_countries/address/country/Ireland","israel":"http://www.fakeaddressgenerator.com/All_countries/address/country/Israel","iran":"http://www.fakeaddressgenerator.com/All_countries/address/country/Iran","italy":"http://www.fakeaddressgenerator.com/World/Italy_address_generator","ivoryCoast":"http://www.fakeaddressgenerator.com/All_countries/address/country/Ivory%20Coast","jamaica":"http://www.fakeaddressgenerator.com/All_countries/address/country/Jamaica","japan":"http://www.fakeaddressgenerator.com/World_more/Japan_address_generator","jordan":"http://www.fakeaddressgenerator.com/All_countries/address/country/Jordan","kazakhstan":"http://www.fakeaddressgenerator.com/World_more/kazakhstan_address_generator","kenya":"http://www.fakeaddressgenerator.com/All_countries/address/country/Kenya","korea":"http://www.fakeaddressgenerator.com/World_more/Korea_address_generator","kyrgyzstan":"http://www.fakeaddressgenerator.com/All_countries/address/country/Kyrgyzstan","kuwait":"http://www.fakeaddressgenerator.com/All_countries/address/country/Kuwait","latvia":"http://www.fakeaddressgenerator.com/World_more/Latvia_address_generator","lebanon":"http://www.fakeaddressgenerator.com/All_countries/address/country/Lebanon","sriLanka":"http://www.fakeaddressgenerator.com/All_countries/address/country/Sri%20Lanka","lesotho":"http://www.fakeaddressgenerator.com/All_countries/address/country/Lesotho","lithuania":"http://www.fakeaddressgenerator.com/All_countries/address/country/Lithuania","luxembourg":"http://www.fakeaddressgenerator.com/All_countries/address/country/Luxembourg","libya":"http://www.fakeaddressgenerator.com/All_countries/address/country/Libya","morocco":"http://www.fakeaddressgenerator.com/All_countries/address/country/Morocco","madagascar":"http://www.fakeaddressgenerator.com/All_countries/address/country/Madagascar","mali":"http://www.fakeaddressgenerator.com/All_countries/address/country/Mali","myanmar":"http://www.fakeaddressgenerator.com/All_countries/address/country/Myanmar","malta":"http://www.fakeaddressgenerator.com/All_countries/address/country/Malta","mauritius":"http://www.fakeaddressgenerator.com/All_countries/address/country/Mauritius","malawi":"http://www.fakeaddressgenerator.com/All_countries/address/country/Malawi","mexico":"http://www.fakeaddressgenerator.com/All_countries/address/country/Mexico","malaysia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Malaysia","moldova":"http://www.fakeaddressgenerator.com/World_more/Moldova_address_generator","namibia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Namibia","newZealand":"http://www.fakeaddressgenerator.com/World/New_Zealand_address_generator","nigeria":"http://www.fakeaddressgenerator.com/All_countries/address/country/Nigeria","nicaragua":"http://www.fakeaddressgenerator.com/All_countries/address/country/Nicaragua","nepal":"http://www.fakeaddressgenerator.com/All_countries/address/country/Nepal","netherlands":"http://www.fakeaddressgenerator.com/World/Netherlands_address_generator","norway":"http://www.fakeaddressgenerator.com/World/Norway_address_generator","oman":"http://www.fakeaddressgenerator.com/All_countries/address/country/Oman","panama":"http://www.fakeaddressgenerator.com/All_countries/address/country/Panama","peru":"http://www.fakeaddressgenerator.com/All_countries/address/country/Peru","papuaNewGuinea":"http://www.fakeaddressgenerator.com/All_countries/address/country/Papua%20New%20Guinea","philippines":"http://www.fakeaddressgenerator.com/All_countries/address/country/Philippines","pakistan":"http://www.fakeaddressgenerator.com/All_countries/address/country/Pakistan","puertoRico":"http://www.fakeaddressgenerator.com/All_countries/address/country/Puerto%20Rico","paraguay":"http://www.fakeaddressgenerator.com/All_countries/address/country/Paraguay","poland":"http://www.fakeaddressgenerator.com/World/Poland_address_generator","portugal":"http://www.fakeaddressgenerator.com/World/Portugal_address_generator","qatar":"http://www.fakeaddressgenerator.com/All_countries/address/country/Qatar","romania":"http://www.fakeaddressgenerator.com/All_countries/address/country/Romania","russia":"http://www.fakeaddressgenerator.com/World_more/Russia_address_generator","rwanda":"http://www.fakeaddressgenerator.com/All_countries/address/country/Rwanda","saudiArabia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Saudi%20Arabia","singapore":"http://www.fakeaddressgenerator.com/All_countries/address/country/Singapore","slovakia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Slovakia","senegal":"http://www.fakeaddressgenerator.com/All_countries/address/country/Senegal%3C","spain":"http://www.fakeaddressgenerator.com/World/Spain_address_generator","slovenia":"http://www.fakeaddressgenerator.com/World_more/Slovenia_address_generator","suriname":"http://www.fakeaddressgenerator.com/All_countries/address/country/Suriname","southAfrica":"http://www.fakeaddressgenerator.com/World_more/South_Africa_address_generator","sweden":"http://www.fakeaddressgenerator.com/World_more/Sweden_address_generator","switzerland":"http://www.fakeaddressgenerator.com/World_more/Switzerland_address_generator","syria":"http://www.fakeaddressgenerator.com/All_countries/address/country/Syria","thailand":"http://www.fakeaddressgenerator.com/All_countries/address/country/Thailand","turkey":"http://www.fakeaddressgenerator.com/All_countries/address/country/Turkey","trinidadAndTobago":"http://www.fakeaddressgenerator.com/All_countries/address/country/Trinidad%20and%20Tobago","taiwan":"http://www.fakeaddressgenerator.com/All_countries/address/country/Taiwan","tanzania":"http://www.fakeaddressgenerator.com/All_countries/address/country/Tanzania","tunisia":"http://www.fakeaddressgenerator.com/World_more/Tunisia_address_generator","United Kingdom":"http://www.fakeaddressgenerator.com/World/uk_address_generator","uganda":"http://www.fakeaddressgenerator.com/All_countries/address/country/Uganda","ukraine":"http://www.fakeaddressgenerator.com/World_more/Ukraine_address_generator","uruguay":"http://www.fakeaddressgenerator.com/World_more/Uruguay_address_generator","uzbekistan":"http://www.fakeaddressgenerator.com/All_countries/address/country/Uzbekistan","venezuela":"http://www.fakeaddressgenerator.com/All_countries/address/country/Venezuela","vietnam":"http://www.fakeaddressgenerator.com/All_countries/address/country/Vietnam","yemen":"http://www.fakeaddressgenerator.com/All_countries/address/country/Yemen","zambia":"http://www.fakeaddressgenerator.com/All_countries/address/country/Zambia","zimbabwe":"http://www.fakeaddressgenerator.com/All_countries/address/country/Zimbabwe"}
  i=0
  for key,value in enlaces.items():
      print("[{}] - {}".format(i,key))
      i+=1
  paiselegido=input('\nIngrese el numero del pais a buscar --> ')
  paiselegido=int(paiselegido)
  i=0
  for key,value in enlaces.items():
      if(i==paiselegido):
          print(key)
          page=value
      i+=1
  values={}
  user_agent = {'User-agent': 'Mozilla/5.0'}
  page= requests.post(page, headers=user_agent, data=values).text
  #print(page)
  soup=BeautifulSoup(page,"html.parser")
  items= soup.findAll("div", attrs={"class":"row item"})

  for row in items:
    divs=row.findAll("div")
    title=divs[0]
    title=title.find("span").text

    value=divs[1]
    try:
      value=value.find("input").get("value")
    except:
      value="None"
    print("\033[1;33m"+title,":",value)
  print()
  print()
  input('\033[1;32m'+'Presione ENTER para continuar... ')
#---------------------------------------------------
#---------------------------------------------------
def main():
  b=0
  os.system('clear')
  print("\033[1;32;45m",end='')
  banner()
  print()
  while True:
    if(b>0):
      os.system('clear')
      print(ban.center(50," "))
    print('\033[0m')
    for i in '\033[1;33m'+'[1] GENERAR CCS A BASE DE BIN':
        print(i,end='',flush=True)
        sleep(0.007)
    print()
    for i in '\033[1;32m'+'[2] CHECK BIN':
        print(i,end='',flush=True)
        sleep(0.007)
    print()
    for i in '\033[1;35m'+'[3] EXTRAPOLAR BIN/CC':
        print(i,end='',flush=True)
        sleep(0.007)
    for i in '\033[1;36m'+'\n[4] GENERAR DIRECCION':
        print(i,end='',flush=True)
        sleep(0.007)
    print()
    print()
    opt=input("\033[1;31m""~~>"+'\033[0m')
    if(opt=='version' or opt=='Version'):
      print('VERSION E INFO DEL PROGRAMA...')
      print('CREADO POR @LANNISCAF')
      print('VERSION: 0.1.3V')
      sleep(2)
    elif(opt=='1'):
      generarB()
    elif(opt=='2'):
      try:
        checkearB()
      except:
        print('Error! VERIFICA TU CONEXION A RED')
        sleep(1.2)
    elif(opt=='3'):
      extrapolatodoB()
    elif(opt=="4"):
      try:
        direccionGen()
      except:
        print("ERROR: VERIFIQUE SU RED Y ELIJA UN PAIS VALIDO!")
    else:
      for i in 'Opcion Invalida!':
        print(i,end='',flush=True)
        sleep(0.03)
      sleep(0.02)
    b=1
  
    



if __name__ == "__main__":
  try:
    main()
  except:
    print("Fatal Err")
