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
## 📊 Exemplo de Saída do Sistema (Relatório de Frota)
```text
------------------------------------------------------------------------------------------
📋 RELATÓRIO DE FROTA INDUSTRIAL - DATA: 27/03/2026
------------------------------------------------------------------------------------------
[VTR-001] Hilux 4x4 L200  | Status: Disponível   | Odômetro: 45200 km | Faltam 4800 km
[VTR-002] Hilux 4x4 L200  | Status: Disponível   | Odômetro: 61000 km | ⚠️ CRÍTICO: REVISÃO IMEDIATA
[EMP-010] Empilhadeira CAT| Status: Em Manutenção| Odômetro: 12500 km | Faltam 9500 km
[VTR-003] Ford Ranger     | Status: Disponível   | Odômetro: 15000 km | Faltam 5000 km
[BUS-005] Micro-ônibus    | Status: Disponível   | Odômetro: 89500 km | Faltam 500 km
------------------------------------------------------------------------------------------
