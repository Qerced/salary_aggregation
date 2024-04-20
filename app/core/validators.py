from core.db import operations


KEY_MISSING_ERROR = 'Required keys are missing in the input data set'
AGGREGATION_TYPE_KEY_ERROR = 'Unknown aggregation type'
DATA_TYPE_ERROR = 'Input data must be a dictionary'

valid_keys = ['dt_from', 'dt_upto', 'group_type']


async def check_data(data):
    if not isinstance(data, dict):
        raise TypeError(DATA_TYPE_ERROR)
    if not all(key in data for key in valid_keys):
        raise KeyError(KEY_MISSING_ERROR)
    if operation := operations.get(data['group_type']):
        return data, operation
    raise KeyError(AGGREGATION_TYPE_KEY_ERROR)
