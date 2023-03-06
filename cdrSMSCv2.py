import os
import csv
import glob
import sys
import tkinter as tk
from tkinter import filedialog, Tk, Text, BOTH, W, N, E, S
from datetime import datetime, timedelta
from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Frame, Button, Label, Style
import paramiko
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar
from threading import Thread
from tkcalendar import *

host = "10.111.30.204"
port = 22
username = "taskmng"
password = "Atae_123"
dateTocomp = datetime.now() - timedelta(days=3)


def get_date(calen):
    x = (datetime.strftime(calen.get_date(), '%Y%m%d'))
    return x

def create_thread():
  run_thread = Thread(target=search)
  run_thread.start()
  pb1.start()

def search():
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connect(host, port, username, password)
  session = client.get_transport().open_session()
  x = ""
  p=0
  liste = []
  liste2 = []
  tableau.delete(*tableau.get_children())
  inputValue1=textBox1.get("1.0","end-1c")
  inputValueCall=textBoxcall.get("1.0","end-1c")
  #inputValue2=textBox2.get("1.0","end-1c")
  inputValue2=get_date(cal1)
  #inputValue3=textBox3.get("1.0","end-1c")
  inputValue3=get_date(cal2)

  
  if (inputValue1=="" and inputValueCall==""):
      messagebox.showinfo("None input", "Insert caller or callee")

  if (inputValue2=="" and inputValue3==""):
      messagebox.showinfo("None date input", "Insert date")
      
  if (inputValue1!="" and inputValueCall==""):
    if (inputValue2 > inputValue3):
        messagebox.showinfo("None date input", "End date must be greater than start date")
    
    else:
      print ("searching ...")
      
      
      while(x != inputValue3):
        x =(datetime.strptime(inputValue2, '%Y%m%d') + timedelta(days=p)).strftime('%Y%m%d')
        liste.append(x)
        p = p+1
      
      selection = v.get()
      if selection ==1:
        for y in liste:
         com = "/home/taskmng/bill/backup/cursite/451/SMApp/11/"+y+"/prm*"
         liste2.append(com)
        cmd = "zgrep "+inputValue1+" "+' '.join(liste2)+" | awk -F\",\" \'{print$1,$2,$3,$22,$16,$18,$20,$20,$26,$53}\' | awk -F\"gz:\" \'{print$2}\'"
        #stdin, stdout, stderr = client.exec_command("zgrep {a} /home/smc/billdata/checkbill/checkbak/{b}/SMC*.txt.gz | awk -F\",\" \'{print$3,$7,$11,$12,$17,$18,$19,$23,$24}\'".format(a=inputValue1,b=inputValue2))
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        print(len(lines))
        record.set(len(lines))
        for i in lines:
          sp = i.split()
          print(sp)
		  #begin
          if (len(sp)== 13):
            sp[1]=sp[1]+" "+sp[2]
            sp.pop(2)
          #Fin
          if (len(sp) == 10):
            sp.insert(5,' ')
            sp.insert(6,' ')
          if (sp[8] == "0"):
              sp[8] = "Success"
          else :
              sp[8] = "Failed"
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10],sp[11]))
        client.close()
        """cmd = "zgrep "+inputValue1+" /home/smc/billdata/bpsbill/11/backup/prm"+inputValue2+"* | zgrep "+inputValueCall+" | awk -F\",\" \'{print$2,$3,$22,$16,$18,$20,$20,$26,$53}\'"
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        #print(resp)
        for i in lines:
          sp = i.split()
          print(sp)
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10]))
        client.close()"""

      if selection ==2:
        for y in liste:
         com = "/home/taskmng/bill/backup/cursite/451/SMApp/12/"+y+"/prm*"
         liste2.append(com)
        cmd = "zgrep "+inputValue1+" "+' '.join(liste2)+" | awk -F\",\" \'{print$1,$2,$3,$14,$20,$15,$16,$17,$26,$27,$22}\' | awk -F\"gz:\" \'{print$2}\'"
        #stdin, stdout, stderr = client.exec_command("zgrep {a} /home/smc/billdata/checkbill/checkbak/{b}/SMC*.txt.gz | awk -F\",\" \'{print$3,$7,$11,$12,$17,$18,$19,$23,$24}\'".format(a=inputValue1,b=inputValue2))
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        print(len(lines))
        record.set(len(lines))
        for i in lines:
          sp = i.split()
          print(sp)
		  #begin
          if (len(sp)== 14):
            sp[1]=sp[1]+" "+sp[2]
            sp.pop(2)
          #Fin
          if (len(sp) == 11):
            sp.insert(5,' ')
            sp.insert(6,' ')
          if (sp[8] == "0"):
              sp[8] = "Success"
          else :
              sp[8] = "Failed"
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10],sp[11],sp[12]))
        client.close()
        """cmd = "zgrep "+inputValue1+" /home/smc/billdata/bpsbill/12/backup/prm"+inputValue2+"* | zgrep "+inputValueCall+" | awk -F\",\" \'{print$2,$3,$14,$20,$15,$16,$16,$26,$27}\'"
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        #print(resp)
        for i in lines:
          sp = i.split()
          print(sp)
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10]))
        client.close()"""


      if selection ==3:
        for y in liste:
         com = "/home/taskmng/bill/backup/cursite/451/SMApp/checkbill/"+y+"/SMC*"
         liste2.append(com)
        cmd = "zgrep "+inputValue1+" "+' '.join(liste2)+" | awk -F\",\" \'{print$2,$3,$7,$11,$12,$17,$18,$19,$23,$24,$33}\'"
        #stdin, stdout, stderr = client.exec_command("zgrep {a} /home/smc/billdata/checkbill/checkbak/{b}/SMC*.txt.gz | awk -F\",\" \'{print$3,$7,$11,$12,$17,$18,$19,$23,$24}\'".format(a=inputValue1,b=inputValue2))
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        print(len(lines))
        record.set(len(lines))
        for i in lines:
          sp = i.split()
          print(sp)
		  #begin
          if (len(sp)== 14):
            sp[1]=sp[1]+" "+sp[2]
            sp.pop(2)
          #Fin
          if (len(sp) == 11):
            sp.insert(5,' ')
            sp.insert(6,' ')
          if (sp[8] == "1"):
              sp[8] = "Success"
          else :
              sp[8] = "Failed"
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10],sp[11],sp[12]))
        client.close()

      
  if (inputValue1!="" and inputValueCall!=""):
    if (inputValue2 > inputValue3):
        messagebox.showinfo("None date input", "End date must be greater than start date")
        
    else:
      print ("searching ...")
      
      
      while(x != inputValue3):
        x =(datetime.strptime(inputValue2, '%Y%m%d') + timedelta(days=p)).strftime('%Y%m%d')
        liste.append(x)
        p = p+1
      
      selection = v.get()
      if selection ==1:
        for y in liste:
         com = "/home/taskmng/bill/backup/cursite/451/SMApp/11/"+y+"/prm*"
         liste2.append(com)
         
        cmd = "zgrep "+inputValue1+" "+' '.join(liste2)+" | zgrep "+inputValueCall+" | awk -F\",\" \'{print$1,$2,$3,$22,$16,$18,$20,$20,$26,$53}\' | awk -F\"gz:\" \'{print$2}\'"
        #stdin, stdout, stderr = client.exec_command("zgrep {a} /home/smc/billdata/checkbill/checkbak/{b}/SMC*.txt.gz | awk -F\",\" \'{print$3,$7,$11,$12,$17,$18,$19,$23,$24}\'".format(a=inputValue1,b=inputValue2))
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        print(len(lines))
        record.set(len(lines))
        for i in lines:
          sp = i.split()
          print(sp)
		  #begin
          if (len(sp)== 13):
            sp[1]=sp[1]+" "+sp[2]
            sp.pop(2)
          #Fin
          if (len(sp) == 10):
            sp.insert(5,' ')
            sp.insert(6,' ')
          if (sp[8] == "0"):
              sp[8] = "Success"
          else :
              sp[8] = "Failed"
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10],sp[11]))
        client.close()
        """cmd = "zgrep "+inputValue1+" /home/smc/billdata/bpsbill/11/backup/prm"+inputValue2+"* | zgrep "+inputValueCall+" | awk -F\",\" \'{print$2,$3,$22,$16,$18,$20,$20,$26,$53}\'"
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        #print(resp)
        for i in lines:
          sp = i.split()
          print(sp)
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10]))
        client.close()"""

      if selection ==2:
        for y in liste:
         com = "/home/taskmng/bill/backup/cursite/451/SMApp/12/"+y+"/prm*"
         liste2.append(com)
        
        cmd = "zgrep "+inputValue1+" "+' '.join(liste2)+" | zgrep "+inputValueCall+" | awk -F\",\" \'{print$1,$2,$3,$14,$20,$15,$16,$17,$26,$27,$22}\' | awk -F\"gz:\" \'{print$2}\'"
        #stdin, stdout, stderr = client.exec_command("zgrep {a} /home/smc/billdata/checkbill/checkbak/{b}/SMC*.txt.gz | awk -F\",\" \'{print$3,$7,$11,$12,$17,$18,$19,$23,$24}\'".format(a=inputValue1,b=inputValue2))
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        print(len(lines))
        record.set(len(lines))
        for i in lines:
          sp = i.split()
          print(sp)
		  #begin
          if (len(sp)== 14):
            sp[1]=sp[1]+" "+sp[2]
            sp.pop(2)
          #Fin
          if (len(sp) == 11):
            sp.insert(5,' ')
            sp.insert(6,' ')
          if (sp[8] == "0"):
              sp[8] = "Success"
          else :
              sp[8] = "Failed"
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10],sp[11],sp[12]))
        client.close()
        """cmd = "zgrep "+inputValue1+" /home/smc/billdata/bpsbill/12/backup/prm"+inputValue2+"* | zgrep "+inputValueCall+" | awk -F\",\" \'{print$2,$3,$14,$20,$15,$16,$16,$26,$27}\'"
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        #print(resp)
        for i in lines:
          sp = i.split()
          print(sp)
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10]))
        client.close()"""


      if selection ==3:
        for y in liste:
         com = "/home/taskmng/bill/backup/cursite/451/SMApp/checkbill/"+y+"/SMC*"
         liste2.append(com)
        
        cmd = "zgrep "+inputValue1+" "+' '.join(liste2)+" | zgrep "+inputValueCall+" | awk -F\",\" \'{print$2,$3,$7,$11,$12,$17,$18,$19,$23,$24,$33}\'"
        #stdin, stdout, stderr = client.exec_command("zgrep {a} /home/smc/billdata/checkbill/checkbak/{b}/SMC*.txt.gz | awk -F\",\" \'{print$3,$7,$11,$12,$17,$18,$19,$23,$24}\'".format(a=inputValue1,b=inputValue2))
        stdin, stdout, stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        #resp=''.join(lines)
        #text.insert(tk.END,resp)
        print(len(lines))
        record.set(len(lines))
        for i in lines:
          sp = i.split()
          print(sp)
		  #begin
          if (len(sp)== 14):
            sp[1]=sp[1]+" "+sp[2]
            sp.pop(2)
          #Fin
          if (len(sp) == 11):
            sp.insert(5,' ')
            sp.insert(6,' ')
          if (sp[8] == "1"):
              sp[8] = "Success"
          else :
              sp[8] = "Failed"
          if len(sp):
            tableau.insert('','end', values=(sp[0],sp[1],sp[2],sp[3],sp[4],sp[5],sp[6],sp[7],sp[8],sp[9],sp[10],sp[11],sp[12]))
        client.close()
  pb1.stop()

def save_csv():
    with open("cdrsaved.csv", "w", newline='') as myfile:
        csvwriter = csv.writer(myfile, delimiter=';')
        csvwriter.writerow(['SM ID','Sender','Receiver','StartDate','StartTime','StopDate','StopTime','SMlength','SMstatus','ErrorCode','OrgAccount','DestAccount','DeliverCount'])
        for row_id in tableau.get_children():
            row = tableau.item(row_id)['values']
            print('save row:', row)
            csvwriter.writerow(row)      
    
    
    
master = Tk()
master.title('Get CDR SMS')
v = IntVar()
v.set("3")
l1 = Label(master, text = "Get CDR SMS")
l1.grid(row=0, column = 1, sticky = N, pady = 2)

l1 = Label(master, text = "Sender")
l1.grid(row=1, column = 0, sticky=tk.W, pady = 2)



textBox1=Text(master, height=1, width=50)
textBox1.grid(row=1, column = 1, pady = 4, sticky=tk.W)

lcall = Label(master, text = "Receiver")
lcall.grid(row =2, column = 0, sticky=tk.W, pady = 2)

textBoxcall=Text(master, height=1, width=50)
textBoxcall.grid(row=2, column = 1, pady = 4, sticky=tk.W)

l2 = Label(master, text = "Start date")
l2.grid(row=3, column = 0, sticky=tk.W, pady = 2)

#textBox2=Text(master, height=1, width=50)
#textBox2.grid(row=3, column = 1, pady = 4, sticky=tk.W)
cal1= DateEntry(master, selectmode="day", date_pattern='y/mm/dd')
cal1.grid(row=3, column = 1, sticky=tk.W)
l2date = Label(master, text = "End date")
l2date.grid(row=4, column = 0, sticky=tk.W, pady = 2)
#textBox3=Text(master, height=1, width=50)
#textBox3.grid(row=4, column = 1,pady=4, sticky=tk.W)
cal2= DateEntry(master, selectmode="day", date_pattern='y/mm/dd')
cal2.grid(row=4, column = 1, sticky=tk.W)




r1 = Radiobutton(master, text="MO", variable=v, value=1)
r1.grid(row=5, column = 0, sticky=tk.W, pady = 4)
r2 = Radiobutton(master, text="MT", variable=v, value=2)
r2.grid(row=5, column = 1, sticky=tk.W, pady = 4)
r3 = Radiobutton(master, text="checkbak", variable=v, value=3)
r3.grid(row=5, column = 2, sticky=tk.W, pady = 4)
l3 = Label(master, text = "Résultat")
l3.grid(row=6, column = 1, sticky=tk.W, pady = 2)

tableau = Treeview(master,columns=('SM ID','originalAdress', 'destinationAdress', 'Org_Submission_Time','org_time','finalTime','time','SMlength','SMstatus','ErrorCode','OrgAccount','DestAccount','DeliverCount'))

tableau.heading('SM ID', text='SM ID')
tableau.column('SM ID', width = 100)
tableau.heading('originalAdress', text='Sender')
tableau.column('originalAdress', width = 100)
tableau.heading('destinationAdress', text='Receiver')
tableau.column('destinationAdress', width = 100)
tableau.heading('Org_Submission_Time', text='Start Date')
tableau.column('Org_Submission_Time', width = 100)
tableau.heading('org_time', text='Start time')
tableau.column('org_time', width = 100)
tableau.heading('finalTime', text='Stop Date')
tableau.column('finalTime', width = 100)
tableau.heading('time', text='Stop Time')
tableau.column('time', width = 100)
tableau.heading('SMlength', text='SM length')
tableau.column('SMlength', width = 100)
tableau.heading('SMstatus', text='SM status')
tableau.column('SMstatus', width = 100)
tableau.heading('ErrorCode', text='Error Code')
tableau.column('ErrorCode', width = 100)
tableau.heading('OrgAccount', text='Original Account')
tableau.column('OrgAccount', width = 100)
tableau.heading('DestAccount', text='Destination Account')
tableau.column('DestAccount', width = 100)
tableau.heading('DeliverCount', text='Deliver Count')
tableau.column('DeliverCount', width = 100)
tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert

#treeYScroll = ttk.Scrollbar(master, orient=VERTICAL)
#tableau.configure(yscrollcommand=treeYScroll.set)
#treeYScroll.grid(column=2, row=6, columnspan=3, sticky=W + E)
#treeYScroll.grid(column=1, row=6, sticky = tk.E, pady = 1)

tableau.grid(row=7, column = 0, sticky = tk.W,columnspan=3)

button_choice = tk.Button(master, text='search', command=create_thread)
button_choice.grid(row=8, column = 0, pady = 4,padx = 5 )
button_save= tk.Button(master, text='save', command=save_csv)
button_save.grid(row=8, column = 2, pady = 4,padx = 5 )
l4 = Label(master, text = "Total records :")
record = tk.StringVar()
lab = Label(master,textvariable=record)
l4.grid(row=9, column = 0, sticky = W, pady = 2)
lab.grid(row=9, column = 1, sticky = W, pady = 2)
pb1 = Progressbar(master, orient=HORIZONTAL, length=100, mode='indeterminate')
pb1.grid(row=10, column = 0, sticky = W, pady = 2)
mainloop()
