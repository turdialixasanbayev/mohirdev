# Mohirdev Clone (Django REST API)

> **Til:** O‘zbekcha (Uzbek).  
> **Author:** Turdiali Xasanbayev (@turdialixasanbayev)

Mohirdev platformasining backend kloni. Loyiha Django + Django REST Framework asosida kurslar, video darslar, kategoriyalar, teglar, layk/dislayk reaksiyalari, sharh/reytinglar, va kontakt shakli kabi funksionallarni taqdim etadi. Foydalanuvchilar telefon raqami orqali autentifikatsiya qilinadi va rollar (admin, o‘qituvchi, talaba va h.k.) asosida ruxsatlar boshqariladi.

> **Izoh:** README ushbu repozitoriydagi mavjud fayl tuzilmasi (`apps/`, `config/`, `manage.py`, `.env.example`, `requirements.txt`) va suhbatdagi talablaringizga tayangan holda yozildi. Ayrim endpointlar va nomlar sizning kodingizdan farq qilsa, README ichidagi TODO bo‘limlarini moslab yangilab qo‘ying.

---

## 📦 Texnologiyalar (Stack)

- **Python 3.11+** (tavsiya)
- **Django 4.x**
- **Django REST Framework**
- **drf-spectacular** (OpenAPI/Swagger hujjatlari) *— agar yoqsangiz, `yasg` o‘rniga tavsiya etiladi*
- **django-filter** (filtrlash)
- **django-ckeditor** (rich text maydonlar)
- **phonenumber-field / phonenumbers** (telefon raqami validatsiyasi)
- **PostgreSQL** (tavsiya) yoki SQLite (dev)
- **Redis/Celery** (agar fon vazifalari zarur bo‘lsa — ixtiyoriy)

> Aniq versiyalar `requirements.txt` faylida.

---

## 🗂️ Projekt tuzilmasi

```
mohirdev/
├─ apps/
│  ├─ user/                # CustomUser, role management, phone login
│  ├─ course/              # Course, VideoLesson, Category (parent-child)
│  ├─ reaction/            # Like/Dislike
│  ├─ review/              # Review + Rating
│  ├─ tag/                 # Tags
│  └─ contact/             # ContactUs form
├─ config/                 # settings, urls, wsgi/asgi
├─ manage.py
├─ requirements.txt
└─ .env.example
```
> Eslatma: `apps/` ichidagi app nomlari siznikidan farq qilsa, moslab o‘zgartiring.

---

## 🚀 Tez start (Local)

### 1) Muhitni tayyorlash
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2) `.env` fayli
`.env.example` asosida `.env` yarating va quyidagilarga o‘xshash qiymatlarni to‘ldiring:

```
# Django
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost

# Database (PostgreSQL tavsiya)
DB_NAME=mohirdev
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=127.0.0.1
DB_PORT=5432

# DRF/Autht
DEFAULT_PAGE_SIZE=10

# Media/Static
MEDIA_ROOT=media
STATIC_ROOT=staticfiles

# Phone auth
DEFAULT_COUNTRY=UZ
```

### 3) Migratsiyalar va superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4) Serverni ishga tushirish
```bash
python manage.py runserver
```

---

## 🔐 Autentifikatsiya & Rollar

- **CustomUser**: telefon raqami (unique) orqali login.  
- **Role-based access**: (misol) `Admin / Teacher / Student` yoki siz belgilagan rollar.  
- DRF **permission** va **throttling** moslamalari bilan API himoyalanadi.

> TODO: Agar `JWT` ishlatayotgan bo‘lsangiz, `djangorestframework-simplejwt` sozlamalari va login/refresh endpointlarini shu yerga qo‘shing.

---

## 📚 API Hujjatlari

Agar `drf-spectacular` bo‘lsa, odatda quyidagilar bo‘ladi:

- OpenAPI schema: `/api/schema/`
- Swagger UI: `/api/docs/`
- ReDoc: `/api/redoc/`

> TODO: Loyihangizdagi haqiqiy URL-larni shu yerda yangilang.

---

## ✨ Asosiy imkoniyatlar

- **Kurslar**: yaratish, yangilash, o‘chirish, ro‘yxatlash, detail.
- **Video darslar**: kurslarga biriktirish, ko‘rish tartibi.
- **Kategoriyalar**: `parent-child` tuzilma (cheksiz chuqurlik emas — root -> child lar).
- **Teglar**: kurslarni teglar bilan belgilash/filtrlash.
- **Reaksiyalar**: Like/Dislike (bir foydalanuvchi-bitta reaktsiya qoidasi).
- **Sharh/Rating**: foydalanuvchi fikrlari va ball berish.
- **ContactUs**: foydalanuvchilar murojaatini qabul qilish.
- **Savatcha/Wishlist**: (agar kiritilgan bo‘lsa) kurslarni saqlab qo‘yish va xarid jarayoni.
- **Admin**: Django admin orqali barcha obyektlarni boshqarish.

---

## 🔧 Ishlab chiquvchi uchun qulayliklar

- **Pre-commit** (ixtiyoriy): `black`, `isort`, `flake8` ni ulash tavsiya.
- **.env.example** mavjud — tez start uchun.
- **docker-compose** (agar qo‘shilsa): dev/prod konfiguratsiyalarini soddalashtirish.
- **Testing**: `pytest` yoki `unittest` bilan asosiy testlar (TODO).

---

## 🧪 Namuna so‘rovlar (curl)

> URL va maydon nomlarini sizning implemetatsiyangizga moslang.

```bash
# Login (agar JWT bo‘lsa)
curl -X POST http://127.0.0.1:8000/api/auth/login/   -H "Content-Type: application/json"   -d '{"phone_number":"+998901234567","password":"your-pass"}'

# Kurslar ro‘yxati
curl http://127.0.0.1:8000/api/courses/

# Kursga layk berish
curl -X POST http://127.0.0.1:8000/api/courses/42/like/
```

---

## 🗺️ Roadmap

- [ ] Swagger/Redoc URL-larini yakuniy qilish
- [ ] JWT auth (agar kerak bo‘lsa) va refresh flow hujjatlari
- [ ] CI/CD (GitHub Actions)
- [ ] Docker (dev/prod) qo‘shish
- [ ] Test coverage oshirish
- [ ] Caching (Redis) va permission optimizatsiyasi

---

## 🤝 Hissa qo‘shish (Contributing)

1. Fork + yangi branch: `feat/xyz` yoki `fix/bug-123`
2. Kod uslubi: `black`, `isort`, `flake8`
3. Pull Request oching — izohda o‘zgarishlarni qisqacha yozing

---

## 📄 Litsenziya

Bu loyiha ochiq manbali. (TODO: MIT/Apache-2.0 dan birini tanlang va LICENSE fayl qo‘shing.)

---

## 🆘 Muammo/aloqa

Agar xatolik topsangiz yoki taklif bo‘lsa: Issues bo‘limida yozib qoldiring.

— Rahmat!
