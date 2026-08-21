#Variaveis
m_vendedor = ["", 0]
vendas = [[1200, 1500, 1100],[1000, 1300, 1400],[900, 1700, 1600]]



def line():
    print(28 * '-')

def total_vendedor():
    for c1 in range(0, len(vendas)):
        tot_vendas = 0
        for c2 in range(0, len(vendas[c1])):
            tot_vendas += vendas[c1][c2]
        if tot_vendas > m_vendedor[1]:
            m_vendedor[1] = tot_vendas
            m_vendedor[0] = c1
        print(f"total vendedor {c1 + 1}; R${tot_vendas}")

def total_mes():
    for c1 in range(0, len(vendas)):
        tot_mes = 0
        for c2 in range(0, len(vendas)):
            tot_mes += vendas[c2][c1]
        print(f"total vendido no mes {c1 + 1}; R${tot_mes}")

def total_empresa():
    tot_empresa = 0
    for c1 in range(0, len(vendas)):
        for c2 in range(0, len(vendas[c1])):
            tot_empresa += vendas[c1][c2]
    print(f"total da empresa; R${tot_empresa}")

def melhor_vendedor():
    print(f"O melhor vendedor foi o {m_vendedor[0] + 1}º com R${m_vendedor[1]} ")



#Execução
total_vendedor()
line()
total_mes()
line()
total_empresa()
line()
melhor_vendedor()