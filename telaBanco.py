from conta import Conta
conta1 = Conta("Antonio", 1234, "1010-7")
conta1.extrato()
conta1.deposito(1000)
conta1.saque(200)
conta1.saque(1500)
conta1.extrato()
conta2 = Conta("Tonhio" 1234, "7070-7")
conta2.extrato
conta1.transferir(300,conta2)