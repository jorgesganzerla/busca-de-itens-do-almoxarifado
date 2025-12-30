import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista de produtos (com nomes únicos e formatados)
produtos = [
    "Gliter", "Cola", "Fita transparente", "Etiquetas Pimaco 2000", "Folha", "Pilha", "Caneta", "Pincel para quadro branco",
    "Apontador", "Borracha", "Lâmina", "Refio", "Sacola Madeira", "Sacola Transparente", "Bastão (Grosso e Fino)",
    "Perfurador", "Papel Contactil", "Fita Madeira", "Pasta da URI", "Folha branca de ofício",
    "Papel pardo", "Post-it", "Caneta para CD e DVD", "Grampo", "Clip", "Fósforo", "CD", "DVD",
    "Giz Branco", "Giz Colorido", "Envelope", "Papel de Arquivo Morto", "Azeite", "Café",
    "Guardanapo", "Farinha", "Massa", "Água", "Açúcar", "Copo de café", "Pasta do ANAGRO", "Balão",
    "Tampa de Vaso", "Cola P. Cano", "Fita Vesa Rosca", "Parafuso", "Colher e Prato de festa",
    "Pano de chão", "Pano de louça", "Copo 50 ML", "Térmica", "Copo para Alcoolgel", "Arame", "Prego", "Ganchos",
    "Rebite", "Fita isolante", "Bucha", "Parafuso", "Interruptor", "Plug", "Tomada", "Disjuntor", "Isopor",
    "Sapato", "EPI", "Luvas de borracha", "Máscara", "Óculos de Proteção", "Capa de Chuva",
    "Luvas Multi-Tato", "Repelente", "Protetor solar", "Nitrílica"
]

faixas_prateleira = {
    "primeira": range(1, 33),
    "segunda": range(33, 45),
    "terceira": range(45, 54),
    "quarta": range(54, 66),
    "quinta": range(66, len(produtos) + 1)
}

excecoes = {
    "parafuso": ["segunda", "quarta"],
    "prego": "quarta",
    "ganchos": "quarta",
    "epi": "quinta",
    "papel de arquivo morto": "primeira"
}

sugestoes = {
    "prato": "Colher e prato de festa",
    "colher": "Colher e prato de festa",
    "etiquetas": "Etiquetas Pimaco 2000",
    "giz": ["Giz Colorido", "Giz Branco"],
    "pincel": "Pincel para quadro branco",
    "sacola": ["Sacola Madeira", "Sacola Transparente"],
    "bastão": "Bastão (Grosso e Fino)",
    "fita": ["Fita Madeira", "Fita Transparente", "Fita Vesa Rosca", "Fita isolante"],
    "caneta": ["Caneta para CD e DVD", "Caneta"],
    "copo": ["Copo de café", "Copo 50 ML", "Copo para Alcoolgel"],
    "papel": ["Papel Contactil", "Papel pardo", "Papel de Arquivo Morto", "Folha branca de ofício"],
    "pasta": ["Pasta da URI", "Pasta do ANAGRO"],
    "tampa": "Tampa de Vaso",
    "pregos": "Prego",
    "gancho": "Ganchos",
    "cola": ["Cola", "Cola P. Cano"],
    "pano": ["Pano de chão", "Pano de louça"],
    "luvas": ["Luvas de borracha", "Luvas Multi-Tato"]
}

def localizar_produto(nome_produto):
    nome_produto = nome_produto.lower()
    produtos_normalizados = [p.lower() for p in produtos]

    if nome_produto in excecoes:
        valor = excecoes[nome_produto]
        if isinstance(valor, list):
            return f"\n📦 O produto '{nome_produto.title()}' está nas estantes: {', '.join(valor)}."
        else:
            return f"\n📦 O produto '{nome_produto.title()}' está na {valor} estante."

    if nome_produto in produtos_normalizados:
        indice = produtos_normalizados.index(nome_produto) + 1
        for nome_prateleira, faixa in faixas_prateleira.items():
            if indice in faixa:
                return f"\n📦 O produto '{produtos[indice - 1]}' está na {nome_prateleira} estante."
    return "❌ Produto não encontrado. Verifique a grafia ou acentuação."

# Criar interface
tela = tk.Tk()
tela.title("Localizador de Produtos - Almoxarifado")
tela.geometry("500x300")
tela.configure(bg="#f0f0f0")

rotulo = tk.Label(tela, text="Digite o nome do produto:", font=("Arial", 14), bg="#f0f0f0")
rotulo.pack(pady=10)

entrada = tk.Entry(tela, width=40, font=("Arial", 12))
entrada.pack(pady=5)

def buscar():
    nome = entrada.get().strip().lower()
    if not nome:
        messagebox.showwarning("Aviso", "Por favor, digite o nome de um produto.")
        return

    if nome in sugestoes:
        opcao = sugestoes[nome]
        if isinstance(opcao, list):
            escolha = simpledialog.askinteger(
                "Produto semelhante",
                "Você quis dizer:\n" + "\n".join(f"{i+1}) {item}" for i, item in enumerate(opcao)) + "\n\nDigite o número da opção:",
                minvalue=1, maxvalue=len(opcao)
            )
            if escolha:
                resultado = localizar_produto(opcao[escolha - 1])
            else:
                resultado = "⚠️ Nenhuma opção selecionada."
        else:
            resultado = localizar_produto(opcao)
    else:
        resultado = localizar_produto(nome)

    messagebox.showinfo("Resultado", resultado)

botao = tk.Button(tela, text="Buscar", font=("Arial", 12), bg="#4caf50", fg="white", command=buscar)
botao.pack(pady=20)

tela.mainloop()