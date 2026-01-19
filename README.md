# School API

## Rebuild Guide (From Scratch)

### Build List

* student_app -> Student model + validators + student endpoints
* class_app -> Class model + validators + class endpoints
* grade_app -> Grade model + validators + grade endpoints

1. Models + validators + clean() rules
2. Migration and DB setup
3. Endpoints

Endpoints:
 revers("all_students") -> returns list of students (fixture style)
 revers("all_classes") -> returns list of classes (fixture style)
 /api/v1/students/<pk>/ -> nested student detail format
 /api/v1/classes/<subject>/ -> nested class detail format

## Project Setup

01. Create Repo + venv
01.1 Start Project + apps

## Part I - Configure Django

1.1 settings.py : Installed apps
1.2 Database config (Postgres in Docker)
school_proj/settings.py

Notion Reference for code: 

## Part II - Models + Relationships (Student, Class, Grade)

2.1 Student model requirements
/student_app/models.py
/student_app/student_model_reqs.md

2.2 Class model requirements
/class_app/models.py
/class_app/class_model_reqs.md

2.3 Grade model requirements
/grade_app/models.py
/grade_app/grade_model_reqs.md

## Part III - Validators
  * each app has validators
3.1 student_app/validators
3.2 class_app/validators
3.3 grade_app/validators

### Validator Code Snippet
...
import re
from django.core.exceptions import ValidationError
from django.code.validators import MinValueValidator, MaxValueValidator

def validate_something(value:str):
    # Example: "John W. Watson " must be First M. Last format 
    if not match(pattern, value):
        raise ValidationError("Name must be in 'First M. Last' format.")
...

## Part IV - Build Models 
** KEY RULE ** 
- In Student, references Class using string: "class_app.Class"
- In Class, references Student using string: "student_app.Student"

## Part V - Migrations
...
    python manage.py makemigrations
    python manage.py migrate

...

## Part VI - API Endpoints (API 1-6)
### What tests usuall expect 
Two "list" endpoints user reverse() names:
* reverse("all_classes") -> AllClasses CBV
* reverse("all_students") -> AllStudents CBV

API 6 "detail" endpoints
* /api/v1/students/<pk>/
* /api/v1/classes/<subject>/

## Part VII - URL Wiring
7.1 school_proj/urls.py
7.2 school_proj/api_urls.py  (details endpoints)


## PART VII - List Endpoints (reverse names)
8.1 class_app/urls.py
8.2 student_app/urls.py

NOTE: Do NOT SET APP_NAME in these urls.py if tests do reverse("all_classes")
without namespace Example student_app = "student_app"

## PART IX - List Views
9.1 class_app/views.py
9.2 student_app/views.py

## PART X - API 6 Detail View (FBV)
10.1 student_app/api_views.py
10.2 class_app/api_views.py

## PART XI - Admin Setup
...
python manage.py createsuperuser
...

Register models:
student_app/admin.py
class_app/admin.py



