import pika
import time
import sys
from tkinter import *

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='Notepad Directory')
print("Enter a note or enter 'stop' to stop.")

root = Tk()
root.title('Simple Notepad')
root.geometry("500x500")
root.config(bg = "grey")
root.resizable(0, 0)

makeNote = Text(root, width = 30, height = 10)
makeNote.pack(side = TOP, pady = 10, padx = 10, fill = X)
showNotes = Text(root, width = 30, height = 10)
showNotes.pack(side = TOP, pady = 10, padx = 10, fill = X)

def callback(ch, method, properties, body):
    ctr = 1
    print(" [x] received %r" % body)
    notes.append(body)

    for i in notes:
        print(i.decode('utf-8'))
        ctr += 1
    n = notes

def getNote():
    global makeNote
    note = makeNote.get("1.0",'end-1c')
    channel.basic_publish(exchange='', routing_key='Notepad Directory', body=note)
    print("Note saved.")
save = Button(text = "Save Note", highlightcolor = "#E4F2FA", font = ('times 14'), bg = '#0EC90D', width = 15, height = 15, padx = 5, pady = 5, command = getNote)
save.pack(side = LEFT)

def delNote():
    makeNote.delete("1.0", "end")
    showNotes.delete("1.0", "end")
delete = Button(text = "Clear Entry", highlightcolor = "#E4F2FA", font = ('times 14'), bg = "#ED2B02", width = 15, height = 15, padx = 5, pady = 5, command = delNote)
delete.pack(side = RIGHT)

def importNotes():
    channel.basic_consume(queue='Notepad Directory', auto_ack=True, on_message_callback=callback2)
    channel.start_consuming()
    channel.basic_publish(exchange='', routing_key='Notepad Directory', body=notes)
    for i in notes:
        showNotes.insert(INSERT, body[i])
importN = Button(text = "Import Note", highlightcolor = "#E4F2FA", font = ('times 14'), bg = "#2FABF9", width = 15, height = 15, padx = 5, pady = 5, command = importNotes)
importN.pack(side = BOTTOM) 

root.mainloop()