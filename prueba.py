import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
from tkPDFViewer import tkPDFViewer as pdf
import tkinter as ttk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import PhotoImage
import tkinter
import os
from PIL import ImageTk,Image
count = 0
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Inicio", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Informacion",
                            command=lambda: controller.show_frame("PageOne"),width=30,height=5)
        button2 = tk.Button(self, text="Quiz",
                            command=lambda: controller.show_frame("PageTwo"),width=20,height=4)
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Informacion", font=controller.title_font)
        label.pack(side="top", fill="x", pady=5)
        button = tk.Button(self, text="Ir a inicio",command=lambda: controller.show_frame("StartPage"))
        button.pack()

        v1 = pdf.ShowPdf() 
        v2 = v1.pdf_view(self, pdf_location = r"variable.pdf", width = 80, height = 80) 
        v2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Quiz", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Ir a inicio",command=lambda: controller.show_frame("StartPage"))
        button.pack()

        main_frame=Frame(self)
        main_frame.pack(fill=BOTH,expand=1)

        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame=Frame(my_canvas)

        my_canvas.create_window((0,0),window=second_frame,anchor="nw")

        page_1 = tk.Frame(second_frame)
        page_1_lb = tk.Label(page_1, text='1. ??Cu??l es el concepto dentro de las matem??ticas que la mayor??a de los estudiantes les es dif??cil comprender, pero es de gran importancia en su ense??anza?', font=('Bold', 12))
        page_1_lb.pack()
        
        #boton1=Button(page_1,text=f'Button',bg='#C4A580')
        boton1=Button(page_1,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_1,text="Numero general")
        lbq1.pack()

        boton2=Button(page_1,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_1,text="Variable")
        lbq2.pack()

        boton2=Button(page_1,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_1,text="Inc??gnita especifica")
        lbq2.pack()

        boton2=Button(page_1,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_1,text="Relaci??n funcional")
        lbq2.pack()
        page_1.pack(pady=100)

        page_2 = tk.Frame(second_frame)

        page_1_lb = tk.Label(page_2, text='2. ??C??mo se conoce a la variable cuando la existencia de algo desconocido puede determinar cu??ndo se simboliza y comprueba dicho resultado?', font=('Bold', 12))
        page_1_lb.pack()
        
        boton1=Button(page_2,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_2,text="Literal")
        lbq1.pack()

        boton2=Button(page_2,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_2,text="Expresi??n algebraica")
        lbq2.pack()

        boton2=Button(page_2,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_2,text="Numero general")
        lbq2.pack()

        boton2=Button(page_2,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_2,text="Inc??gnita especifica")
        lbq2.pack()

        page_3 = tk.Frame(second_frame)

        page_1_lb = tk.Label(page_3, text='3. ??Cu??l de los siguientes incisos corresponde a 2 implicaciones verdaderas sobre la variable inc??gnita especifica?', font=('Bold', 12))
        page_1_lb.pack()
        
        boton1=Button(page_3,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_3,text="Reconocer patrones y reglas")
        lbq1.pack()

        boton2=Button(page_3,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_3,text="Interpretar el s??mbolo")
        lbq2.pack()

        boton2=Button(page_3,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_3,text="Expresar una relaci??n funcional")
        lbq2.pack()

        boton2=Button(page_3,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_3,text="s??mbolo que aparece en una ecuaci??n")
        lbq2.pack()

        page_4 = tk.Frame(second_frame)
        page_1_lb = tk.Label(page_4, text='4. ??Cu??l de los siguientes ejemplos puede resolverse con ayuda de la inc??gnita especifica?', font=('Bold', 12))
        page_1_lb.pack()
        
        boton1=Button(page_4,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_4,text="Creaci??n de tabla con valores")
        lbq1.pack()

        boton2=Button(page_4,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_4,text="Reducir t??rminos semejantes")
        lbq2.pack()

        boton2=Button(page_4,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_4,text="Ecuaci??n 8x+19=139")
        lbq2.pack()

        boton2=Button(page_4,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_4,text=" Desarrollar la expresi??n: (x+7)(x???3)+2x")
        lbq2.pack()


        page_5 = tk.Frame(second_frame)
        page_1_lb = tk.Label(page_5, text='5. ??Qu?? tipo de variable abarca la interpretaci??n de una literal como la representaci??n de un n??mero, el reconocimiento de patrones y deducci??n de m??todos generales?', font=('Bold', 12))
        page_1_lb.pack()
        
        boton1=Button(page_5,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_5,text=" Variable como n??mero general")
        lbq1.pack()

        boton2=Button(page_5,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_5,text="Inc??gnita especifica")
        lbq2.pack()

        boton2=Button(page_5,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_5,text="Cuantitativa")
        lbq2.pack()

        boton2=Button(page_5,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_5,text=" Relaci??n funcional")
        lbq2.pack()

        page_6 = tk.Frame(second_frame)
        page_1_lb = tk.Label(page_6, text='6. ??Cu??l de los siguientes incisos corresponde a 2 implicaciones verdaderas sobre la variable como numero general?', font=('Bold', 12))
        page_1_lb.pack()
        
        boton1=Button(page_6,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_6,text="Reconocer patrones y reglas")
        lbq1.pack()

        boton2=Button(page_6,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_6,text="Determinar la inc??gnita")
        lbq2.pack()

        boton2=Button(page_6,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_6,text="Diferenciar entre los valores conocidos")
        lbq2.pack()

        boton2=Button(page_6,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_6,text="Desarrollar la idea de m??todo general")
        lbq2.pack()


        page_7 = tk.Frame(second_frame)
        page_1_lb = tk.Label(page_7, text='7. ??Cu??l de los siguientes ejemplos puede resolverse con ayuda de la interpretaci??n de una literal como la representaci??n de un numero?', font=('Bold', 12))
        page_1_lb.pack()
        
        boton1=Button(page_7,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_7,text="Creaci??n de tabla con valores")
        lbq1.pack()

        boton2=Button(page_7,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_7,text=" Desarrollar la expresi??n: (x+7)(x???3)+2x")
        lbq2.pack()

        boton2=Button(page_7,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_7,text="Ecuaci??n 8x+19=139")
        lbq2.pack()

        boton2=Button(page_7,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_7,text="Reducir t??rminos semejantes")
        lbq2.pack()


        page_8 = tk.Frame(second_frame)
        page_1_lb = tk.Label(page_8, text='8. ??Qu?? variable hace una referencia al reconocimiento de que existe una correspondencia entre los valores de las variables involucradas?', font=('Bold', 12))
        page_1_lb.pack()
        
        boton1=Button(page_8,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_8,text="Variable en relaci??n funcional")
        lbq1.pack()

        boton2=Button(page_8,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_8,text="Variable como n??mero general")
        lbq2.pack()

        boton2=Button(page_8,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_8,text="Cualitativa")
        lbq2.pack()

        boton2=Button(page_8,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_8,text=" Inc??gnita especifica")
        lbq2.pack()


        page_9 = tk.Frame(second_frame)
        page_1_lb = tk.Label(page_9, text='9. ??Cu??l de los siguientes incisos corresponde a 2 implicaciones verdaderas sobre la variable en relaci??n funcional?', font=('Bold', 12))
        page_1_lb.pack()
        
        boton1=Button(page_9,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_9,text="Interpretar el s??mbolo que aparece en una ecuaci??n")
        lbq1.pack()

        boton2=Button(page_9,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_9,text="Desarrollar la idea de m??todo general")
        lbq2.pack()

        boton2=Button(page_9,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_9,text="Determinar los valores de la variable")
        lbq2.pack()

        boton2=Button(page_9,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_9,text="Nombrar las variable o constantes")
        lbq2.pack()


        page_10 = tk.Frame(second_frame)
        page_1_lb = tk.Label(page_10, text='10. ??Qu?? tipo de variable abarca la interpretaci??n de una literal como la representaci??n de un n??mero, el reconocimiento de patrones y deducci??n de m??todos generales?', font=('Bold', 12))
        page_1_lb.pack()
        
        boton1=Button(page_10,bg='#F5B041',width=10,height=3)
        boton1.place(x=5,y=5)
        boton1.pack()
        lbq1=Label(page_10,text="Fibonacci (con los conejos)")
        lbq1.pack()

        boton2=Button(page_10,bg='#5DADE2',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_10,text="Ley de Pascal")
        lbq2.pack()

        boton2=Button(page_10,bg='#1ABC9C',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_10,text="Graficar coordenadas en plano cartesiano")
        lbq2.pack()

        boton2=Button(page_10,bg='#C70039',width=10,height=3)
        boton2.place(y=15,x=10)
        boton2.pack()
        lbq2=Label(page_10,text="Creaci??n de tabla con valores")
        lbq2.pack()


        page_11 = tk.Frame(second_frame)
        page_1_lb = tk.Label(page_11, text='RESULTADOS',font=('Bold', 18),fg='#1B4F72')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text='Variable')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text=' Inc??gnita espec??fica')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text='Interpretar el s??mbolo')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text='Ecuaci??n 8x + 19 = 139')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text='Variable como n??mero general')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text='Desarrollar la idea de m??todo general')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text='Desarrollar la expresi??n: (x+7)(x???3)+2x')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text='Variable en relaci??n funcional')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text='Determinar los valores de la variable')
        page_1_lb.pack()
        page_1_lb = tk.Label(page_11, text='Fibonacci')
        page_1_lb.pack()

        page_1_lb = tk.Label(page_11, text='Total: 9',font=('Bold', 18),fg='#1B4F72')
        page_1_lb.pack()

        btr = tk.Button(self, text="Reiniciar",command=lambda: controller.show_frame("StartPage"),bg = "#AED6F1")
        btr.pack()


        second_frame.pack(fill=tk.BOTH, expand=True)

        #pages variable of all the UI
        pages = [page_1, page_2, page_3, page_4,page_5,page_6,page_7,page_8,page_9,page_10,page_11]
        #count = 0

        def move_next_page():
            global count

            if not count > len(pages) - 2:

                for p in pages:
                    p.pack_forget()

            count += 1
            # counts how many pages
            page = pages[count]
            page.pack(pady=100)

        def move_back_page():

                global count

                if not count == 0:

                    for p in pages:
                        p.pack_forget()

                count -= 1
                # counts how many pages
                page = pages[count]
                page.pack(pady=100)



        bottom_frame = tk.Frame(second_frame)
        # back button UI,  command is using the move back page function
        back_btn = tk.Button(bottom_frame, text='<',font=('Bold', 12),bg='#F9F292', fg='black', width=8,command=move_back_page)
        back_btn.pack(side=tk.LEFT, padx=10)
        # next button UI, command is using the move next page function
        next_btn = tk.Button(bottom_frame, text='>',font=('Bold', 12),bg='#F9F292', fg='black', width=8,command=move_next_page)
        next_btn.pack(side=tk.RIGHT, padx=10)
        bottom_frame.pack(side=tk.BOTTOM, pady=10)
        
       

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()