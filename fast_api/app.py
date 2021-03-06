import json
from fastapi import FastAPI
from util import array_multiply
import asyncio

app = FastAPI(debug=False)


@app.get("/api-fast/multiply")
async def api_fast_multiply():
    results = await asyncio.gather(*[array_multiply(_) for _ in range(5)],
                                   return_exceptions=True)

    # with open("result_fast_api.json", "w") as fp:
    #     json.dump(results, fp)

    return {"message": "HELLO"}
