m_total = 50
num_gue = 3
m_p_guer = m_total // num_gue # divisão exata
m_inf = m_total % num_gue # pega o resto de divisão
print(f"Cada Guerreiro receberá: {m_p_guer} moedas")
print(f"O informante receberá: {m_inf} moedas")