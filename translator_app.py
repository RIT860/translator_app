#Work for Translator
#************---IMPORT TRANSLATOR ------*******************
#CMD :- pip install googletrans==4.0.0-rc1


#Sir/mam, I am unable to run this code because I can't install Tkinter. 
# Therefore, this code won't execute here. 
# Sir, please install both Tkinter and Google Translator so that the code can be executed.


from tkinter import *  # Importing tkinter for GUI
from tkinter import ttk  # Importing ttk for Combobox
from googletrans import Translator,LANGUAGES # Importing Translator and LANGUAGES from googletrans

#This function will Translate the text
def change(text="type",src="english",dest="hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)

    return trans1.text

#This function will print the value at the destination
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END) # Get the text from the source text box
    textget = change(text=masg , src=s , dest=d) # Call the change function to translate the text
    dest_txt.delete(1.0,END) # Clear the destination text box
    dest_txt.insert(END,textget) # Insert the translated text into the destination text box




#Project UI
root = Tk()
root.title("Translator")
root.geometry("500x700")  # Corrected the geometry format
root.config(bg='Red')
root.resizable(False,False) # This command is used to fix the window size


lab_txt = Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg='White')
lab_txt.place(x=100,y=40,height=50,width=300)


frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg='black',bg='red')
lab_txt.place(x=100,y=100,height=20,width=300)


Sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,values=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")

#button to translate language
button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=200,y=300,height=40,width=100)

comb_dest = ttk.Combobox(frame,values=list_text)
comb_dest.place(x=330,y=300,height=40,width=160)
comb_dest.set("hindi")


lab_txt = Label(root,text="Dist Text",font=("Time New Roman",20,"bold"),fg='black',bg='red')
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()


#                                   Thank you sir/mam