# configuracoes.py
# ------------------------------------------------------------------------------
# Define as configurações fixas para cada instância:
# - Visitantes a serem resgatados (posições)
# - Porta de entrada
# - Porta de saída
# ------------------------------------------------------------------------------

configuracoes = {

    # Instância 1
    1: {
        "resgates": [(2, 1), (4, 4)],
        "entrada": (4, 2),  # Porta sul
        "saida": (2, 4)     # Porta leste
    },

    # Instância 2
    2: {
        "resgates": [(0, 0), (0, 4), (4, 4)],
        "entrada": (4, 2),  # Porta sul
        "saida": (0, 2)     # Porta norte
    },

    # Instância 3
    3: {
        "resgates": [(1, 1), (3, 2), (5, 6)],
        "entrada": (3, 0),  # Porta oeste
        "saida": (6, 3)     # Porta sul
    },

    # Instância 4
    4: {
        "resgates": [(0, 1), (0, 5), (3, 2), (5, 6)],
        "entrada": (6, 0),  # Porta oeste
        "saida": (3, 6)     # Porta leste
    },

    # Instância 5
    5: {
        "resgates": [(1, 2), (3, 5), (6, 7), (8, 0)],
        "entrada": (4, 0),  # Porta oeste
        "saida": (8, 4)     # Porta sul
    },

    # Instância 6
    6: {
        "resgates": [(3, 1), (4, 4), (5, 6), (6, 5), (7, 9), (9, 5)],
        "entrada": (0, 5),  # Porta norte
        "saida": (10, 5)    # Porta sul
    },

    # Instância 7
    7: {
        "resgates": [(1, 0), (2, 11), (3, 6), (5, 2), (8, 4),
                     (9, 5), (10, 4), (10, 10), (11, 12), (12, 3)],
        "entrada": (6, 0),   # Porta oeste
        "saida": (6, 12)     # Porta leste
    },

    # Instância 8
    8: {
        "resgates": [(0, 0), (0, 12), (1, 13), (5, 12), (6, 6),
                     (7, 10), (8, 14), (9, 5), (11, 13), (14, 14)],
        "entrada": (0, 7),   # Porta norte
        "saida": (14, 7)     # Porta sul
    },

    # Instância 9 (idêntica à 8 no enunciado)
    9: {
        "resgates": [(0, 0), (0, 12), (1, 13), (5, 12), (6, 6),
                     (7, 10), (8, 14), (9, 5), (11, 13), (14, 14)],
        "entrada": (0, 7),
        "saida": (14, 7)
    },

    # Instância 10
    10: {
        "resgates": [(0, 0), (0, 12), (3, 6), (5, 12), (6, 2),
                     (7, 10), (8, 12), (10, 10), (11, 0), (14, 14)],
        "entrada": (0, 7),    # Porta norte
        "saida": (14, 7)      # Porta sul
    }
}
