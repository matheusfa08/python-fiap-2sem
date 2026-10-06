import oracledb

USUARIO = "rm570933"
SENHA = "200308"
HOST = "oracle.fiap.com.br"
PORTA = 1521
SERVICE_NAME = "ORCL"

dsn = oracledb.makedsn(
    HOST,
    PORTA,
    service_name=SERVICE_NAME
)

class ConnectionFactory:
    def conectar(self):
        return oracledb.connect(
            user=USUARIO,
            password=SENHA,
            dsn=dsn
        )