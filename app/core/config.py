import os
from pathlib import Path

DB_URL = 'mongodb://{user}:{password}@{host}:{port}/'


class Settings:
    base_dir = Path(__file__).parent.parent
    dump_file = base_dir.joinpath('dump/sampleDB/sample_collection.bson')
    db_name = 'sample_db'
    salary_table = 'salary'
    bot_name = 'my_bot'
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    bot_token = os.getenv('BOT_TOKEN')

    @property
    def mongodb_url(self):
        return DB_URL.format(
            user=os.getenv('MONGO_INITDB_ROOT_USERNAME'),
            password=os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )


settings = Settings()
