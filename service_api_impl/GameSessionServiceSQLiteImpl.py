import sqlite3
from dto.GameSession import GameSession
from dto.GameSessionGuess import GameSessionGuess
from main import constants


class GameSessionServiceSQLiteImpl:

    def __init__(self):
        self.db_connection = sqlite3.connect("wordle.db")
        self.db_connection.row_factory = sqlite3.Row
        self.create_tables_if_not_exist()
        self.create_game_session_sql_template = """
            INSERT INTO game_session(target_word) VALUES (:target_word)
        """
        self.get_game_session_sql_template = """
            SELECT id, target_word from game_session WHERE id = :id;
        """
        self.create_game_session_guess_sql_template = """
            INSERT INTO game_session_guess(game_session_id, guess_number, guess_word) 
            VALUES (:game_session_id, :guess_number, :guess_word)
        """
        self.get_number_guesses_for_game_session_template = """
            SELECT count(game_session_id) from game_session_guess WHERE game_session_id = :game_session_id;
        """
        self.get_guesses_for_game_session_template = """
            SELECT game_session_id, guess_number, guess_word from game_session_guess 
            WHERE game_session_id = :game_session_id
            ORDER BY guess_number asc;
        """

    def start_game_session(self, target_word):

        cur = self.db_connection.cursor()
        cur.execute(self.create_game_session_sql_template, {"target_word": target_word})
        game_session_id = cur.lastrowid
        self.db_connection.commit()
        cur.close()

        return game_session_id

    def get_game_session(self, game_session_id):

        cur = self.db_connection.cursor()
        result_set = cur.execute(self.get_game_session_sql_template, {"id": game_session_id})
        game_session_db_row = result_set.fetchone()
        game_session = GameSession(game_session_db_row["id"], game_session_db_row["target_word"])
        cur.close()
        return game_session

    def record_guess(self, guess_word, guess_number, game_session_id):

        cur = self.db_connection.cursor()
        cur.execute(self.create_game_session_guess_sql_template,
                    {"game_session_id": game_session_id, "guess_number": guess_number, "guess_word": guess_word})
        self.db_connection.commit()
        cur.close()

    def count_number_guesses_for_game_session(self, game_session_id):

        cur = self.db_connection.cursor()
        result_set = cur.execute(self.get_number_guesses_for_game_session_template,
                                 {"game_session_id": game_session_id})
        number_guesses_made = result_set.fetchone()[0]
        cur.close()
        return number_guesses_made

    def number_remaining_guesses(self, game_session_id):
        return constants.NUM_ALLOWED_GUESSES - self.count_number_guesses_for_game_session(game_session_id)

    def get_guesses_for_game_session(self, game_session_id):

        cur = self.db_connection.cursor()
        result_set = cur.execute(self.get_guesses_for_game_session_template, {"game_session_id": game_session_id})
        guesses_for_game_session_result_set = result_set.fetchall()
        guesses_for_game_session = []
        for row in guesses_for_game_session_result_set:
            guesses_for_game_session.append(GameSessionGuess(row["game_session_id"], row["guess_number"],
                                                             row["guess_word"]))
        cur.close()
        return guesses_for_game_session


    def create_tables_if_not_exist(self):

        create_game_session_table_sql = """
            CREATE TABLE IF NOT EXISTS game_session(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                target_word VARCHAR(5)
            );
        """

        create_game_session_guess_table_sql = """
            CREATE TABLE IF NOT EXISTS game_session_guess(
                game_session_id INTEGER, 
                guess_number INTEGER, 
                guess_word VARCHAR(5),
                FOREIGN KEY(game_session_id) REFERENCES game_session(id)
            );
        """

        cur = self.db_connection.cursor()
        cur.execute(create_game_session_table_sql)
        cur.execute(create_game_session_guess_table_sql)
        self.db_connection.commit()
        cur.close()





