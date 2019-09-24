import zerorpc


# Inisisi class
class mp(object):
    # Buat remote function yang harus dieksekusi oleh server
    # - Nama fungsi : hello
    # - Parameter : data berupa string

    def topup(self, jumlah, saldo_client_awal, ):
        saldo_client= jumlah + saldo_client_awal
        return "jumlah topup : " + str(jumlah), "saldo awal user di marketplace : " + str(saldo_client_awal), "saldo akhir user di marketplace: " + str(saldo_client)


# Inisiasi server
server = zerorpc.Server(mp())
# Binding ke IP dan port tertentu
server.bind("tcp://0.0.0.0:8888")
server.run()