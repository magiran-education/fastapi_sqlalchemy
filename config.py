from dotenv import load_dotenv
import os


# из файла .env экспортируем переменные в окружение системы
load_dotenv()


# из системы импортируем переменные в python
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
