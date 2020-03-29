from tkinter import *
from tkinter import messagebox
import Back_End


aalaa_designs = Tk()
aalaa_designs.geometry('1300x630')
aalaa_designs.title("Aalaa Designs")
aalaa_designs.config(bg="ghost white")
Name=StringVar()
Date=StringVar()
cde=StringVar()
Address=StringVar()
Mobile=StringVar()
wight=StringVar()
length=StringVar()
orderr=StringVar()
history=StringVar()

######Frames######
#This is the main frame
Mainframe=Frame(aalaa_designs, bg="deep sky blue")
Mainframe.grid()


titleframe=Frame(Mainframe, bd=1, padx=518,pady=10, bg="deep sky blue",relief= RIDGE)
titleframe.pack(side=TOP)


aalaa_designs.lbltit=Label(titleframe,text='Aalaa Designs', font=('arial',30,'bold'),bg='deep sky blue')
aalaa_designs.lbltit.grid()

#This frame contains the Buttons
Dataframe=Frame(Mainframe, bd=1,width=1,height=-40, padx=0,pady=2, bg="deep sky blue",relief= RIDGE)
Dataframe.pack(side=BOTTOM)

#This frame contains the inputs
DataframeLeft=LabelFrame(Mainframe, bd=1,width=1,height=1, padx=25,pady=43 ,bg="deep sky blue",font=('arial',20,'bold'),border=2,text='Customer information')
DataframeLeft.pack(side=LEFT)

#This frame displays the data
DataframeRight=LabelFrame(Mainframe, bd=1,width=1,height=1, padx=1,pady=63, bg="deep sky blue",font=('arial',20,'bold'),text='Customer Details')
DataframeRight.pack(side=LEFT)


######Labels######

#Here is the labels of the data entry and the positions of them
aalaa_designs.lblname=Label(DataframeLeft,font=('arial',20,'bold'),text='Customer Name:', padx=2,pady=2, bg="deep sky blue")
aalaa_designs.lblname.grid(row=0,column=0,sticky=W)
aalaa_designs.txtname=Entry(DataframeLeft,font=('arial',20,'bold'),textvariable=Name,width=39, bg="deep sky blue")
aalaa_designs.txtname.grid(row=0,column=1,sticky=W)

aalaa_designs.lblDate=Label(DataframeLeft,font=('arial',20,'bold'),text='Date:', padx=2,pady=2, bg="deep sky blue")
aalaa_designs.lblDate.grid(row=1,column=0,sticky=W)
aalaa_designs.txtDate=Entry(DataframeLeft,font=('arial',20,'bold'),textvariable=Date,width=39, bg="deep sky blue")
aalaa_designs.txtDate.grid(row=1,column=1,sticky=W)

aalaa_designs.lblcde=Label(DataframeLeft,font=('arial',20,'bold'),text='Order Code:', padx=2,pady=2, bg="deep sky blue")
aalaa_designs.lblcde.grid(row=2,column=0,sticky=W)
aalaa_designs.txtcde=Entry(DataframeLeft,font=('arial',20,'bold'),textvariable=cde,width=39, bg="deep sky blue")
aalaa_designs.txtcde.grid(row=2,column=1,sticky=W)

aalaa_designs.lbladdress=Label(DataframeLeft,font=('arial',20,'bold'),text='Address:', padx=2,pady=2, bg="deep sky blue")
aalaa_designs.lbladdress.grid(row=3,column=0,sticky=W)
aalaa_designs.txtaddress=Entry(DataframeLeft,font=('arial',20,'bold'),textvariable=Address,width=39, bg="deep sky blue")
aalaa_designs.txtaddress.grid(row=3,column=1,sticky=W)

aalaa_designs.lblmobile=Label(DataframeLeft,font=('arial',20,'bold'),text='Mobile Number:', padx=2,pady=2, bg="deep sky blue")
aalaa_designs.lblmobile.grid(row=4,column=0,sticky=W)
aalaa_designs.txtmobile=Entry(DataframeLeft,font=('arial',20,'bold'),textvariable=Mobile,width=39, bg="deep sky blue")
aalaa_designs.txtmobile.grid(row=4,column=1,sticky=W)

aalaa_designs.lblwight=Label(DataframeLeft,font=('arial',20,'bold'),text='Wight:', padx=2,pady=2, bg="deep sky blue")
aalaa_designs.lblwight.grid(row=5,column=0,sticky=W)
aalaa_designs.txtwight=Entry(DataframeLeft,font=('arial',20,'bold'),textvariable=wight,width=39, bg="deep sky blue")
aalaa_designs.txtwight.grid(row=5,column=1,sticky=W)

aalaa_designs.lbllength=Label(DataframeLeft,font=('arial',20,'bold'),text='Length:', padx=2,pady=2, bg="deep sky blue")
aalaa_designs.lbllength.grid(row=6,column=0,sticky=W)
aalaa_designs.txtlength=Entry(DataframeLeft,font=('arial',20,'bold'),textvariable=length,width=39, bg="deep sky blue")
aalaa_designs.txtlength.grid(row=6,column=1,sticky=W)

aalaa_designs.lblorderr=Label(DataframeLeft,font=('arial',20,'bold'),text='Order:', padx=2,pady=2, bg="deep sky blue")
aalaa_designs.lblorderr.grid(row=7,column=0,sticky=W)
aalaa_designs.txtorderr=Entry(DataframeLeft,font=('arial',20,'bold'),textvariable=orderr,width=39, bg="deep sky blue")
aalaa_designs.txtorderr.grid(row=7,column=1,sticky=W)

aalaa_designs.txthistory=Entry(DataframeLeft,font=('arial',20,'bold'),textvariable=history,width=39, bg="deep sky blue")
aalaa_designs.txthistory.grid(row=8,column=1,sticky=W)
aalaa_designs.lblhistory=Label(DataframeLeft,font=('arial',20,'bold'),text='History:', padx=2,pady=2, bg="deep sky blue")
aalaa_designs.lblhistory.grid(row=8,column=0,sticky=W)







######Patien Data####

#Records
def customer__rec(event):
    global pd
    searchpt=customerlist.curselection()[0]
    pd=customerlist.get(searchpt)
    
    aalaa_designs.txtname.delete(0,END)
    aalaa_designs.txtname.insert(END,pd[1])
    aalaa_designs.txtcde.delete(0,END)
    aalaa_designs.txtcde.insert(END,pd[2])
    aalaa_designs.txtDate.delete(0,END)
    aalaa_designs.txtDate.insert(END,pd[3])
    aalaa_designs.txtaddress.delete(0,END)
    aalaa_designs.txtaddress.insert(END,pd[4])
    aalaa_designs.txtmobile.delete(0,END)
    aalaa_designs.txtmobile.insert(END,pd[5])
    aalaa_designs.txtwight.delete(0,END)
    aalaa_designs.txtwight.insert(END,pd[6])
    aalaa_designs.txtlength.delete(0,END)
    aalaa_designs.txtlength.insert(END,pd[7])
    aalaa_designs.txtorderr.delete(0,END)
    aalaa_designs.txtorderr.insert(END,pd[8]) 
    aalaa_designs.txthistory.delete(0,END)
    aalaa_designs.txthistory.insert(END,pd[9])    





######scrollbar######


#scrollbar position

scrollbar=Scrollbar(DataframeRight)
scrollbar.grid(row=0 ,column=1,sticky=NS)

customerlist=Listbox(DataframeRight, width=41,height=16,font=('arial',12,'bold'),fg='black',bg="deep sky blue",yscrollcommand=scrollbar.set)
customerlist.bind('<<ListboxSelect>>',customer__rec)
customerlist.grid(row=0 ,column=0,padx=1)
scrollbar.config(command=customerlist.yview)



######functions######

#This is the functions of the Buttons

def iExit():
    iExit=messagebox.askyesno("Exit","Are you sure you want to exit?")
    if iExit < 1:
        return 0
    aalaa_designs.destroy()
    return

def clear_Data():
    aalaa_designs.txtname.delete(0,END)
    aalaa_designs.txtcde.delete(0,END)
    aalaa_designs.txtDate.delete(0,END)
    aalaa_designs.txtaddress.delete(0,END)
    aalaa_designs.txtmobile.delete(0,END)
    aalaa_designs.txtwight.delete(0,END)
    aalaa_designs.txtlength.delete(0,END)
    aalaa_designs.txtorderr.delete(0,END)
    aalaa_designs.txthistory.delete(0,END)
    


def add_Data():
    if (len(Name.get())!=0) :
        Back_End.add_pt_data(Name.get(),cde.get(),Date.get(),Address.get(),Mobile.get(),wight.get(),length.get(),orderr.get(),history.get())
        customerlist.delete(0,END)
        customerlist.insert(END,Name.get(),cde.get(),Date.get(),Address.get(),Mobile.get(),wight.get(),length.get(),orderr.get(),history.get())
    

def display_data():
    customerlist.delete(0,END)
    for row in Back_End.viewptdata():
        customerlist.insert(END,row,str(""))
    

def delete_data():
    if (len(Name.get()) !=0) :
        Back_End.deletedata(pd[0])
        clear_Data()
        display_data()


def search_db():
    customerlist.delete(0,END)
    for row in Back_End.searchdata(Name.get(),cde.get(),Date.get(),Address.get(),Mobile.get(),wight.get(),length.get(),orderr.get(),history.get()):
        customerlist.insert(END,row,str(""))



def update_data():
    if(len(Name.get()) !=0):
        Back_End.deletedata(pd[0])
    if(len(Name.get() )!=0):
        Back_End.updatedata(Name.get(),cde.get(),Date.get(),Address.get(),Mobile.get(),wight.get(),length.get(),orderr.get(),history.get())
        customerlist.delete(0,END)
        customerlist.insert(END,Name.get(),cde.get(),Date.get(),Address.get(),Mobile.get(),wight.get(),length.get(),orderr.get(),history.get())
        



######Buttons######
#This is the buttons positions and styles

Addnewbut = Button(Dataframe, text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,command=add_Data )
Addnewbut.grid(row=0, column=0)

Updatebut = Button(Dataframe, text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,command=update_data)
Updatebut.grid(row=0, column=1)

Displaybut = Button(Dataframe, text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=display_data)
Displaybut.grid(row=0, column=2)

Clearbut = Button(Dataframe, text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4, command=clear_Data)
Clearbut.grid(row=0, column=3)

Deletebut = Button(Dataframe, text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=delete_data)
Deletebut.grid(row=0, column=4)

searchbut = Button(Dataframe, text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,command=search_db)
searchbut.grid(row=0, column=5)

Exit = Button(Dataframe,font=('arial',20,'bold'),height=1,width=10,bd=4,text="Exit", command=iExit)
Exit.grid(row=0, column=6)





aalaa_designs.mainloop()