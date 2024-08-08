# Setup for Django (Week2)
- Django Installation


1. Set up Virtual Environment
[Install virtualenv]
> pip install virtualenv

[Create a virtual environment]
> py -m venv myvenv

[Activate virtual environment]
> myvenv\Scripts\activate.bat


2. Install Django
> pip install django


3. Creating Project
> django-admin startproject `pj_name`

[สำหรับเอาไว้ run server ทดสอบ]
> python manage.py runserver

[เปลี่ยน port ที่เอาไว้ run server]
> python manage.py runserver 8080


4. Create Apps
> python manage.py startapp `app_name`
- สร้างแล้ว ให้ไปเพิ่มชื่อ app ใน setting.py ด้วย
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Add your apps here
    "app_name", <--
]


5. Database Setup
[Check version Postgres]
> postgres --version

[Install Postgres]
> pip install psycopg2

- Install เสร็จแล้ว ให้ไปแก้ไฟล์ setting.py ด้วย (แก้ NAME, user, pass ด้วย)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mypolls",
        "USER": "db_username",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


6. Install Jupiter
> pip install django-extensions ipython jupyter notebook

[แก้ version package ของ jupiter, notebook]
> pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2

[แก้ version notebook]
> pip install notebook==6.5.7

[ไปเพิ่ม Installed Apps ใน Setting ด้วย]
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "django_extensions", <----
    "blogs",
]


[Start Jupiter Notebook Server]
> python manage.py shell_plus --notebook

[run cell นี้ก่อนทุกครั้ง เวลาจะใช้ Jupiter notebook]
> import os
> os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

[ถ้า run ไม่ได้ ลองเช็คใน notebook ว่าเปลี่ยน kernel เป็น django shell แล้วรึยัง]
[ถ้ายัง run ไม่ได้อีก ติด synchronus บลาๆ ให้ลอง run cell แรกใหม่อีกรอบ]

----------------------

[คำสั่ง Import?]
from django.db.models import *
from django.db.models.functions import *
from django.db.models.lookups import *

import json 
(print(json.dumps(dictionary, indent=4, sort_keys=False)))
from ชื่อapp.models import *

____________


# Week2 : View
1. View
description : ส่วนใหญ่จะเกี่ยวกับ View --> ไม่รู้ยังไง เดี๋ยวค่อยกลับมาเขียนต่อ


2. Creating Models -> เป็นเหมือนการสร้าง ตาราง (tables) ลงใน Database และแต่ละ field จะเป็น column ใน table

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

[ไม่ว่าจะแก้ไขอะไรกับ Models ต้อง makemigrations เสมอ]
> python manage.py makemigrations polls
> python manage.py migrate


3. วิธีเข้า python shell
> python manage.py shell

[ทำการ import models Question, Choice]
>>> from polls.models import Question, Choice

[ทำการ SELECT ข้อมูลในตาราง question (SELECT * FROM question)]
>>> Question.objects.all()
<QuerySet []>

[สร้าง instance ของ Question]
>>> from django.utils import timezone
>>> q = Question(question_text="What is new?", pub_date=timezone.now())

[บันทึกข้อมูลลงใน table question]
>>> q.save()

[ID ของ question ที่สร้าง = 1]
>>> q.id
1

[ตัวแปร q เป็น instance ของ class Question ดังนั้นจะมี attribute question_text, pub_date ซึ่งสามารถเข้าถึงได้โดยใช้ dot notation ของ Python]
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2024, 2, 26, 13, 0, 0, 115217, tzinfo=datetime.timezone.utc)

[แก้ไขข้อมูลเปลี่ยน question_text จาก "What's new?" -> "What's up?"]
[SQL: UPDATE question SET question.question_text="What's up?" WHERE question.id = 1]
>>> q.question_text = "What is up?"

[สั่ง save เพื่อบันทึกข้อมูลลง database]
>>> q.save()

[Question.objects.all() แสดงข้อมูลทั้งหมดในตาราง question]
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>


4. 
[แปลง obj เป็น dict]
> xxxxx.value()


____________


# Week4
1. Jupiter
[เวลาจะไปใช้ Jupiter ให้ import model ของตารางมาก่อนด้วย]
> from blogs.models import Blog

2. Field Lookups
[หลักการใช้ endwiths]
> `table_name`.objects.filter(`field_name`__endswith='features.')

[การใช้ order_by เพื่อเรียงลำดับผลลัพธ์]
ต้องใส่ '' ครอบชื่อ Field ด้วย, ถ้าอยากให้เป็น dasc -> เติม - ข้างใน เช่น '-id'
> Product.objects.filter(price__range=(101, 199)).order_by('id')

3. Add, Update, Delete Objects (อยู่ใน README.md)

[เวลา Add ลง Many-to-Many ให้ add ผ่านฝั่งที่เก็บ Field m-m]
> obj = xxx.objects.get(xxx='') <-- ใช้ get จะได้ออกมาเป็น obj พร้อมใช้
> new3.categories.add(elec) <-- แล้วค่อยไปยัดเข้า


____________


# Week5
1. Model Relationship
[Add obj ใหม่เข้าคสพ.แบบ one-to-one, one-to-many] -> ใส่ obj ตอน create ได้เลย ไม่ต้องไป add เหมือนตอนทำ Many-to-Many
[อ่านเพิ่ม model-relationships.md Week5]

[Value_list] Get only ids -> เลือกได้ว่าจะให้แสดงแค่ Field 'id'
>>> penguin_pub.book_set.filter(name__startswith="The").values_list("id", flat=True)
<QuerySet [2, 6, 9, 15, 18]>


2. Query Expression --> จะใช้ต้อง import ด้วยนะ
[annotate] -> เป็นการสร้าง Field เพิ่ม (แบบไม่ไปกระทบ db) เอาไว้คิด +-*
ex.
company = (Company.objects.filter(num_employees__gt=F("num_chairs"))
...     .annotate(`new_field_name`=F('`Field_name`') - F('`Field_name`')) <-- ใส่ ' ตรง Field name ด้วย!!!
...     .first()
... )
[Aggregate] -> ใช้กับพวก function Avg(), Sum(), Min(), Max()
- concat
> from django.db.models import CharField, Value as V
> from django.db.models.functions import Concat
> Concat('name', V(' ('), 'goes_by', V(')'))

- avg
> from django.db.models import Avg
> Book.objects.aggregate(Avg("price", default=0))

[Group by อะไรไม่รู้ของเฟรม] --> ใช้ values คู่กับ annotate โดยข้างในเป็น aggregate

> pro = Product.objects.filter(Q(categories__name = "Electronics")| Q(categories__name = "Jewelry")
, price__range=(8000, 50000)).values("categories__name").annotate(count = Count('id'))

> for i in pro:
    print(i['categories__name']+" "+str(i['count']))