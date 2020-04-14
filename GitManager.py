from tkinter import *
import os
import git_funcs_GUI as Git
from tkinter import filedialog, simpledialog
from tkinter import messagebox as mb

dirPath=''


class MainPage(Tk):

    def __init__(self):
        super().__init__()
        # self.geometry('700x450')
        self.color1 = 'cyan'
        self.color2 = 'yellow'

        self.title('Git Repo')
        self['bg'] = self.color1
        self.addWidget()
        # if add is not None:
        self.getAddress()
        self.refresh()

    def addWidget(self):
        # title lable

        self.repoName = StringVar()
        Label(textvariable=self.repoName, font=('bold', 11), bg=self.color1).grid(row=0, column=0, columnspan=3)
        self.repoName.set('Repo :                          ', )

        # refresh btn
        Button(text='Refresh', command=self.refresh, font=('bold', 13), background=self.color2).grid(row=0, column=5,
                                                                                                     pady=10, padx=10)

        # to source
        Button(text='Push', command=self.push, font=('bold', 13), background=self.color2).grid(row=0, column=4, pady=10,
                                                                                               padx=10)

        # listbox
        self.scrollbar = Scrollbar()

        self.textBox = Text(yscrollcommand=self.scrollbar.set, height=8, width=70)
        self.textBox.grid(row=1, column=0, columnspan=10, padx=10, pady=10)

        self.scrollbar.config(command=self.textBox.yview)

        # comment btn

        Button(text='Commit', command=self.askCommit, font=('bold', 13), background=self.color2).grid(row=0, column=3,
                                                                                                      pady=10, padx=10)

    def refresh(self):
        msg = Git.status()
        self.populateBOX(msg)

    def askCommit(self):
        msg = simpledialog.askstring("Comment", "Add the comment Massage ")
        if msg is not None:
            msg1 = Git.add()
            msg2 = Git.commit(msg)
            self.populateBOX(msg2)

    def populateBOX(self, content):
        self.textBox.delete('1.0', END)
        self.textBox.insert(END, content)

    def push(self):
        link = simpledialog.askstring('url','remote repo')
        print(4)
        Git.add_remote(url=link)
        Git.push_all()


    def getAddress(self):
        self.GitPath = str(filedialog.askdirectory())
        os.chdir(self.GitPath)
        self.repoName.set('Repo : ' + self.GitPath)


class StartPage(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('440x200')
        self.color1 = 'cyan'
        self.color2 = 'yellow'

        self.title('Git Repo')
        self['bg'] = self.color1
        self.addWidget()

    def addWidget(self):
        Button(text='Create Local', bg=self.color2, command=self.createLocal).place(x=30, y=60, height=60, width=160)
        Button(text='Fork from origin', bg=self.color2, command=self.fork).place(x=230, y=60, height=60, width=160)
        #Button(text='Quit', bg=self.color2, command=self.quit).place(x=230, y=160, height=60, width=160)
        #Button(text='Open Folder', bg=self.color2, command=self.openFolder).place(x=30, y=160, height=60, width=160)

    def createLocal(self):
        
        path = filedialog.askdirectory()
        name = simpledialog.askstring('Name', 'Enter the name For Repo')
        os.chdir(path)
        Git.init(name)
        self.destroy()
        #path = os.getcwd()
        #MainPage().mainloop()
        #dirPath =path


    def fork(self):
        path = filedialog.askdirectory()
        link = simpledialog.askstring('Clone', 'Paste the Repo Link')
        os.chdir(path)
        out = Git.clone(link)
        if out:
            mb.showinfo('message', out)
        self.destroy()
        #path = os.getcwd()
        #MainPage().mainloop()
        #dirPath = path

    def openFolder(self):
        path = filedialog.askdirectory()
        self.quit()
        os.chdir(path)
        #MainPage().mainloop()
        dirPath=path

    def folderSelect(self):
        path = filedialog.askdirectory()
        print(path)



if __name__ == '__main__':
    StartPage().mainloop()
    MainPage().mainloop()

