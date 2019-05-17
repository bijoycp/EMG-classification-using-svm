# sudo pip3 install matplotlib==3.0.3
# sudo pip3 install python-csv

import tkinter
import os

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter import *
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt

import numpy as np

from sklearn import datasets
from sklearn import svm

from sklearn.externals import joblib

dir0="patient_data"
data_len=1500
try:
    os.mkdir(dir0)
except:
    print('contain folder in same name')

root = tkinter.Tk()
root.wm_title("Electromyo Belt")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig,master=root)

file_name_read=StringVar()
state = BooleanVar()
state.set(False)
v = StringVar() 
v.set("")

fields = ('Name', 'Age', 'Sex')


def gen_graph():

  x=[]
  f_name_local=file_name_read.get()
  print('patient_data/'+str(f_name_local)+'.csv')
  ii=0
  with open('patient_data/'+str(f_name_local)+'.csv','r') as csvfile:
    plots = csv.reader(csvfile)
    # print(plots)
    next(plots)
    for row in plots:
      
      x.append(int(row[0]))
      print(type(x[0]))
      ii=ii+1
      if(ii>data_len):
        break
      # y.append(int(row[1]))
  print(x)
  # plt.plot(x, label='Loaded from file!')
  # plt.title('EMG')
  # plt.legend()
  # plt.show()

  fig.autofmt_xdate()
  import matplotlib.dates as mdates
  ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')  
  ax.cla()
  line, = ax.plot(x)


  canvas.draw()
  canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH)

  clf = svm.SVC(kernel='linear')
  filename = 'EMG-model.sav'
  clf1 = joblib.load(filename)
  print("output")

  pred=clf1.predict([x])
  if(pred==0):
    v.set("state : UBNORMAL")
    print("ubnormal")
  elif(pred==1):
    v.set("state : NORMAL")
    print("ubnormal")


def emg_data():
   global ax
   if (state.get()):
    ax.cla()
    canvas.draw()
   filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt file","*.txt"),("all files","*.*")))
   print(filename)
   file_str=str(filename)
   file_list=filename.split('/')
   print(file_list[-1])
   f_name=file_list[-1].split('.')
   ff_name=f_name[0]
   print(ff_name)
   file_name_read.set(ff_name)

   with open(filename, 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('patient_data/'+ff_name+'.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)
    return ff_name
def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries


ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e = ents: fetch(e)))
 

b1 = Button(root, text = 'EMG Data',
  command=emg_data)
b1.pack(side = LEFT, padx = 5, pady = 5)
b2 = Button(root, text='Generate Graph ',
command=gen_graph)
b2.pack(side = LEFT, padx = 5, pady = 5)
b3 = Button(root, text = 'Quit', command = root.quit)
b3.pack(side = LEFT, padx = 5, pady = 5)
l2=Label(root, width=22, textvariable=v)
l2.pack(side = BOTTOM, padx = 5, pady = 5,anchor='w')




def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)





def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


# button = tkinter.Button(master=root, text="Quit", command=_quit)
# button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.