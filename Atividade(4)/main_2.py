from restaurante import Restaurante

def main():
    restaurante = Restaurante("Temperos da Vó", "Comida Caseira")

    print(restaurante)
    print(f"Clientes atendidos: {restaurante.getNumeroServidos()}")

    restaurante.setNumeroServidos(35)
    print(f"Clientes atendidos após alteração: {restaurante.getNumeroServidos()}")

    restaurante.incrementeNumeroServidos(10)
    print(f"Clientes atendidos após incrementar atualização: {restaurante.getNumeroServidos()}")

    restaurante.abrirRestaurante()

if __name__ == "__main__":
    main()