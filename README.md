# Localizador de Produtos - Almoxarifado URI
Sistema de busca para localização de produtos no almoxarifado da URI, desenvolvido em Python com interface gráfica.

## Funcionalidades
- **Busca por nome**: Digite o nome do produto para encontrar sua localização
- **Sugestões inteligentes**: O sistema sugere produtos similares quando há múltiplas opções
- **Organização por estantes**: Produtos organizados em 5 estantes numeradas
- **Interface amigável**: Interface gráfica simples e intuitiva

## Como usar
1. Execute o arquivo `busca_por_nome_do_produto_do_Almoxarifado.py`
2. Digite o nome do produto na caixa de texto
3. Clique em "Buscar"
4. O sistema mostrará a localização do produto ou sugerirá alternativas

## Requisitos
- Python 3.x
- Tkinter (incluído na instalação padrão do Python)

## Execução
```bash
python busca_por_nome_do_produto_do_Almoxarifado.py
```

## Produtos disponíveis
O sistema possui mais de 70 produtos catalogados, incluindo:
- Material de escritório (canetas, papel, clips)
- Material de limpeza (panos, produtos de higiene)
- Material elétrico (fitas, parafusos, disjuntores)
- EPIs (máscaras, luvas, óculos de proteção)
- Alimentos básicos (café, açúcar, água)

## Organização das estantes
- **Primeira estante**: Produtos 1-32
- **Segunda estante**: Produtos 33-44  
- **Terceira estante**: Produtos 45-53
- **Quarta estante**: Produtos 54-65
- **Quinta estante**: Produtos 66+

## Recursos especiais
- **Exceções**: Alguns produtos têm localizações específicas (ex: parafusos em múltiplas estantes)
- **Sugestões**: Sistema de autocorreção para termos similares (ex: "prato" → "Colher e prato de festa")
- **Busca flexível**: Aceita variações de nomes e termos parciais
