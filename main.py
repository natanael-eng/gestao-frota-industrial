import json
from datetime import datetime

class Veiculo:
    def __init__(self, tag, modelo, odometro_atual, ultima_revisao, status="Disponível"):
        self.tag = tag
        self.modelo = modelo
        self.odometro_atual = odometro_atual
        self.ultima_revisao = ultima_revisao
        self.status = status  # Disponível, Em Manutenção, Reservado

    def calcular_proxima_revisao(self, intervalo=10000):
        km_para_revisao = (self.ultima_revisao + intervalo) - self.odometro_atual
        return km_para_revisao

    def exibir_status(self):
        km_restante = self.calcular_proxima_revisao()
        alerta = "⚠️ CRÍTICO: REVISÃO IMEDIATA" if km_restante <= 0 else f"Faltam {km_restante} km"
        
        print(f"[{self.tag}] {self.modelo.ljust(15)} | Status: {self.status.ljust(12)} | Odômetro: {self.odometro_atual} km | {alerta}")

# --- BANCO DE DADOS SIMULADO (5 VEÍCULOS DE MINERAÇÃO) ---
frota = [
    Veiculo("VTR-001", "Hilux 4x4 L200", 45200, 40000),    # Faltam 4800km
    Veiculo("VTR-002", "Hilux 4x4 L200", 61000, 50000),    # VENCIDO (11000km rodados)
    Veiculo("EMP-010", "Empilhadeira CAT", 12500, 12000, "Em Manutenção"),
    Veiculo("VTR-003", "Ford Ranger", 15000, 10000),       # Faltam 5000km
    Veiculo("BUS-005", "Micro-ônibus", 89500, 80000)       # Faltam 500km (Próximo!)
]

def gerar_relatorio_frota():
    print("-" * 90)
    print(f"📋 RELATÓRIO DE FROTA INDUSTRIAL - DATA: {datetime.now().strftime('%d/%m/%Y')}")
    print("-" * 90)
    for v in frota:
        v.exibir_status()
    print("-" * 90)

if __name__ == "__main__":
    gerar_relatorio_frota()
