""" Fazer type hinting e abstrações maiores no define_x e pegafuncao e testar no pycharm
    tentar fazer a seleção por setas do teclado
    - aplicar funcionalidades como y do vertice e x do vertice para a quadrática e as outras caso tenham
        - agora em todos
    -- adicionar histórico de gráficos feitos
"""

import tkinter as tk
from tkinter import messagebox
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
        window_height1 = 550

        screen_width2 = window.winfo_screenwidth()
        screen_height2 = window.winfo_screenheight()

        posx2 = (screen_width2 // 2) - (window_width1 // 2)
        posy2 = (screen_height2 // 2) - (window_height1 // 2)

        # Define a posição da janela
        window.geometry('{}x{}+{}+{}'.format(window_width1, window_height1, posx2, posy2))

        def define_x(func):
            if func == '5':
                def salvar_valores() -> None:
                    if value1.get() == '' or value3.get() == '' or value2.get() == '':
                        messagebox.showwarning(title="Error", message="Campos vazios!")
                    elif float(value1.get()) < 0 or float(value2.get()) < 0 or float(value3.get()) < 0:
                        messagebox.showwarning(title="Error", message="Valores <= 0 não são aceitos.")
                    else:
                        global comeca, termina, num

                        comeca = float(value1.get())
                        termina = float(value2.get())
                        num = int(value3.get())

                        tk.Label(window, text="Salvo!", font=('Courier', 14, 'bold'), padx=2, pady=2).pack()
                        ttkb.Button(window, text='Avançar', bootstyle='success', width=15,
                                    command=lambda: pega_funcao(func)).pack(padx=2, pady=6)

                for widget in window.winfo_children():
                    widget.destroy()

                ttkb.Button(window, text='Voltar', bootstyle='success', width=15, command=main).pack(padx=4, pady=4,
                                                                                                     anchor='nw')

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Agora digite os valores de X:", font=('Courier', 15, 'bold'),
                      padx=2,
                      pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="(começam / terminam / quantos são)", font=('Courier', 15, 'bold'), padx=2,
                      pady=2).pack()
                tk.Label(window, text="ex: 0.1 / 5 / 100", font=('Courier', 20, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Obs: Para log, x > 0.  ", font=('Courier', 20, 'bold'), padx=2, pady=2).pack()

                value1 = ttkb.Entry(window, font=('Courier', 20, 'bold'), width=7)
                value1.pack(padx=2, pady=2)

                value2 = ttkb.Entry(window, font=('Courier', 20, 'bold'), width=7)
                value2.pack(padx=2, pady=2)

                value3 = ttkb.Entry(window, font=('Courier', 20, 'bold'), width=7)
                value3.pack(padx=2, pady=2)

                ttkb.Button(window, text='Salvar', bootstyle='success', width=10, command=salvar_valores).pack(padx=2,
                                                                                                               pady=2)
            elif func == '6':
                def salvar_valores() -> None:
                    if value1.get() == '' or value3.get() == '' or value2.get() == '':
                        messagebox.showwarning(title="Error", message="Campos vazios!")
                    else:
                        global comeca, termina, num

                        comeca = float(value1.get())
                        termina = float(value2.get())
                        num = int(value3.get())

                        ttkb.Label(window, text="Salvo!", font=('Courier', 14, 'bold')).pack(padx=2, pady=2)
                        ttkb.Button(window, text='Avançar', bootstyle='success', width=15,
                                    command=lambda: pega_funcao(func)).pack(padx=2, pady=6)

                for widget in window.winfo_children():
                    widget.destroy()

                ttkb.Button(window, text='Voltar', bootstyle='success', width=15, command=main).pack(padx=4, pady=4,
                                                                                                     anchor='nw')

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Agora digite os valores de X:",
                      font=('Courier', 12, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="(começam / terminam / quantos são)", font=('Courier', 15, 'bold'), padx=2,
                      pady=2).pack()
                # Label(window, text="", font=('Courier', 12, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="ex: 0 / 360 / 100", font=('Courier', 20, 'bold'), padx=2, pady=2).pack()

                value1 = ttkb.Entry(window, font=('Courier', 20, 'bold'), width=7)
                value1.pack(padx=2, pady=2)

                value2 = ttkb.Entry(window, font=('Courier', 20, 'bold'), width=7)
                value2.pack(padx=2, pady=2)

                value3 = ttkb.Entry(window, font=('Courier', 20, 'bold'), width=7)
                value3.pack(padx=2, pady=2)

                ttkb.Button(window, text='Salvar', bootstyle='success', width=10, command=salvar_valores).pack(padx=2,
                                                                                                               pady=2)
            else:
                def salvar_valores() -> None:
                    if value1.get() == '' or value3.get() == '' or value2.get() == '':
                        messagebox.showwarning(title="Error", message="Campos vazios!")
                    else:
                        global comeca, termina, num

                        comeca = float(value1.get())
                        termina = float(value2.get())
                        num = int(value3.get())

                        ttkb.Label(window, text="Salvo!", font=('Courier', 14, 'bold')).pack(padx=2, pady=2)
                        ttkb.Button(window, text='Avançar', bootstyle='success', width=15,
                                    command=lambda: pega_funcao(func)).pack(padx=2, pady=6)

                for widget in window.winfo_children():
                    widget.destroy()

                ttkb.Button(window, text='Voltar', bootstyle='success', width=15, command=main).pack(padx=4, pady=4,
                                                                                                     anchor='nw')

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Agora digite os valores de X:", font=('Courier', 15, 'bold'),
                      padx=2,
                      pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="(começam / terminam / quantos são)", font=('Courier', 20, 'bold'), padx=2,
                      pady=2).pack()
                tk.Label(window, text="ex: -5 / 5 / 100", font=('Courier', 20, 'bold'), padx=2, pady=2).pack()

                value1 = ttkb.Entry(window, font=('Courier', 20, 'bold'), width=7)
                value1.pack(padx=2, pady=2)

                value2 = ttkb.Entry(window, font=('Courier', 20, 'bold'), width=7)
                value2.pack(padx=2, pady=2)

                value3 = ttkb.Entry(window, font=('Courier', 20, 'bold'), width=7)
                value3.pack(padx=2, pady=2)

                ttkb.Button(window, text='Salvar', bootstyle='success', width=15, command=salvar_valores).pack(padx=2,
                                                                                                               pady=2)

        def linear(a):
            if a == '':
                messagebox.showwarning(title="Error", message="Campos vazios!")
            else:
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
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15,
                            command=lambda: pega_funcao('1')).pack(padx=4, pady=4)

        def afim(a, b):
            if a == '' or b == '':
                messagebox.showwarning(title="Error", message="Campos vazios!")
            else:
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
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15,
                            command=lambda: pega_funcao('2')).pack(padx=4, pady=4)

        def quad(a, b, c):
            if a == '' or b == '' or c == '':
                messagebox.showwarning(title="Error", message="Campos vazios!")
            else:
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

                x_vertice = -float(b) / (2 * float(a))
                y_vertice = float(a) * (x_vertice ** 2) + float(b) * x_vertice + float(c)

                # Plotando os pontos máximos e mínimos no gráfico
                ax.plot(x_vertice, y_vertice, 'ro', label=f'Vertex ({x_vertice:.2f}, {y_vertice:.2f})')
                ax.legend()

                # Criar uma instância de FigureCanvasTkAgg
                canvas = FigureCanvasTkAgg(fig, master=window)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack()

                ttkb.Button(window, text='Reiniciar', bootstyle="success", width=15, command=main).pack(padx=2, pady=6)
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15,
                            command=lambda: pega_funcao('3')).pack(padx=4, pady=4)

        def exp(a):
            if a == '':
                messagebox.showwarning(title="Error", message="Campos vazios!")
            else:
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
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15,
                            command=lambda: pega_funcao('4')).pack(padx=4, pady=4)

        def log(a):
            if a == '':
                messagebox.showwarning(title="Error", message="Campos vazios!")
            elif float(a) <= 1:
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
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15,
                            command=lambda: pega_funcao('5')).pack(padx=4, pady=4)

        def trig(func):
            if func == '':
                messagebox.showwarning(title="Error", message="Campos vazios!")
            elif func == '1':
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
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15,
                            command=lambda: pega_funcao('6')).pack(padx=4, pady=4)
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
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15,
                            command=lambda: pega_funcao('6')).pack(padx=4, pady=4)
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
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15,
                            command=lambda: pega_funcao('6')).pack(padx=4, pady=4)

        def pega_funcao(op):
            # Limpar a janela antes de exibir o resultado
            for widget in window.winfo_children():
                widget.destroy()

            if op == '1':
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15, command=lambda: define_x('1')).pack(
                    padx=4, pady=4, anchor='nw')
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = ax |", font=('Courier', 20, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="> Digite o valor de a:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                a_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                a_entry.pack(padx=2, pady=2)

                # Botão para calcular a função linear
                ttkb.Button(window, text='Gráfico', bootstyle="success", width=15,
                            command=lambda: linear(a_entry.get())).pack(padx=2, pady=2)
            elif op == '2':
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15, command=lambda: define_x('2')).pack(
                    padx=4, pady=4, anchor='nw')
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = ax + b |", font=('Courier', 20, 'bold'), padx=2,
                      pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()

                tk.Label(window, text="> Digite o valor de a:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                a_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                a_entry.pack(padx=2, pady=2)

                tk.Label(window, text="> Digite o valor de b:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                b_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                b_entry.pack(padx=2, pady=2)

                ttkb.Button(window, text='Gráfico', bootstyle="success", width=10,
                            command=lambda: afim(a_entry.get(), b_entry.get())).pack(padx=2, pady=2)
            elif op == '3':
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15, command=lambda: define_x('3')).pack(
                    padx=4, pady=4,anchor='nw')

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = ax² + bx + c |", font=('Courier', 20, 'bold'), padx=2,
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

                ttkb.Button(window, text='Gráfico', bootstyle="success", width=10,
                            command=lambda: quad(a_entry.get(), b_entry.get(), c_entry.get())).pack(padx=2, pady=2)
            elif op == '4':
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15, command=lambda: define_x('4')).pack(
                    padx=4, pady=4,anchor='nw')

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = a^x |", font=('Courier', 20, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="> Digite o valor de a:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                a_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                a_entry.pack(padx=2, pady=2)

                ttkb.Button(window, text='Gráfico', bootstyle="success", width=10,
                            command=lambda: exp(a_entry.get())).pack(padx=2, pady=2)
            elif op == '5':
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15, command=lambda: define_x('5')).pack(
                    padx=4, pady=4,anchor='nw')

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = logax (log de x na base a) |", font=('Courier', 15, 'bold'),
                      padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="Obs: Para log, a > 1.", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="> Digite o valor de a:", font=('Courier', 15, 'bold'), padx=2, pady=2).pack()
                a_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                a_entry.pack(padx=2, pady=2)

                ttkb.Button(window, text='Gráfico', bootstyle="success", width=10,
                            command=lambda: log(a_entry.get())).pack(padx=2, pady=2)
            elif op == '6':
                ttkb.Button(window, text='Voltar', bootstyle='success', width=15, command=lambda: define_x('6')).pack(
                    padx=4, pady=4, anchor='nw')

                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="| Equação geral: f(x) = 1 - sen(x) 2 - cos(x) 3 - tg(x) |",
                      font=('Courier', 13, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
                tk.Label(window, text="> Digite a opção de função:", font=('Courier', 20, 'bold'), padx=2, pady=2).pack()
                func_entry = ttkb.Entry(window, font=('Courier', 15, 'bold'), width=5)
                func_entry.pack(padx=2, pady=2)

                ttkb.Button(window, text='Gráfico', bootstyle="success", width=10,
                            command=lambda: trig(func_entry.get())).pack(padx=2, pady=2)

        def main():
            def call2(event):
                if op.get() in {'1', '2', '3', '4', '5', '6'}:
                    define_x(op.get())
                else:
                    messagebox.showwarning(title="Error", message="Valor não existente")

            for widget in window.winfo_children():
                widget.destroy()

            tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="|| Obter Gráficos ||", fg='blue', font=('Courier', 22, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="  ", font=('Courier', 4, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="Qual o tipo da sua função?", font=('Courier', 22, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="1 - Linear", font=('Courier', 22, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="2 - Afim", font=('Courier', 22, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="3 - Quadrática", font=('Courier', 22, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="4 - Exponencial", font=('Courier', 22, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="5 - Logarítmica", font=('Courier', 22, 'bold'), padx=2, pady=2).pack()
            tk.Label(window, text="6 - Trigonométrica", font=('Courier', 22, 'bold'), padx=2, pady=2).pack()

            tk.Button(window, text='Histórico de gráficos', font=('Courier New', 10, 'bold'), width=12,
                      pady=3, padx=2).place(x=30, y=500)

            op = ttkb.Entry(window, bootstyle="danger", font=('Courier', 22, 'bold'), width=1)
            op.pack(padx=2, pady=2)

            op.bind('<Return>', call2)

            # ttkb.Button(window, text='Ok', bootstyle="success", width=5, command=lambda: define_x(op.get())).pack(
            #    padx=2,
            #    pady=2)

        main()

        window.mainloop()

    def doc_window():
        docwin = ttkb.Window(themename='cyborg')
        docwin.iconbitmap('capivara.ico')
        docwin.title("Gráficos")
        docwin.resizable(False, False)

        width3 = 400
        height3 = 400

        width5 = first_window.winfo_screenwidth()
        height5 = first_window.winfo_screenheight()

        posx4 = (width5 // 5) - (width3 // 5)
        posy4 = (height5 // 2) - (height3 // 2)

        # Define a posição da janela
        docwin.geometry('{}x{}+{}+{}'.format(width3, height3, posx4, posy4))

        # Criando uma barra de rolagem vertical
        barra_de_rolagem = tk.Scrollbar(docwin)
        barra_de_rolagem.pack(side=tk.RIGHT, fill=tk.Y)

        # Criando um widget de texto
        texto = tk.Text(docwin, wrap=tk.NONE, yscrollcommand=barra_de_rolagem.set, state='normal')
        texto.pack()

        # Associando a barra de rolagem ao widget de texto
        barra_de_rolagem.config(command=texto.yview)

        # Adicionando algum texto ao widget de texto
        texto.insert(tk.END, "1.0 - Primeira Janela (tema)\n"
                             "2.0 - Segunda Janela (tipos de funções)\n"
                     "3.0 - Valores de X\n"
                     "4.0 - Equação geral e valor dos coeficientes numéricos\n"
                     "5.0 - Gráfico\n"
                     "\n"
                     "1.0 - Primeira Janela:\n"
                     "Na primeira janela é possível escolher entre 4 temas diferentes\n"
                     "sendo 2 claros e 2 escuros. Ao selecionar o número do tema\n"
                     "basta pressionar enter e a próxima janela será aberta.\n"
                     "\n"
                     "2.0 - Segunda Janela:\n"
                     "Na segunda janela são dispostas as 6 opções de funções para\n"
                     "criação de gráficos, podendo serem selecionadas apenas com o\n"
                     "número e pressionando enter.\n"
                     "\n"
                     "3.0 - Valores dos pontos no eixo X:\n"
                     "Agora é necessário definir qual o intervalo de pontos no eixo X\n"
                     "passados para a função, e também a quantidade deles, formando a\n"
                     "imagem da função. No caso de uma função trigonométrica esses\n"
                     "pontos serão em graus. E em caso de uma função logaritmica, há\n"
                     "uma restrição, os pontos devem começar acima de 0.\n"
                     "\n"
                     "4.0 - Equação geral e o valor dos coeficientes numéricos\n"
                     "Na penúltima tela, é exibida a equação geral da função escolhida,\n"
                     "e é nela que se definem os valores dos termos que multiplicam X na\n"
                     "função.\n"
                     "\n"
                     "5.0 - Gráfico:\n"
                     "Por fim, o gráfico é gerado, podeno ser reiniciado ou apenas voltar.\n"

                     )

        docwin.mainloop()

    # Função para verificar se a opção está correta e chamar a main
    def call(event) -> None:
        opcao = tema.get()
        if opcao in {'1', '2', '3', '4'}:
            main_window(opcao)
        else:
            messagebox.showwarning(title="Error", message="Valor não existente")

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
    tk.Label(first_window, text="4 - Vapor", font=('Courier New', 18, 'bold'), padx=2, pady=2).pack()

    tema = ttkb.Entry(first_window, bootstyle="dark", font=('Courier New', 18, 'bold'), width=1)
    tema.pack(padx=2, pady=2)

    tema.bind('<Return>', call)

    tk.Label(first_window, text="Pressione Enter", font=('Courier New', 10, 'bold'), padx=2, pady=2).pack()

    ttkb.Button(first_window, text='Ok', bootstyle="success", width=8, command=lambda: main_window(tema.get()))

    tk.Button(first_window, text='Documentação', font=('Courier New', 10, 'bold'), width=12, command=doc_window,
              pady=3, padx=2).place(x=150, y=360)

    first_window.mainloop()


theme_definition_window()
