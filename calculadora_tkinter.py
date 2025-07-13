import tkinter as tk

def calcular():
    try:
        resultado = eval(entrada.get())
        rotulo_resultado.config(text="Resultado: " + str(resultado))
    except:
        rotulo_resultado.config(text="Erro!")

# Criar janela
janela = tk.Tk()
janela.title("Calculadora")

# Campo de entrada
entrada = tk.Entry(janela, width=20)
entrada.pack(padx=10, pady=10)

# Botão para calcular
botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack(pady=5)

# Resultado
rotulo_resultado = tk.Label(janela, text="Resultado:")
rotulo_resultado.pack(pady=5)

# Iniciar a interface
janela.mainloop()
