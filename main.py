""" Fazer type hinting e abstrações maiores no define_x e pegafuncao e testar no pycharm
    arrumar o caso dos valores errados < 0 para log e outros para n bugar a tela
    tentar fazer a seleção por setas do teclado
"""

import tkinter as tk
import ttkbootstrap as ttkb
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

global comeca, termina, num


def theme_definition_window():
    def main_window(value):
        if value == '1':
            theme = 'yeti'
        elif value == '2':
            theme = 'cyborg'
        elif value == '3':
            theme = 'morph'
        elif value == '4':
            theme = 'vapor'

        window = ttkb.Window(themename=theme)
        window.iconbitmap('capivara.ico')

        # window.iconbitmap("")
        window.title("Gráficos")
        window.resizable(False, False)

        window_width1 = 600
        window_height1 = 520

        screen_width2 = window.winfo_screenwidth()
        screen_height2 = window.winfo_screenheight()

        posx2 = (screen_width2 // 2) - (window_width1 // 2)
        posy2 = (screen_height2 // 2) - (window_height1 // 2)

        # Define a posição da janela
        window.geometry('{}x{}+{}+{}'.format(window_width1, window_height1, posx2, posy2))

        def define_x(func):
            if func == '5':
                def salvar_valores() -> None:
                    if(float(value1.get()) < 0 or float(value2.get()) < 0 or float(value3.get()) < 0):
                        tk.Label(window, text="Valores <= 0 não são aceitos.", font=('Courier', 8, 'bold'), padx=2, pady=2).pack()
                    else:
                        global comeca, termina, num

                        comeca = float(value1.get())
                        termina = float(value2.get())
                        num = int(value3.get())

                        tk.Label(window, text="Salvo!", font=('Courier', 8, 'bold'), padx=2, pady=2).pack()

                for widget in window.winfo_children():
                    widget.destroy()

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Agora digite os valores dos pontos, no eixo X:", font=('Courier', 15, 'bold'),
                      padx=2,
                      pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="(começam / terminam / quantos são)", font=('Courier', 15, 'bold'), padx=2,
                      pady=2).pack()
                tk.Label(window, text="ex: 0.1 / 5 / 100", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Obs: Para log, x > 0.  ", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()

                value1 = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=7)
                value1.pack(padx=2, pady=2)

                value2 = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=7)
                value2.pack(padx=2, pady=2)

                value3 = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=7)
                value3.pack(padx=2, pady=2)

                ttkb.Button(window, text='Salvar', bootstyle='success', width=10, command=salvar_valores).pack(padx=2,
                                                                                                               pady=2)
                ttkb.Button(window, text='Gráfico', bootstyle='success', width=10,
                            command=lambda: pega_funcao(func)).pack(
                    padx=2, pady=6)
            elif func == '6':
                def salvar_valores() -> None:
                    global comeca, termina, num

                    comeca = float(value1.get())
                    termina = float(value2.get())
                    num = int(value3.get())

                    ttkb.Label(window, text="Salvo!", font=('Courier', 8, 'bold')).pack(padx=2, pady=2)

                for widget in window.winfo_children():
                    widget.destroy()

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Agora digite os valores dos pontos (EM GRAUS), no eixo X:",
                      font=('Courier', 12, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="(começam / terminam / quantos são)", font=('Courier', 15, 'bold'), padx=2,
                      pady=2).pack()
                # Label(window, text="", font=('Courier', 12, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="ex: 0 / 360 / 100", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()

                value1 = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=7)
                value1.pack(padx=2, pady=2)

                value2 = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=7)
                value2.pack(padx=2, pady=2)

                value3 = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=7)
                value3.pack(padx=2, pady=2)

                ttkb.Button(window, text='Salvar', bootstyle='success', width=10, command=salvar_valores).pack(padx=2,
                                                                                                               pady=2)
                ttkb.Button(window, text='Gráfico', bootstyle='success', width=10,
                            command=lambda: pega_funcao(func)).pack(
                    padx=2, pady=6)
            else:
                def salvar_valores() -> None:
                    global comeca, termina, num

                    comeca = float(value1.get())
                    termina = float(value2.get())
                    num = int(value3.get())

                    ttkb.Label(window, text="Salvo!", font=('Courier', 8, 'bold')).pack(padx=2, pady=2)

                for widget in window.winfo_children():
                    widget.destroy()

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Agora digite os valores dos pontos, no eixo X:", font=('Courier', 15, 'bold'),
                      padx=2,
                      pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="(começam / terminam / quantos são)", font=('Courier', 15, 'bold'), padx=2,
                      pady=2).pack()
                tk.Label(window, text="ex: -5 / 5 / 100", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()

                value1 = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=7)
                value1.pack(padx=2, pady=2)

                value2 = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=7)
                value2.pack(padx=2, pady=2)

                value3 = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=7)
                value3.pack(padx=2, pady=2)

                ttkb.Button(window, text='Salvar', bootstyle='success', width=10, command=salvar_valores).pack(padx=2,
                                                                                                               pady=2)
                ttkb.Button(window, text='Gráfico', bootstyle='success', width=10,
                            command=lambda: pega_funcao(func)).pack(
                    padx=2, pady=6)

        def linear(a):
            for widget in window.winfo_children():
                widget.destroy()

            global comeca, termina, num
            x_values = np.linspace(comeca, termina, num)

            for widget in window.winfo_children():
                widget.destroy()

            y_values = [float(a) * float(x) for x in x_values]

            fig, ax = plt.subplots()  # Criar uma figura e eixo para o gráfico
            ax.plot(x_values, y_values)
            ax.set_xlabel('Abscissas')
            ax.set_ylabel('Ordenadas')
            ax.set_title('Gráfico da Função Linear')
            ax.grid(True)

            # Criar uma instância de FigureCanvasTkAgg
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()

            ttkb.Button(window, text='Reiniciar', bootstyle="success", width=15, command=main).pack(padx=2, pady=6)

        def afim(a, b):
            for widget in window.winfo_children():
                widget.destroy()

            global comeca, termina, num
            x_values = np.linspace(comeca, termina, num)

            for widget in window.winfo_children():
                widget.destroy()

            y_values = [(float(a) * float(x)) + float(b) for x in x_values]

            fig, ax = plt.subplots()  # Criar uma figura e eixo para o gráfico
            ax.plot(x_values, y_values)
            ax.set_xlabel('Abscissas')
            ax.set_ylabel('Ordenadas')
            ax.set_title('Gráfico da Função Afim')
            ax.grid(True)

            # Criar uma instância de FigureCanvasTkAgg
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()

            ttkb.Button(window, text='Reiniciar', bootstyle="success", width=15, command=main).pack(padx=2, pady=6)

        def quad(a, b, c):
            for widget in window.winfo_children():
                widget.destroy()

            global comeca, termina, num
            x_values = np.linspace(comeca, termina, num)

            for widget in window.winfo_children():
                widget.destroy()

            y_values = [((float(a) * (float(x) ** 2)) + (float(b) * float(x)) + float(c)) for x in x_values]

            fig, ax = plt.subplots()  # Criar uma figura e eixo para o gráfico
            ax.plot(x_values, y_values)
            ax.set_xlabel('Abscissas')
            ax.set_ylabel('Ordenadas')
            ax.set_title('Gráfico da Função Quadrática')
            ax.grid(True)

            # Criar uma instância de FigureCanvasTkAgg
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()

            ttkb.Button(window, text='Reiniciar', bootstyle="success", width=15, command=main).pack(padx=2, pady=6)

        def exp(a):
            for widget in window.winfo_children():
                widget.destroy()

            global comeca, termina, num
            x_values = np.linspace(comeca, termina, num)

            for widget in window.winfo_children():
                widget.destroy()

            y_values = [(float(a) ** float(x)) for x in x_values]

            fig, ax = plt.subplots()  # Criar uma figura e eixo para o gráfico
            ax.plot(x_values, y_values)
            ax.set_xlabel('Abscissas')
            ax.set_ylabel('Ordenadas')
            ax.set_title('Gráfico da Função Exponencial')
            ax.grid(True)

            # Criar uma instância de FigureCanvasTkAgg
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()

            ttkb.Button(window, text='Reiniciar', bootstyle="success", width=15, command=main).pack(padx=2, pady=6)

        def log(a):
            if(float(a) <= 1):
                tk.Label(window, text="Digite valores > 1 para a base.", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
            else:
                for widget in window.winfo_children():
                    widget.destroy()

                global comeca, termina, num
                x_values = np.linspace(comeca, termina, num)

                for widget in window.winfo_children():
                    widget.destroy()

                y_values = [float(np.log(x)) / float(np.log(float(a))) for x in x_values]

                fig, ax = plt.subplots()  # Criar uma figura e eixo para o gráfico
                ax.plot(x_values, y_values)
                ax.set_xlabel('Abscissas')
                ax.set_ylabel('Ordenadas')
                ax.set_title('Gráfico da Função Logaritmica')
                ax.grid(True)

                # Criar uma instância de FigureCanvasTkAgg
                canvas = FigureCanvasTkAgg(fig, master=window)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack()

                ttkb.Button(window, text='Reiniciar', bootstyle="success", width=15, command=main).pack(padx=2, pady=6)

        def trig(func):
            if func == '1':
                for widget in window.winfo_children():
                    widget.destroy()

                global comeca, termina, num
                x_values = np.linspace(comeca, termina, num)

                for widget in window.winfo_children():
                    widget.destroy()

                rad_values = (x_values * np.pi) / 180

                y_values = [np.sin(rad) for rad in rad_values]

                fig, ax = plt.subplots()  # Criar uma figura e eixo para o gráfico
                ax.plot(rad_values, y_values)
                ax.set_xlabel('Abscissas')
                ax.set_ylabel('Ordenadas')
                ax.set_title('Gráfico da Função Trigonométrica')
                ax.grid(True)

                # Criar uma instância de FigureCanvasTkAgg
                canvas = FigureCanvasTkAgg(fig, master=window)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack()

                ttkb.Button(window, text='Reiniciar', bootstyle="success", width=15, command=main).pack(padx=2, pady=6)
            elif func == '2':
                for widget in window.winfo_children():
                    widget.destroy()

                # global comeca, termina, num
                x_values = np.linspace(comeca, termina, num)

                for widget in window.winfo_children():
                    widget.destroy()

                rad_values = (x_values * np.pi) / 180

                y_values = [np.cos(rad) for rad in rad_values]

                fig, ax = plt.subplots()  # Criar uma figura e eixo para o gráfico
                ax.plot(rad_values, y_values)
                ax.set_xlabel('Abscissas')
                ax.set_ylabel('Ordenadas')
                ax.set_title('Gráfico da Função Trigonométrica')
                ax.grid(True)

                # Criar uma instância de FigureCanvasTkAgg
                canvas = FigureCanvasTkAgg(fig, master=window)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack()

                ttkb.Button(window, text='Reiniciar', bootstyle="success", width=15, command=main).pack(padx=2, pady=6)
            elif func == '3':
                for widget in window.winfo_children():
                    widget.destroy()

                # global comeca, termina, num
                x_values = np.linspace(comeca, termina, num)

                for widget in window.winfo_children():
                    widget.destroy()

                rad_values = (x_values * np.pi) / 180

                y_values = [np.tan(rad) for rad in rad_values]

                fig, ax = plt.subplots()  # Criar uma figura e eixo para o gráfico
                ax.plot(rad_values, y_values)
                ax.set_xlabel('Abscissas')
                ax.set_ylabel('Ordenadas')
                ax.set_title('Gráfico da Função Trigonométrica')
                ax.grid(True)

                # Criar uma instância de FigureCanvasTkAgg
                canvas = FigureCanvasTkAgg(fig, master=window)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack()

                ttkb.Button(window, text='Reiniciar', bootstyle="success", width=15, command=main).pack(padx=2, pady=6)

        def pega_funcao(op):
            # Limpar a janela antes de exibir o resultado
            for widget in window.winfo_children():
                widget.destroy()

            if op == '1':
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = ax |", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="> Digite o valor de a:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                a_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                a_entry.pack(padx=2, pady=2)

                # Botão para calcular a função linear
                ttkb.Button(window, text='Calcular', bootstyle="success", width=15,
                            command=lambda: linear(a_entry.get())).pack(padx=2, pady=2)
            elif op == '2':
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = ax + b |", font=('Courier', 15, 'bold'), padx=2,
                      pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()

                tk.Label(window, text="> Digite o valor de a:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                a_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                a_entry.pack(padx=2, pady=2)

                tk.Label(window, text="> Digite o valor de b:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                b_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                b_entry.pack(padx=2, pady=2)

                ttkb.Button(window, text='Calcular', bootstyle="success", width=10,
                            command=lambda: afim(a_entry.get(), b_entry.get())).pack(padx=2, pady=2)
            elif op == '3':
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = ax² + bx + c |", font=('Courier', 15, 'bold'), padx=2,
                      pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()

                tk.Label(window, text="> Digite o valor de a:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                a_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                a_entry.pack(padx=2, pady=2)

                tk.Label(window, text="> Digite o valor de b:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                b_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                b_entry.pack(padx=2, pady=2)

                tk.Label(window, text="> Digite o valor de c", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                c_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                c_entry.pack(padx=2, pady=2)

                ttkb.Button(window, text='Calcular', bootstyle="success", width=10,
                            command=lambda: quad(a_entry.get(), b_entry.get(), c_entry.get())).pack(padx=2, pady=2)
            elif op == '4':
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = a^x |", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="> Digite o valor de a:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                a_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                a_entry.pack(padx=2, pady=2)

                ttkb.Button(window, text='Calcular', bootstyle="success", width=10,
                            command=lambda: exp(a_entry.get())).pack(padx=2, pady=2)
            elif op == '5':
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = logax (log de x na base a) |", font=('Courier', 15, 'bold'),
                      padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Obs: Para log, a > 1.", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="> Digite o valor de a:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                a_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                a_entry.pack(padx=2, pady=2)

                ttkb.Button(window, text='Calcular', bootstyle="success", width=10,
                            command=lambda: log(a_entry.get())).pack(padx=2, pady=2)
            elif op == '6':
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = 1 - sen(x) 2 - cos(x) 3 - tg(x) |",
                      font=('Courier', 10, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="> Digite a opção de função:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                func_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                func_entry.pack(padx=2, pady=2)

                ttkb.Button(window, text='Calcular', bootstyle="success", width=10,
                            command=lambda: trig(func_entry.get())).pack(padx=2, pady=2)

        def main():
            def call2(event):
                if op.get() in {'1', '2', '3', '4', '5', '6'}:
                    define_x(op.get())
                else:
                    tk.Label(window, text="Tente novamente!", fg='blue', font=('Courier', 10, 'bold'), padx=2,
                          pady=2).pack()

            for widget in window.winfo_children():
                widget.destroy()

            tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="|| Obter Gráficos ||", fg='blue', font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="Qual o tipo da sua função?", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="1 - Linear", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="2 - Afim", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="3 - Quadrática", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="4 - Exponencial", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="5 - Logarítmica", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="6 - Trigonométrica", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()

            op = ttkb.Entry(window, bootstyle="danger", font=('Courier', 15, 'bold'), width=1)
            op.pack(padx=2, pady=2)

            op.bind('<Return>', call2)

            # ttkb.Button(window, text='Ok', bootstyle="success", width=5, command=lambda: define_x(op.get())).pack(
            #    padx=2,
            #    pady=2)

        main()

        window.mainloop()

    # Função para verificar se a opção está correta e chamar a main
    def call(event) -> None:
        opcao = tema.get()
        if opcao in {'1', '2', '3', '4'}:
            main_window(opcao)
        else:
            ttkb.Label(first_window, text="Tente novamente!", fg='blue', font=('Courier', 10, 'bold'), padx=2,
                  pady=2).pack()

    def on_closing1():
        if tk.messagebox.askokcancel("Fechar Aplicativo", "Já vai? :c"):
            first_window.destroy()

    first_window = ttkb.Window(themename='cyborg')
    first_window.iconbitmap('capivara.ico')

    first_window.protocol("WM_DELETE_WINDOW", on_closing1)

    first_window.title("Gráficos")
    first_window.resizable(False, False)

    width1 = 400
    height1 = 400

    width = first_window.winfo_screenwidth()
    height = first_window.winfo_screenheight()

    posx = (width // 2) - (width1 // 2)
    posy = (height // 2) - (height1 // 2)

    # Define a posição da janela
    first_window.geometry('{}x{}+{}+{}'.format(width1, height1, posx, posy))

    tk.Label(first_window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
    tk.Label(first_window, text="|| Escolha um tema ||", fg='blue', font=('Courier', 18, 'bold'), padx=2, pady=2).pack()
    tk.Label(first_window, text="  ", font=('Courier', 2, 'bold'), padx=2, pady=2).pack()
    tk.Label(first_window, text="1 - Claro", font=('Courier', 18, 'bold'), padx=2, pady=2).pack()
    tk.Label(first_window, text="2 - Escuro (atual)", font=('Courier', 18, 'bold'), padx=2, pady=2).pack()
    tk.Label(first_window, text="3 - Morph", font=('Courier', 18, 'bold'), padx=2, pady=2).pack()
    tk.Label(first_window, text="4 - Vapor", font=('Courier', 18, 'bold'), padx=2, pady=2).pack()

    tema = ttkb.Entry(first_window, bootstyle="dark", font=('Courier', 18, 'bold'), width=1)
    tema.pack(padx=2, pady=2)

    tema.bind('<Return>', call)

    tk.Label(first_window, text="Pressione Enter", font=('Courier', 10, 'bold'), padx=2, pady=2).pack()

    ttkb.Button(first_window, text='Ok', bootstyle="success", width=8, command=lambda:
              main_window(tema.get()))

    first_window.mainloop()


theme_definition_window()
