# Sharing_knowleadge

# URL
[OG-LAB](http://www.og-lab.net/)

# 통합 브랜치 
* main

# 토픽 브랜치
* user - 승훈님
* category - 예은님
* question - 승환님
* answer - 예은님
* university - 채호님
* company - 채호님


## 초기화
* `git clone https://github.com/Dltmd202/Sharing_knowleadge`
* `python -m venv venv`
* `source venv/Scripts/activate`
* `cd sharing_Kowleadge`  
* `git branch [브랜치 이름]`
* `git checkout [브랜치 이름]`
* `git push -u origin [브랜치 이름]`

## 필요한 것들
* `pip install django`
* `pip install pillow`
* `pip install django-formtools`
* `pip install djangorestframework`
* `pip install markdown`
* `pip install django-allauth`
* `pip install django-cors-headers`
* `pip install django-filter`
* `pip install django-hitcount`
* `pip install pip --upgrade`
* `pip install -r requirements.txt`
* `pip install django-markdown-deux`

  
## 개발
* `source venv/Scripts/activate`
* developing~~
* `git add [파일]`
* `git commit -m "Commit Message"`
* `git push`

## 주의사항
* 커밋 메세지는 한글로 한가지의 역할만을 반영하여 작성해주세요!
* 자신이 수정한 파일만 지정해서 `staging area`에 반영해 주세요!  
* `git pull origin main` 명령어는  수정된 파일이 commit 되어 있지않으면 작동하지
    않습니다. 자신의 코드가 모두 원격 저장소에 올라가 있다고 생각한다면 `git fetch --all`, `git reset --hard origin/main`
    으로 원격 저장소의 main 브랜치와 동기화시켜주시기 바랍니다!
* `git push`가 작동하지 않는다면, branch를 정확히 확인해 주셨다는 가정 하에 `git push -f` 해주셔도 됩니다!   

## 서버 운용
* `python mange.py makemigrations`
* `python mange.py migrate`
* `python mange.py collectstatic`
* `python manage.py runserver`
