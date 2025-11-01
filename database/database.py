# database.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------
# Use DIRECT_URL for ORM + async
# -----------------------
DATABASE_URL = os.getenv("DATABASE_URL",)

# ✅ Async engine for SQLAlchemy ORM
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Set True for debugging SQL queries
)

# Async session factory
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for ORM models
Base = declarative_base()
