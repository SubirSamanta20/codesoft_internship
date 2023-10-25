from tkinter import*
from tkinter.font import Font 
from tkinter import filedialog
import pickle


root=Tk()
root.title("my to do list")
root.iconbitmap("C:/icon/list.ico")
root.geometry("600x500")

# defining font'
my_font=Font(family="Stencil Regular",
             size=30,
             weight="bold")


# frame
my_frame=LabelFrame(root)
my_frame.pack(padx=10,pady=10)


# listbox
my_list=Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="white",
    bd=0,
    fg="gray",
    highlightthickness=0,
    selectbackground="skyblue",
    activestyle="none"
    
    )

my_list.pack(side=LEFT,fill=BOTH)

# list=["jogging","breakfast","apptitude","shower","lunch","take a nap","coding session","apptitude","dsa","dinner","sleep"]
# for item in list:
#     my_list.insert(END,item)

# scroll bar
my_scrollbar=Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)


my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# entry box
my_entry=Entry(root,font=("helvatica",24),width=30)
my_entry.pack(pady=20)

# Menu
def save_list():
    file_name=filedialog.asksaveasfilename(
        initialdir="C:\data",
        title="save files",
        filetypes=(("dat files","*.dat"),("all files","*.*")))
    
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name=f"{file_name}.dat"

    stuff=my_list.get(0,END)

    output_file=open(file_name,"wb")

    pickle.dump(stuff,output_file)

def open_list():
    file_name=filedialog.askopenfilename(initialdir="C:\data",
        title="open files",
        filetypes=(("dat files","*.dat"),("all files","*.*"))
        )
    if file_name:
        my_list.delete(0,END)

        input_file=open(file_name,"rb")

        stuff=pickle.load(input_file)

        for item in stuff:
            my_list.insert(END,item)

def delete_list():
    my_list.delete(0,END)

my_menu=Menu(root)
root.config(menu=my_menu)

file_menu=Menu(my_menu,tearoff=FALSE)
my_menu.add_cascade(label="file",menu=file_menu)


file_menu.add_command(label="save list",command=save_list)
file_menu.add_command(label="open list",command=open_list)
file_menu.add_separator()
file_menu.add_command(label="delete list",command=delete_list)



# button
button_frame=Frame(root)
button_frame.pack(pady=20)

def delete_button():
    my_list.delete(ANCHOR)

def add_button():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)


delete=Button(button_frame,text="delete item",command=delete_button)
add=Button(button_frame,text="add item",command=add_button)


delete.grid(row=0,column=0,padx=10)
add.grid(row=0,column=2)




root.mainloop() 