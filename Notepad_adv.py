from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename as afn, asksaveasfilename as asf
import os

class GUI(Tk):
    def __init__(self):
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        global file
        super().__init__()
        self.geometry("744x466")
        self.title("Untitled - Notepad Adv")
        self.wm_iconbitmap(icon_path)
        self.text = Text(self, font="Cambria 13", bg = '#121212', fg = "white")
        file = None
        self.text.pack(fill="both", expand=True)
        self.sidebar(self.text)

    #BackEnd Functions

    def status(self):
        self.version = StringVar(value = '1.10.01')
        self.filename = StringVar(value = "Untitled - Notepad Adv")

        bar_frame = Frame(self)
        bar_frame.config(bg = "#323232")
        bar_frame.pack(side ="bottom", fill = 'x')

        self.file_name = Label(bar_frame, text = f'Current file:  {self.filename.get()}',
                          bg = "#323232", pady = 6, fg = "grey",
                          font = "lucida 9", padx = 18)
        version_bar = Label(bar_frame, text = f"Version {self.version.get()}",
                            bg = "#323232", fg = "grey", pady = 6,
                            padx = 18)

        version_bar.pack(side = 'right')
        self.file_name.pack(side ="left")

    #FileMenu Bar

    def newfile(self):
        global file
        if self.text.get(1.0,END).strip():
            answer = msg.askyesno("Save", "Want to save current changes?")
            if answer:
                file = None
                file = asf(initialfile="Untitled.txt",
                           defaultextension=".text",
                           filetypes=[("All Files", "*.*"), ("Text Documents", '*.txt')])
            else:
                self.title("Untitled - Notepad Adv")
                self.text.delete(1.0, END)



    def openfile(self):
        global file
        file = afn(defaultextension = ".txt",
                   filetypes = [("All Files", "*.*"),
                                ("Text Documents","*.txt")])
        self.filename.set(os.path.basename(file))
        self.file_name.config(text=f"Current file: {self.filename.get()}")

        if file == "":
            file = None
        else:
            self.title(os.path.basename(file) + " - Notepad Adv")
            self.text.delete(1.0, END)
            x = open(file, "r")
            self.text.insert(1.0, x.read())



    def savefile(self):
        global file
        if file is None:
            file = asf(initialfile = "Untitled.txt", defaultextension = ".txt",
                       filetypes= [("All Files", "*.*"),
                                   ("text Document", "*.txt")])
            self.filename.set(os.path.basename(file))
            self.file_name.config(text=f"Current file: {self.filename.get()}")
        else:
            f = open(file, "w")
            f.write(self.text.get(1.0, END))
            f.close()

        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(self.text.get(1.0,END))
            f.close()

            self.title(os.path.basename(file) + " - Notepad Adv")


    def exitfile(self):
        self.destroy()

    #ToolMenu Bar

    def cut(self):
        self.text.event_generate("<<Cut>>")


    def copy(self):
        self.text.event_generate("<<Copy>>")


    def paste(self):
        self.text.event_generate("<<Paste>>")


    def darkmode(self):
        current_bg = self.text['bg']
        if current_bg == "white":
            self.title("Notepad Adv(Dark)")
            self.text.config(bg = "#121212", fg = "white")
        else:
            self.title("Notepad Adv")
            self.text.config(bg = "white", fg = "black")


    #FormatMenu bar

    def format(self):
        lstbox = Listbox(self)
        items = ["arial","cambria","helvetica", "lucida"]
        for i in items:
            lstbox.insert(self.END, i)


    def newfont(self):
        pass #Size of font

    #HelpMenu Bar


    def helpme(self):
        user = msg.askyesno("Help", "Is there any bug in the current window?")
        if user:
            msg.showinfo("Contact",
                         "Sorry for the inconvenience incurred while using the application.")
            msg.showinfo("Contact",
                         "Please contact to helpline number +91 8416913845 for further assistance")
        else:
            msg.showinfo("Help",
                         "Please contact to helpline number +91 8416913845 for further assistance")



    def about(self):
        msg.showinfo("About Us", "This is tkinter based adv-notepad by shreyash")


    #MainFunctions


    def menubar(self):
        mainmenu = Menu(self)
        filemenu = Menu(mainmenu, tearoff = 0)
        filemenu.add_command(label = "New", command = self.newfile)
        filemenu.add_command(label = "Open", command = self.openfile)
        filemenu.add_separator()
        filemenu.add_command(label = "Save", command = self.savefile)
        filemenu.add_command(label = "Exit", command = self.exitfile)

        mainmenu.add_cascade(menu = filemenu, label = "File")

        editmenu = Menu(mainmenu, tearoff = 0)
        editmenu.add_command(label = "Cut", command= self.cut)
        editmenu.add_command(label = "Copy", command= self.copy)
        editmenu.add_command(label = "Paste", command= self.paste)
        editmenu.add_command(label = "Switch Mode", command= self.darkmode)

        mainmenu.add_cascade(menu = editmenu, label = "Tools")

        #Formatmenu Bar

        formatmenu = Menu(mainmenu)
        formatmenu.add_command(label = "Font", command = self.newfont)
        formatmenu.add_command(label = "Format", command= self.format)

        mainmenu.add_cascade(menu = formatmenu, label = "Format")


        helpmenu = Menu(mainmenu, tearoff =0)
        helpmenu.add_command(label = "Help", command = self.helpme)
        helpmenu.add_command(label = "About Notepad", command = self.about)

        mainmenu.add_cascade(menu = helpmenu, label = "Help")

        self.config(menu = mainmenu)



    def sidebar(self, text):

        scroll = Scrollbar(text)
        scroll.pack(side= "right", fill = "y")

        scroll.config(command = text.yview)
        text.config(yscrollcommand = scroll.set)



if __name__ == "__main__":
    window = GUI()
    window.status()
    window.menubar()

    window.mainloop()