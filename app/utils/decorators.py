import json
from functools import wraps
from typing import Union
from pydantic import BaseModel
from loguru import logger


def generic_repr(_func=None, *, phrase: Union[str, None] = None, position: int = 0):
    """Create generic representation of a pydantic model."""
    
    if isinstance(_func, str):
      raise ValueError('Only keyword arguments is supported.')
    
    def decorator_generic_repr(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            item = [item for item in args if isinstance(item, BaseModel)]
            model = None

            if len(item) > 0:
                model = item[position]

            if model:
                model_to_dict = model.dict()
                if phrase:
                    logger.info(f'{phrase}: {json.dumps(model_to_dict)}')
                else:
                    logger.info(f'{json.dumps(model_to_dict)}')
            return func(*args, **kwargs)
        return wrapper


    if not _func:
        return decorator_generic_repr
    return decorator_generic_repr(_func)



