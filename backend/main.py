from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, users, items, outlets

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(outlets.router, prefix="/outlets", tags=["Outlets"])

@app.get("/")
def root():
    return {"status": "200", "message": "Laundry Inventory API is running"}

