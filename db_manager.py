import sqlite3
from sqlite3 import Error
from tkinter import messagebox 

class DatabaseManager:
    def __init__(self, db_name="banco_database.db"):
        self.db_name = db_name
        self.create_tables() # Garante que as tabelas são criadas ao inicializar a classe

    def connect(self):
        """Conecta ao banco de dados e retorna o objeto de conexão."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            conn.execute("PRAGMA foreign_keys = ON") 
            return conn
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            messagebox.showerror("Erro de Banco de Dados", f"Falha ao conectar ao banco de dados: {e}")
            return None

    def create_tables(self):
        """Cria as tabelas necessárias se elas não existirem."""
        conn = self.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS HORARIOS (
                        IDHORARIO INTEGER PRIMARY KEY AUTOINCREMENT,
                        DATA TEXT NOT NULL,
                        HORA_ENTRADA TEXT NOT NULL,
                        ENTRA_ALMOCO TEXT,
                        SAIDA_ALMOCO TEXT,
                        HORA_SAIDA TEXT NOT NULL,
                        SEMANA_PROVA BLOB DEFAULT 0,
                        CODUSUARIO TEXT,
                        FOREIGN KEY (CODUSUARIO) REFERENCES USUARIO(CODUSUARIO)
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS PERFIL (
                        IDPERFIL INTEGER PRIMARY KEY AUTOINCREMENT,
                        CODPERFIL TEXT UNIQUE NOT NULL
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS USUARIO (
                        CODUSUARIO TEXT PRIMARY KEY,
                        NOME TEXT NOT NULL,
                        EMAIL TEXT UNIQUE NOT NULL,
                        SENHA TEXT NOT NULL,
                        CODPERFIL TEXT,
                        FOREIGN KEY (CODPERFIL) REFERENCES PERFIL(CODPERFIL)
                    )
                """)
                conn.commit()
            except Error as e:
                print(f"Erro ao criar tabelas: {e}")
                messagebox.showerror("Erro de Banco de Dados", f"Falha ao criar tabelas: {e}")
            finally:
                conn.close()

    def insert_horario(self, data, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova, codusuario=None):
        """Insere um novo registro de horário no banco de dados."""
        conn = self.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO HORARIOS (DATA, HORA_ENTRADA, ENTRA_ALMOCO, SAIDA_ALMOCO, HORA_SAIDA, SEMANA_PROVA, CODUSUARIO)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (data, hora_entrada, entra_almoco, saida_almoco, hora_saida, semana_prova, codusuario))
                conn.commit()
                return True
            except Error as e:
                print(f"Erro ao inserir horário: {e}")
                messagebox.showerror("Erro de Inserção", f"Falha ao inserir registro: {e}")
                return False
            finally:
                conn.close()

    def get_all_horarios(self):
        """Retorna todos os registros de horários do banco de dados."""
        conn = self.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT IDHORARIO, DATA, HORA_ENTRADA, ENTRA_ALMOCO, SAIDA_ALMOCO, HORA_SAIDA, SEMANA_PROVA FROM HORARIOS ORDER BY DATA")
                return cursor.fetchall()
            except Error as e:
                print(f"Erro ao buscar horários: {e}")
                messagebox.showerror("Erro de Leitura", f"Falha ao recuperar registros: {e}")
                return []
            finally:
                conn.close()

    def get_horario_id(self, idhorario):
        conn = self.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT IDHORARIO, DATA, HORA_ENTRADA, ENTRA_ALMOCO, SAIDA_ALMOCO, HORA_SAIDA, SEMANA_PROVA FROM HORARIOS WHERE IDHORARIO = ?", (idhorario,))
                return cursor.fetchone() # Retorna uma única tupla ou None
            except Error as e:
                print(f"Erro ao buscar horário por ID: {e}")
                messagebox.showerror("Erro de Leitura", f"Falha ao recuperar registro por ID: {e}")
                return None
            finally:
                conn.close()
        return None

    def update_horario(self, idhorario, updates):
        """Atualiza um registro de horário existente."""
        conn = self.connect()
        if not updates: 
            return True # Ou False, dependendo do comportamento desejado para nenhuma operação

        if conn:
            try:
                cursor = conn.cursor()
                set_clause = ", ".join([f"{column} = ?" for column in updates.keys()])
                values = list(updates.values())
                values.append(idhorario)
                cursor.execute(f"UPDATE HORARIOS SET {set_clause} WHERE IDHORARIO = ?", tuple(values))
                conn.commit()
                return True
            except Error as e:
                print(f"Erro ao atualizar horário: {e}")
                messagebox.showerror("Erro de Atualização", f"Falha ao atualizar registro: {e}")
                return False
            finally:
                conn.close()

    def delete_horario(self, idhorario):
        """Exclui um registro de horário do banco de dados."""
        conn = self.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM HORARIOS WHERE IDHORARIO = ?", (idhorario,))
                conn.commit()
                return True
            except Error as e:
                print(f"Erro ao deletar horário: {e}")
                messagebox.showerror("Erro de Exclusão", f"Falha ao deletar registro: {e}")
                return False
            finally:
                conn.close()


    def filtro_horas(self, ant_data, prox_data):
        conn = self.connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                               SELECT IDHORARIO, DATA, HORA_ENTRADA, ENTRA_ALMOCO, SAIDA_ALMOCO, HORA_SAIDA, SEMANA_PROVA FROM HORARIOS 
                               WHERE DATA BETWEEN ? AND ?
                               ORDER BY DATA
                """, (ant_data, prox_data))
                return cursor.fetchall()
            except Error as e:
                print(f"Erro ao buscar horários: {e}")
                messagebox.showerror("Erro de Leitura", f"Falha ao recuperar registros: {e}")
                return []
            finally:
                conn.close()
