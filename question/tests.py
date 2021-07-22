from django.test import TestCase
import requests
# Create your tests here.

# python question/tests.py
base_url = "http://127.0.0.1:8000/viewset/question/"
create_url = "http://127.0.0.1:8000/viewset/question/create_question/"
update_url = "http://127.0.0.1:8000/viewset/question/1/update_question/"


def create():
    ques={
        "ques_title": "배고플 때",
        "post_date": "2021-07-03T00:40:17.792045Z",
        "modify_date": "2021-07-03T04:54:35.468275Z",
        "ques_desc": "어떻게 해야하나요?",
        "ques_point": 1200,
        "head_img": None,
        "vote_count": 0,
        "user_id": 1,
        "category_id": None,
        "who_chosen": 3
    }
    data = requests.post(create_url, data=ques)
    print(data)


def update():
    ques={
        "ques_title": "배고플 때!!!!",
        "post_date": "2021-07-03T00:40:17.792045Z",
        "modify_date": "2021-07-03T04:54:35.468275Z",
        "ques_desc": "어떻게 해야하나요?",
        "ques_point": 1500,
        "head_img": None,
        "user_id": 1,
        "category_id": None,
        "who_chosen": 3
    }
    data = requests.post(update_url, data=ques)
    print(data)


if __name__ == '__main__':
    update()
