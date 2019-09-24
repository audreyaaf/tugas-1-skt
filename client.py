import zerorpc

# Inisiasi client
client = zerorpc.Client()
client1 = zerorpc.Client()

# Buat koneksi TCP ke server
client.connect("tcp://127.0.0.1:8888")
client1.connect("tcp://127.0.0.1:4444")
# Panggil remote function dengan nama "hello" dengan parameter berupa string
# - Client stub akan building message
# - Message akan dikirimkan ke server
# - Menerima response dari server
saldo_awal_mp_bank =10000
saldo_awal_user_bank = 10000
saldo_awal_user_mp = 0

val = input ( "Input jumlah top up : ")
topup = int(val)

marketplace = client.topup(topup,saldo_awal_user_mp)
print (marketplace)

bank = client1.topup_client(topup,saldo_awal_user_bank)
print (bank)

bank = client1.topup_marketplace(topup,saldo_awal_mp_bank)

print (bank)