from sqlalchemy import create_engine

class DBConnectionHandler:

    def __init__(self):
        self.__connection_string = "sqlite:///debug.db"
        self.session = None

    def create_engine(self):
        """
        Retorna o objeto de conexão do banco de dados
        :param - None
        :return - Conexão com o banco de dados
        """
        engine = create_engine(self.__connection_string)
        return engine
