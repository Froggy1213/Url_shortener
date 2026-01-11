import string
import secrets
from sqlalchemy.orm import Session
from . import models, schemas

# 1. Функция генерации случайной строки (ключа)
def create_random_key(length: int = 5) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

# 2. Функция создания записи в БД
def create_db_url(db: Session, url: schemas.URLCreate) -> models.URL:
    key = create_random_key()
    
    # Если ключ занят — генерируем новый (простая защита от коллизий)
    while get_db_url_by_key(db, key):
        key = create_random_key()

    db_url = models.URL(target_url=url.target_url, key=key)
    
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

# 3. Функция получения записи по ключу
def get_db_url_by_key(db: Session, url_key: str) -> models.URL:
    return db.query(models.URL).filter(models.URL.key == url_key).first()