import bson
from datetime import datetime

from core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient

FTIME = '%Y-%m-%dT%H:%M:%S'


db = AsyncIOMotorClient(settings.mongodb_url)[settings.db_name]

operations = {
    'month': {'operator': '$month', 'format': '%Y-%m-%dT00:00:00'},
    'week': {'operator': '$week', 'format': '%Y-%m-%dT00:00:00'},
    'day': {'operator': '$dayOfYear', 'format': '%Y-%m-%dT00:00:00'},
    'hour': {'operator': '$hour', 'format': '%Y-%m-%dT%H:00:00'}
}


async def setup_db():
    if settings.salary_table not in await db.list_collection_names():
        with open(settings.dump_file, 'rb') as f:
            await db[settings.salary_table].insert_many(
                bson.decode_all(f.read())
            )


async def get_aggregated_salary(data, operation):
    results = await db.salary.aggregate([
        {'$match': {
            'dt': {
                '$gte': datetime.strptime(data['dt_from'], FTIME),
                '$lte': datetime.strptime(data['dt_upto'], FTIME)
            }
        }},
        {'$group': {
            '_id': {operation['operator']: '$dt'},
            'date': {
                '$first': {
                    '$dateToString': {
                        'format': operation['format'], 'date': '$dt'
                    }
                }
            },
            'value': {'$sum': '$value'}
        }},
        {'$sort': {'date': 1}}
    ]).to_list(None)
    return {
        'dataset': [doc['value'] for doc in results],
        'labels': [doc['date'] for doc in results]
    }
