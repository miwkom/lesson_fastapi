import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import uvicorn
from fastapi import FastAPI

from src.api.hotels import router as hotel_router
from src.api.auth import router as auth_router
from src.api.rooms import router as rooms_router
from src.api.bookings import router as bookings_router
from src.api.facilities import router as facilities_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(hotel_router)
app.include_router(rooms_router)
app.include_router(facilities_router)
app.include_router(bookings_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
