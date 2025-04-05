# main.py
# ------------------------------------------------------------------------------
# Este é o arquivo principal do projeto de resgate em um parque natural.
# Ele importa as instâncias definidas em instancias.py, aplica a estratégia
# de Busca de Custo Uniforme para encontrar rotas que permitam resgatar
# um número mínimo de vítimas e sair do parque antes do anoitecer.
#
# O imprime os dados da solução para cada instância:
# - Caminho percorrido
# - Vítimas resgatadas
# - Custo total
# - Tempo restante
# ------------------------------------------------------------------------------
# main.py

import time
from instancias import instancias
from configuracoes import configuracoes
from itertools import permutations
import heapq

def dentro_limites(x, y, n):
    return 0 <= x < n and 0 <= y < n

def ucs(mapa, origem, destino):
    n = len(mapa)
    fila = [(0, origem, [])]
    visitados = {}

    while fila:
        custo, (x, y), caminho = heapq.heappop(fila)

        if (x, y) in visitados and visitados[(x, y)] <= custo:
            continue
        visitados[(x, y)] = custo

        novo_caminho = caminho + [(x, y)]

        if (x, y) == destino:
            return novo_caminho, custo

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if dentro_limites(nx, ny, n):
                valor = mapa[nx][ny]
                if valor == 10:
                    continue
                custo_mov = 2 if valor == 2 else 1
                heapq.heappush(fila, (custo + custo_mov, (nx, ny), novo_caminho))

    return None, float('inf')

def resolver_com_configuracao(idx, mapa, n, k, w, tempo_inicial):
    config = configuracoes.get(idx)
    if not config:
        print(f"⚠️ Instância {idx} não tem configuração definida.")
        return

    entrada = config["entrada"]
    saida = config["saida"]
    resgates = config["resgates"]

    tempo = tempo_inicial
    pos_atual = entrada
    caminho_total = [("INÍCIO", entrada)]
    custo_total = 0

    for pos in resgates:
        trajeto, custo = ucs(mapa, pos_atual, pos)
        if trajeto is None:
            print(f"Falha ao chegar a {pos}")
            return
        caminho_total += trajeto[1:]
        custo_total += custo
        tempo -= custo
        bonus = -mapa[pos[0]][pos[1]]
        tempo += bonus
        pos_atual = pos

    # Trajeto até a saída
    trajeto_saida, custo_saida = ucs(mapa, pos_atual, saida)
    if trajeto_saida is None:
        print("Falha ao sair do parque.")
        return

    caminho_total += trajeto_saida[1:]
    custo_total += custo_saida
    tempo -= custo_saida

    print(f"\n Instância {idx} resolvida com caminho fixo:")
    print(f"Entrada: {entrada} | Saída: {saida}")
    print(f"Resgates: {resgates}")
    print(f"Custo total: {custo_total} min")
    print(f"Tempo restante: {tempo} min")
    print("Caminho:")
    for passo in caminho_total:
        print(" ->", passo)

def main():
    for idx, inst in enumerate(instancias, start=1):
        print(f"\n Resolvendo instância {idx} com configuração fixa...")
        mapa, n, k, w, tempo_inicial = inst
        resolver_com_configuracao(idx, mapa, n, k, w, tempo_inicial)

if __name__ == "__main__":
    main()
