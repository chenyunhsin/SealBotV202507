import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

from dotenv import load_dotenv
from app.models import SQLModel  # 如果你的 models 放在別處，請調整這行

# 讀取 .env
load_dotenv()

# Alembic 設定物件（來自 alembic.ini）
config = context.config

# 設定 sync DB 連線字串
config.set_main_option("sqlalchemy.url", os.getenv("SYNC_DATABASE_URL"))

# 設定 logging
fileConfig(config.config_file_name)

# metadata for 'autogenerate'
target_metadata = SQLModel.metadata

def run_migrations_offline():
    """Run migrations without a DB connection (generate SQL only)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations with a real DB connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
