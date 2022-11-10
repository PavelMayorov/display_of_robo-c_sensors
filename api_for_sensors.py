import random

from fastapi import FastAPI, Response


app = FastAPI()


@app.get('/')
async def handler(response: Response):
    response.headers["access-control-allow-origin"] = "*"
    data = {
        # 'temp_sense': f'{random.uniform(23.00, 30.00):5.2f}',
        'temp_sense': '23.4',
        'pres_sense': f'{random.uniform(0.00, 30.00):5.1f}',
        # 'pres_sense': 0,
    }
    return data
