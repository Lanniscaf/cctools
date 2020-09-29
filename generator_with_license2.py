# ----------------------------------------------------------------
# CODIGO ABIERTO PARA IMPORTAR Y/O MODIFICAR
# USO LIBRE Y A SU PROPIA DISCRECION
#-----------------------------------------------------------------

from time   import sleep
from random import randint
import re, time, datetime

# LOG V0.0.1+ALPHA by L
class Log():
    def __init__(self, archivo="nombre.txt"):
        self.nombre=archivo
    def write(self, mensaje=""):
        with open(self.nombre,"a+") as f:
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                f.write("\n")
            f.write(mensaje)
            f.close()
    def reset(self):
        with open(self.nombre,"w") as f:
            f.write("")
            f.close()
    def read(self):
        with open(self.nombre,"r") as f:
            lineas = f.readlines()
            f.close()
            return lineas
class Tools():
  """
  TOOLS IS BASED IN
  CCTOOLS - Multi Tools of Carding, EDUCATIONAL PURPOSES.
  Copyright (C) 2020  

  DISCLAIMER: This file is for informational and educational purposes only. 
  We are not responsible for any misuse applied to it. All responsibility falls on the user

  ||================================================================================||
  || FRAGMENTS USED FROM https://github.com/Lanniscaf/cctools/blob/master/cctools.py||
  ||================================================================================||

  Adapted BY flyead ALL RIGHTS RESERVED
  """
  def __init__(self):
    self.especialCCG = False
    self.fromFileName = 'binlist.txt'
    super()
  def __cardLuhnChecksumIsValid(self,card_number):
    # // checks to make sure that the card passes a luhn mod-10 checksum 
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
  def __ccgen(self, bin_format):
    permiso = True
    while permiso:
      out_cc = ""
      completo = 0
      #Iteration over the bin
      if(bin_format[:1]=="3"):
          self.especial = True
          for i in range(15):
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
                  print('else')
          if(completo>=14):
              return('Favor extrapole el bin')
              break
              
      else:    
          self.especial=False
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
          if(self.especial):
            #///
            #Generate checksum (last digit) -- IMPLICIT CHECK
            for i in range(10):
                checksum_check = out_cc
                checksum_check = checksum_check + str(i)

                if self.__cardLuhnChecksumIsValid(checksum_check):
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
            if (self.__cardLuhnChecksumIsValid(checksum_check) and numberC==respect):
                out_cc = checksum_check
                permiso= False
                break
            else:
                checksum_check = out_cc
              

    return(out_cc)   
  def __ccvgen(self):
    if(self.especial==False):
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
  def __dategen(self):
    now = datetime.datetime.now()
    date = ""
    month = str(randint(1, 12))
    if(int(month) < 10):
        month = "0"+month
    current_year = str(now.year)
    year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
    date = month + "|" + year

    return date
  def __monthonly(self):
    month= str(randint(1,12))
    if(int(month) < 10):
        month = "0"+month
    return month
  def __yearonly(self):
    now = datetime.datetime.now()
    date = ""
    current_year = str(now.year)
    year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
    return year
  def generador(self, bins, month=False, year=False, codigocvv=False):
    try:
      if(bins != ''):
        beans = list()
        beans.append(self.regex(bins[0])[0])
        cc_list = list()
        for _ in range(10):
          bin_format = beans[0]
          banIA = self.__ccgen(bin_format)
          if(banIA == 'Favor extrapole el bin'):
            # //EL BIN NO ESTA EXTRAPOLADO
            return False

          if(month == False):
            mes=self.__monthonly()
          elif(month != False):
            mes=month
          if(year == False):
            ano=self.__yearonly()
          elif(year != False):
            ano=year
          if(codigocvv == False):
            carverificationv=self.__ccvgen()
          elif(codigocvv != False):
            carverificationv=codigocvv
          
          if(banIA == False):
            return False
          cc_list.append('{0}|{1}|{2}|{3}'.format(banIA,mes,ano,carverificationv))
        return cc_list

    except:
      return False
  def regex(self, toParse):
    format = r'([A-Za-z]|\s)'
    return re.subn(format, '', toParse)
  def ccgenFromList(self, bins, month=False, year=False, cvv=False):
    try:
      if(type(bins) == type([])):
        i = 0
        for l in bins:
          i += 1
        if i == 1:
          return self.generador(bins)
        # // el usuario entrgo una lista de bins
        beans = list()
        for bin_f in bins:
          scaped = self.regex(bin_f)
          beans.append(scaped)
        cc_list = list()
        for bin_format in beans:
          banIA = self.__ccgen(bin_format[0])
          if(banIA == 'Favor extrapole el bin'):
            # //EL BIN NO ESTA EXTRAPOLADO
            return False

          if(month == False):
            mes=self.__monthonly()
          elif(month != False):
            mes=month
          if(year == False):
            ano=self.__yearonly()
          elif(year != False):
            ano=year
          if(cvv == False):
            carverificationv=self.__ccvgen()
          elif(cvv != False):
            carverificationv=cvv
          
          cc_list.append('{0}|{1}|{2}|{3}'.format(banIA,mes,ano,carverificationv))
        return cc_list  

    except:
      return False
  def fromFileList(self):
    log = Log(archivo= self.fromFileName)
    result = self.ccgenFromList(log.read())
    log.reset()
    message = ''
    # formato
    for i in result:
      message += i + '\n'
    log.write(mensaje=message)
    

try:
  # // al iniciar el archivo intenta buscar si hay una lista de bins para usar
  Tools().fromFileList()
except:
  pass

#  ///////////////
# USO: CREAR UNA INSTANCIA DEL OBJETO TOOLS (PUEDES RENOMBRARLO)
# SE PUEDE AJUSTAR EL NOMBRE 
# PUEDES BORRAR LA LICENCIA PERO DEBE SER INCLUIDO MINIMO UNA MENCION
# HAY ALGUNAS PARTES PERSONALIZABLES EN LA CLASE LOG Y EN LA DE TOOLS EN LOS __INIT
# PUEDES PERSONALIZAR MAS LOS ERRORES DE TOOLS Y ANADIRLE MAS FUNCIONES
# PARA APLICAR EN TU BOT DE TELEGRAM PUEDES SIMPLEMENTE IMPORTAR ESTE ARCHIVO Y CREAR UNA INSTANCIA
# DE LA CLASE DONDE LA NECESITES, POR DEFECTO LA CLASE DEVUELVE UNA LISTA CON LAS TARJETAS
# PUEDES MODIFICAR EL FORMATO DE SALIDA EN TOOLS > FROMLIST


# //TODO: ANADIR PERSONALIZACION DE MES|ANO|CVV

#bins = ['5042068','507809']
#binf = ['408305']
#obj = Tools()

#print(obj.ccgenFromList(bins))
#print(obj.ccgenFromList(binf))

