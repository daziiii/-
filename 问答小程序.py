from tkinter import *


class basedesk():
    def __init__(self,master):
        self.root=master
        self.root.config()
        self.root.title("改成你程序的名字")
        self.root.geometry("400x350")
        initface(self.root)

class initface():
    def __init__(self,master):
        self.master=master
        self.master.config()
        self.initface=Frame(self.master)
        self.initface.pack()
        
        self.photo=PhotoImage(file='改成你所加图片的文件名，xxx.gif')#注意这个照片要gif格式，和py文件同一文件夹
        logo=Button(self.initface,image=self.photo,
                    cursor='heart',command=self.change)

        label0=Label(self.initface,text='改成界面上方的一行字',
                     bg='#fae3d9',fg='#1e2022',
                     font='TIMES 15 bold',
                     cursor='star')

        label1=Label(self.initface,text='账号',
                     bg='#fae3d9',fg='#1e2022',
                     width=4,
                     font='宋体 13 bold',
                     cursor='star')

        label2=Label(self.initface,text='密码',
                     bg='#fae3d9',fg='#1e2022',
                     width=4,
                     font='宋体 13 bold',
                     cursor='star')

        self.x=StringVar()
        message1=Entry(self.initface,textvariable=self.x,width=31)
        self.y=StringVar()
        message2=Entry(self.initface,textvariable=self.y,width=31,show='*')

        label0.grid(row=0,column=0,columnspan=2,padx=5,pady=10)
        logo.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        label1.grid(row=2,column=0,pady=10)
        message1.grid(row=2,column=1,pady=10)
        label2.grid(row=3,column=0,pady=0)
        message2.grid(row=3,column=1,pady=0)


    def change(self):
        if self.x.get()=='改成你所设置的账号' and self.y.get()=='改成你所设置的密码':
            self.initface.destroy()
            face0(self.master)

class face0():
    def __init__(self,master):
        self.master=master
        self.master.config(bg='#f0f0f0')
        self.face0=Frame(self.master)
        self.face0.pack()

        label=Label(self.face0,text='改成\n\n你要做的告示\n\n',#\n是用来给你的话换行的，相当于回车键的作用
                     bg='#bbded6',fg='#f8f3d4',
                     font='宋体 13 bold',cursor='star',
                     wraplength=300,justify='left',
                     padx=20,pady=20)
        btn=Button(self.face0,text='改成设置的按钮名字',command=self.back,
                   bg="#ffb6b9",cursor='heart',
                   font='宋体 13 bold',
                   padx=3,pady=3)
        label.grid(row=0,column=0,padx=20,pady=20)
        btn.grid(row=1,column=0,pady=10)
    def back(self):
        self.face0.destroy()
        face1(self.master)
    

class face1():
    def __init__(self,master):
        self.master=master
        self.master.config(bg='#f0f0f0')
        self.face1=Frame(self.master)
        self.face1.pack()

        label3=Label(self.face1,text='改成\n\n问题1\n\n',
                     bg='#bbded6',fg='#f8f3d4',
                     font='宋体 13 bold',cursor='star',
                     wraplength=300,justify='left',
                     padx=20,pady=20)
        btn=Button(self.face1,text='改成你要设置的按钮名字',command=self.back,
                   bg="#ffb6b9",cursor='heart',
                   font='宋体 13 bold',
                   padx=3,pady=3)
        self.z=StringVar()
        message3=Entry(self.face1,textvariable=self.z,width=20)
        
        label3.grid(row=0,column=0,columnspan=2,padx=10,pady=30)
        message3.grid(row=1,column=0,padx=10,pady=10)
        btn.grid(row=1,column=1,padx=10,pady=10)
    def back(self):
        if self.z.get()=='改成问题1的答案':
            self.face1.destroy()
            face2(self.master)

class face2():
    def __init__(self,master):
        self.master=master
        self.master.config(bg='#f0f0f0')
        self.face2=Frame(self.master)
        self.face2.pack()

        label=Label(self.face2,text='改成\n\n问题2\n\n',
                    bg='#bbded6',fg='#f8f3d4',
                    font='宋体 13 bold',cursor='star',
                    wraplength=300,justify='left',
                    padx=20,pady=20)
        btn=Button(self.face2,text='改成设置的按钮名字',command=self.back,
                   bg="#ffb6b9",cursor='heart',
                   font='宋体 13 bold',
                   padx=3,pady=3)
        self.a=StringVar()
        message3=Entry(self.face2,textvariable=self.a,width=20)
        
        label.grid(row=0,column=0,columnspan=2,padx=10,pady=30)
        message3.grid(row=1,column=0,padx=10,pady=10)
        btn.grid(row=1,column=1,padx=10,pady=10)
    def back(self):
        if self.a.get()=='改成问题2的答案':
            self.face2.destroy()
            face3(self.master)

class face3():
    def __init__(self,master):
        self.master=master
        self.master.config(bg='#f0f0f0')
        self.face3=Frame(self.master)
        self.face3.pack()

        label=Label(self.face3,text='改成\n\n问题3\n\n',
                    bg='#bbded6',fg='#f8f3d4',
                    font='宋体 13 bold',cursor='star',
                    wraplength=300,justify='left',
                    padx=20,pady=20)
        btn=Button(self.face3,text='改成设置的按钮名字',command=self.back,
                   bg="#ffb6b9",cursor='heart',
                   font='宋体 13 bold',
                   padx=3,pady=3)
        self.a=StringVar()
        message3=Entry(self.face3,textvariable=self.a,width=20)
        
        label.grid(row=0,column=0,columnspan=2,padx=10,pady=30)
        message3.grid(row=1,column=0,padx=10,pady=10)
        btn.grid(row=1,column=1,padx=10,pady=10)
    def back(self):
        if self.a.get()=='改成问题3的答案':
            self.face3.destroy()
            face4(self.master)

class face4():
    def __init__(self,master):
        self.master=master
        self.master.config(bg='#f0f0f0')
        self.face4=Frame(self.master)
        self.face4.pack()

        label=Label(self.face4,text=
                    '改成\n\n问题4\n\n',
                    bg='#bbded6',fg='#f8f3d4',
                    font='宋体 13 bold',cursor='star',
                    wraplength=300,justify='left',
                    padx=20,pady=20)
        btn=Button(self.face4,text='改成设置的按钮名字',command=self.back,
                   bg="#ffb6b9",cursor='heart',
                   font='宋体 13 bold',
                   padx=3,pady=3)
        self.a=StringVar()
        message3=Entry(self.face4,textvariable=self.a,width=20)
        
        label.grid(row=0,column=0,columnspan=2,padx=10,pady=30)
        message3.grid(row=1,column=0,padx=10,pady=10)
        btn.grid(row=1,column=1,padx=10,pady=10)
    def back(self):
        if self.a.get()=='改成问题4的答案':
            self.face4.destroy()
            face5(self.master)

class face5():
    def __init__(self,master):
        self.master=master
        self.master.config(bg='#f0f0f0')
        self.face5=Frame(self.master)
        self.face5.pack()

        label=Label(self.face5,text=
                    '改成\n\n问题5\n\n',
                    bg='#bbded6',fg='#f8f3d4',
                    font='宋体 13 bold',cursor='star',
                    wraplength=300,justify='left',
                    padx=20,pady=20)
        btn=Button(self.face5,text='改成设置的按钮名字',command=self.back,
                   bg="#ffb6b9",cursor='heart',
                   font='宋体 13 bold',
                   padx=3,pady=3)
        self.a=StringVar()
        message3=Entry(self.face5,textvariable=self.a,width=20)
        
        label.grid(row=0,column=0,columnspan=2,padx=10,pady=30)
        message3.grid(row=1,column=0,padx=10,pady=10)
        btn.grid(row=1,column=1,padx=10,pady=10)
    def back(self):
        if self.a.get()=='改成问题5的答案':
            self.face5.destroy()
            face6(self.master)

class face6():
    def __init__(self,master):
        self.master=master
        self.master.config(bg='#f0f0f0')
        self.face6=Frame(self.master)
        self.face6.pack()

        label=Label(self.face6,text=
                    '改成\n\n问题6\n\n',
                    bg='#bbded6',fg='#f8f3d4',
                    font='宋体 13 bold',cursor='star',
                    wraplength=300,justify='left',
                    padx=20,pady=20)
        btn=Button(self.face6,text='改成设置的按钮名字',command=self.back,
                   bg="#ffb6b9",cursor='heart',
                   font='宋体 13 bold',
                   padx=3,pady=3)
        self.a=StringVar()
        message3=Entry(self.face6,textvariable=self.a,width=20)
        
        label.grid(row=0,column=0,columnspan=2,padx=10,pady=30)
        message3.grid(row=1,column=0,padx=10,pady=10)
        btn.grid(row=1,column=1,padx=10,pady=10)
    def back(self):
        if self.a.get()=='改成问题6的答案':
            self.face6.destroy()
            face7(self.master)

class face7():
    def __init__(self,master):
        self.master=master
        self.master.config(bg='#f0f0f0')
        self.face7=Frame(self.master)
        self.face7.pack()

        label=Label(self.face7,text=
                    '改成\n\n问题7\n\n',
                    bg='#bbded6',fg='#f8f3d4',
                    font='宋体 13 bold',cursor='star',
                    wraplength=300,justify='left',
                    padx=20,pady=20)
        btn=Button(self.face7,text='改成设置的按钮名字',command=self.back,
                   bg="#ffb6b9",cursor='heart',
                   font='宋体 13 bold',
                   padx=3,pady=3)
        self.a=StringVar()
        message3=Entry(self.face7,textvariable=self.a,width=20)
        
        label.grid(row=0,column=0,columnspan=2,padx=10,pady=30)
        message3.grid(row=1,column=0,padx=10,pady=10)
        btn.grid(row=1,column=1,padx=10,pady=10)
    def back(self):
        if self.a.get()=='改成问题7的答案':
            self.face7.destroy()
            face8(self.master)

class face8():
    def __init__(self,master):
        self.master=master
        self.master.config(bg='#f0f0f0')
        self.face8=Frame(self.master)
        self.face8.pack()

        label=Label(self.face8,text='改成最后你想说的话',
                     bg='#bbded6',fg='#f8f3d4',
                     font='宋体 13 bold',cursor='star',
                     wraplength=350,justify='left',
                     padx=20,pady=20)
        btn=Button(self.face8,text='改成返回按钮的名字',command=self.back,
                   bg="#ffb6b9",cursor='heart',
                   font='宋体 13 bold',
                   padx=3,pady=3)
        label.grid(row=0,column=0,padx=10,pady=20)
        btn.grid(row=1,column=0,pady=10)

    def back(self):
        self.face8.destroy()
        initface(self.master)

if __name__=='__main__':
    root=Tk()
    basedesk(root)
    root.mainloop()
