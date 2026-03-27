# 🚜 Fleet Industrial Control (FIC) - Gestão de Ativos

## 📌 Visão Geral
Este sistema foi desenvolvido para gerenciar a disponibilidade física e a manutenção preventiva de frotas em ambientes de mineração e grandes indústrias. O foco é garantir que nenhum veículo opere acima do limite de segurança de quilometragem.

## 🛠️ Diferenciais Técnicos
Diferente de scripts simples, este projeto aplica:
* **POO (Programação Orientada a Objetos):** Classes e métodos para representar veículos reais.
* **Lógica de Status:** Controle de prontidão (Disponível vs. Em Manutenção).
* **Cálculo de Proximidade:** Alertas automáticos baseados na diferença entre o odômetro atual e a última revisão.

## 📊 Regras de Negócio Aplicadas
* **Prefixos de Identificação:** Padronização por TAG (VTR, EMP, BUS).
* **Plano de Manutenção:** Intervalo fixo de 10.000 km para revisões preventivas.
* **Priorização:** Alerta crítico para veículos com revisão vencida.

## 💻 Tecnologias
* **Python 3.x**
* **Lógica de Datas e Contadores Numéricos**

---
**Desenvolvido por Natanael Lira Ferreira** *Manutenção Industrial | Estudante de Engenharia de Software*
