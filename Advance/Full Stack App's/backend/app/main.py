from fastapi import FastAPI
from app.api.routes.news import router as news_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI News Personalizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news_router, prefix="/api/news", tags=["News"])

@app.get("/")
def root():
    return {"message": "AI News Personalizer API Running"}