import zerorpc


# Inisisi class
class bank(object):
    # Buat remote function yang harus dieksekusi oleh server
    # - Nama fungsi : hello
    # - Parameter : data berupa string
    def topup_client(self, jumlah, saldo_client_awal ):
        saldo_client = saldo_client_awal - jumlah
        return "saldo user di bank awal : " + str(saldo_client_awal), "saldo user di bank akhir : " + str(saldo_client)

    def topup_marketplace(self, jumlah, saldo_marketplace_awal ):
        saldo_marketplace = saldo_marketplace_awal + jumlah
        return "saldo marketplace di bank awal : " + str(saldo_marketplace_awal), "saldo_marketplace di bank akhir : " + str(saldo_marketplace)


# Inisiasi server
server = zerorpc.Server(bank())
# Binding ke IP dan port tertentu
server.bind("tcp://0.0.0.0:4444")
server.run()