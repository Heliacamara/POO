import tkinter as tk
from tkinter import messagebox, simpledialog
from ContaBancaria import Cliente,ContaBancaria,Endereco,ContaCorrente,ContaPoupanca,ContaSalario

class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x400")

        cliente1 = Cliente('Helia', '164.913', Endereco("Rua zumbi", "834", "centro", "Ceara-mirim"))
        cliente2 = Cliente('Vitor', '124.248', Endereco("Rua Lagos", "29", "centro", "Ceara-mirim"))
        cliente3 = Cliente('Giovanna', '943.135', Endereco("Rua Mosquito", "128", "centro", "Ceara-mirim"))
        cliente4 = Cliente('Bernardo', '517.925', Endereco("Rua do Farol", "724", "centro", "Ceara-mirim"))

        self.contas = [
            ContaCorrente(cliente1, 1001, 500,200,50),
            ContaPoupanca(cliente3, 1003, 300,0.1),
            ContaBancaria(cliente4, 1004, 20),
            ContaBancaria(cliente2, 1002, 1000)
        ]

        if(self.contas[0].verificar_conta_duplicada()):
            messagebox.showerror("Erro", "Existe conta duplicada")
            messagebox.showinfo("contas", self.contas[0].contas_duplicadas())
            exit()

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        btn_depositar = tk.Button(
                janela,
                text="Criar Conta",
                width=15,
                command=lambda:  self.criar_conta()
            )
        # btn_depositar.config(state="disabled")
        btn_depositar.pack(pady=2)


        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()

        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)

            lbl_titular = tk.Label(
                frame,
                text=conta.get_titular(),
                font=("Arial", 14, "bold")
            )
            lbl_titular.pack()

            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}"
            )
            lbl_numero.pack()

            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)

            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            # btn_depositar.config(state="disabled")
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            # btn_sacar.config(state="disabled")
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            # btn_transferir.config(state="disabled")
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            # btn_dados.config(state="disabled")
            btn_dados.pack(pady=2)
            
            # btn_dados.config(state="disabled")
            btn_dados.pack(pady=2)

            btn_rendimento = tk.Button(
                frame,
                text="Render Juros",
                width=15,
                command=lambda c=conta: self.render_juros(c)
            )
            #btn_rendimento.config(state="disabled")
            btn_rendimento.pack(pady=2)

            btn_taxa = tk.Button(
                frame,
                text="Cobrar Taxa",
                width=15,
                command=lambda c=conta: self.cobrar_taxa(c)
            )
            #btn_taxa.config(state="disabled")
            btn_taxa.pack(pady=2)

    def depositar(self, conta):
        valor = simpledialog.askfloat("Depósito", "Digite o valor do depósito:")

        if valor is not None:
            if conta.depositar(valor):
                messagebox.showinfo("Sucesso", "Depósito realizado.")
            else:
                messagebox.showerror("Erro", "Valor inválido.")

        self.atualizar_tela()

    def sacar(self, conta):
        valor = simpledialog.askfloat("Saque", "Digite o valor do saque:")

        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado.")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def transferir(self, conta_origem):
        valor = simpledialog.askfloat("Transferência", "Digite o valor:")

        if valor is None:
            return

        numero_destino = simpledialog.askinteger(
            "Transferência",
            "Digite o número da conta destino:"
        )

        conta_destino = None

        for conta in self.contas:
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta destino não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())
    
    def render_juros(self, conta):
        if(conta.get_tipo_conta() == "Conta Poupança"):
            conta.render_juros()
            messagebox.showinfo("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Conta não disponibiliza rendimento")
        self.atualizar_tela()
    
    def cobrar_taxa(self, conta):
        if(conta.get_tipo_conta() == "Conta Corrente"):
            conta.cobrar_taxa()
            messagebox.showerror("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Cobrança invalida para essa conta")

    def criar_conta(self):
        janela_cadastro = tk.Toplevel(self.janela)
        janela_cadastro.title("Criar nova conta")
        janela_cadastro.geometry("300x500")
        janela_cadastro.resizable(False, False)

        tk.Label(janela_cadastro, text="Titular:").pack(pady=5)
        entrada_titular = tk.Entry(janela_cadastro)
        entrada_titular.pack()

        tk.Label(janela_cadastro, text="Número da conta:").pack(pady=5)
        entrada_numero = tk.Entry(janela_cadastro)
        entrada_numero.pack()

        tk.Label(janela_cadastro, text="Saldo inicial:").pack(pady=5)
        entrada_saldo = tk.Entry(janela_cadastro)
        entrada_saldo.pack()

        tk.Label(janela_cadastro, text="CPF:").pack(pady=5)
        entrada_CPF= tk.Entry(janela_cadastro)
        entrada_CPF.pack()

        tk.Label(janela_cadastro, text="Rua:").pack(pady=5)
        entrada_Rua = tk.Entry(janela_cadastro)
        entrada_Rua.pack()

        tk.Label(janela_cadastro, text="Número:").pack(pady=5)
        entrada_NumeroCasa = tk.Entry(janela_cadastro)
        entrada_NumeroCasa.pack()

        tk.Label(janela_cadastro, text="Bairro:").pack(pady=5)
        entrada_Bairro = tk.Entry(janela_cadastro)
        entrada_Bairro.pack()

        tk.Label(janela_cadastro, text="Cidade:").pack(pady=5)
        entrada_Cidade = tk.Entry(janela_cadastro)
        entrada_Cidade.pack()

        tk.Label(janela_cadastro, text="Tipo de Conta:").pack(pady=5)
        entrada_TipoConta = tk.Entry(janela_cadastro)
        entrada_TipoConta.pack()

        def salvar_conta():
            titular = entrada_titular.get()
            numero = entrada_numero.get()
            saldo = entrada_saldo.get()
            cpf= entrada_CPF.get()
            rua= entrada_Rua.get()
            numeroCasa= entrada_NumeroCasa.get()
            bairro= entrada_Bairro.get()
            cidade= entrada_Cidade.get()
            tipoConta= entrada_TipoConta.get()

            if titular == "" or numero == "" or saldo == "" or cpf == "" or rua == "" or numeroCasa == "" or bairro == "" or cidade == "":
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

            try:
                numero = int(numero)
                saldo = float(saldo)
            except ValueError:
                messagebox.showerror("Erro", "Número da conta e saldo devem ser valores numéricos.")
                return



            cliente=Cliente(titular,cpf, Endereço(rua,numeroCasa,bairro,cidade))

            if tipoConta == "Bancária":
                nova_conta = ContaBancaria(cliente, numero, saldo)
                self.contas.append(nova_conta)

            elif tipoConta == "Corrente":
                janela_cadastro = tk.Toplevel(self.janela)
                janela_cadastro.title("Criar nova conta")
                janela_cadastro.geometry("300x500")
                janela_cadastro.resizable(False, False)

                tk.Label(janela_cadastro, text="Limite:").pack(pady=5)
                entrada_titular = tk.Entry(janela_cadastro)
                entrada_titular.pack()

                tk.Label(janela_cadastro, text="Tarifa mensal:").pack(pady=5)
                entrada_numero = tk.Entry(janela_cadastro)
                entrada_numero.pack()


                nova_conta= ContaCorrente(cliente ,numero, saldo,)
                self.contas.append(nova_conta)

            elif tipoConta == "Poupança":
                nova_conta = ContaPoupaca(cliente,numero,saldo)
                self.contas.append(nova_conta)       

            elif tipoConta == "Salário":
                nova_conta = ContaSalario(cliente,numero,saldo)
                self.contas.append(nova_conta)

            messagebox.showinfo("Sucesso", "Conta criada com sucesso.")

            janela_cadastro.destroy()
            self.atualizar_tela()

        btn_salvar = tk.Button(
            janela_cadastro,
            text="Salvar conta",
            width=15,
            command=salvar_conta
        )
        btn_salvar.pack(pady=15)

janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()