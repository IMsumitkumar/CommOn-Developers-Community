
<!-- BADGES AREA -->
[![GitHub issues](https://img.shields.io/github/issues/IMsumitkumar/CommOn-Developers-Community?style=flat-square)](https://github.com/IMsumitkumar/CommOn-Developers-Community/issues)
[![GitHub forks](https://img.shields.io/github/forks/IMsumitkumar/CommOn-Developers-Community?style=flat-square)](https://github.com/IMsumitkumar/CommOn-Developers-Community/network)
[![GitHub stars](https://img.shields.io/github/stars/IMsumitkumar/CommOn-Developers-Community?style=flat-square)](https://github.com/IMsumitkumar/CommOn-Developers-Community/stargazers)
[![GitHub license](https://img.shields.io/github/license/IMsumitkumar/CommOn-Developers-Community?style=flat-square)](https://github.com/IMsumitkumar/CommOn-Developers-Community/blob/main/LICENSE)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="arrow-down.png" alt="Logo" width="70" height="70">
  </a>
  <h3 align="center">CommOn Developer Community</h3>

  <p align="center">
    <a href="">Demo</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Overview](#overview)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
  * [Run](#run)
  * [Installation errors](#installation-errors)
* [Directory Tree](#directory-tree)
* [Contributing](#contributing)
* [Team](#team)
* [License](#license)
* [Contact](#contact)
* [References](#references)
* [Credits](#credits)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- IMAGE -->
![main page](https://i.imgur.com/L47p5K3.png)

### Overview

- The main purpose of this project is to cluster all the user according to similiar domain(web developement, data science, django framework etc.) so that experienced in the perticular domain can contribute and help each other in `real time` ⌛.
- These rooms are predefined by the admin and the group is also managed by the admin.
- User's can leave the group anytime and can join one core room anytime.
- For now one user can only join group at a time.
- User's can make their own room and can chat in Realtime and anyone can join them.
- In core rooms, No one can abuse, insult or hate anyone🤫. If anyone abuses than bot will warn that user.
- In Core rooms, No one can ask meta question like below. So that conversation can be clean, informative and meaningful and problem can be solved in realtime and lesstime.
    ```
    1. Any user of $X here?
    2. Anyone used technology $y?
    3. whrer are you from ?
    ```
- User can ask question and save their answer (conversation) of that perticular question so that helpful for others in future.
- users can ask for team by filling team recruitment form and can add a individual in project dashboard by username (in developement phase).
- posts(according to the domain) can be added by the admin of the core room which can be benificial for user's to learn a new thing everyday realted to their intresting domain.
- profile / update profile / login / signup / password recovery 👍.
- project is in developement phase. there is a lot more to do.


### Built With

[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/64/000000/python.png"/>](https://www.python.org/)
[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/64/000000/html-5.png"/>](https://www.w3schools.com/html/)
[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/48/000000/css3.png"/>](https://www.w3schools.com/css/)
[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/48/000000/javascript.png"/>](https://www.w3schools.com/js/DEFAULT.asp)
[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/48/000000/linux.png"/>](https://www.linux.org/)
[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/48/000000/django.png"/>](https://www.djangoproject.com/)
[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/48/000000/sql.png"/>](sqhttps://www.mysql.com/l)
[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/fluent/48/000000/github.png"/>](https://github.com)
[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/48/000000/docker.png"/>](https://www.docker.com/)
[<img align="left" alt="sumit" width="33px" src="https://img.icons8.com/color/50/000000/redis.png"/>](https://www.docker.com/)
[<img align="left" alt="sumit" width="45px" src="https://raw.githubusercontent.com/explosion/spaCy/45c9a688285081cd69faa0627d9bcaf1f5e799a1/website/src/images/logo.svg"/>](https://redis.io/)


<br>
<br>
 Scikit learn


<br/>
<br/>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.
make sure [git](https://git-scm.com/downloads) is installed in yout machine.

### Installation

1. Clone the repo
```sh
git clone https://github.com/IMsumitkumar/CommOn-Developers-Community
```
2. create a virtual env and activate
```bash
conda create -n <env_name> python=3.7
conda activate <env_name>
```
2. Install dependencies
```bash
pip install -r requirements.txt      -      (inside project directory)
```

### RUN

> STEP 1 : Migrate the databse tables and create superuser

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

    username : *****
    email    : *****
    password : ******
```
> STEP 2 : Install Docker
- for linux
```
Install directly from store
```

- for windows and mac users
```
https://www.youtube.com/watch?v=CYyUCJad954
```

> STEP 3: start a redis server on port 6379 using docker
```
docker run -p 6379:6379 -d redis:5
```

> STEP 4
```python
python manage.py runserver
```

> STEP 5 : setting up rooms
```
1. Go to 127.0.0.1:8000/admin or localhost:8000/admin
2. Select groups in AUTHENTICATION AND AUTHORIZATION section
3. click on ADD Group
4. add (CP, DS, WD) one by one
```
![Groups selection image](https://i.imgur.com/AuZpMHQ.png)


### Installation errors

`en_core_web_sm module not found`

```
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz --no-deps
```

## Directory Tree 
```
├── common 
│   └─────────── # main folder contains wsgi, routing, settings and urls.
├── common_app
│   └─────────── # handles login, signup and password recovery. 
├── notes 
│   └─────────── # nothing much just a template..
├── project_manag
│   └─────────── # handles project management opeations.
├── QnA
│   └─────────── # QnA dashboard- questions comming from student_gp
├── recruit_team
│   └─────────── # handles recruit team forms.
├── student_gp
│   └─────────── # handles multiple async chat comsumers (rooms)
├── user_group
│   └─────────── # users can create multiple rooms.
├── user_profile
│   └─────────── # profile and updation of profile
├── templates
│   └─────────── # contains landing page templates
├── media
│   └─────────── # contains uploaded media (profile photos etc)
├── static
│   └─────────── # contains static files
├── manage.py
├── arrow-down.png
├── requirements.txt
├── LICENSE
├── README.md
└── db.sqlite3

```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Team
[![Sumit Kumar](https://img.icons8.com/color/48/000000/linux.png)]() |
-|
[Sumit](https://github.com/IMSumitKumar) |)


<!-- LICENSE -->
## License
![APM](https://img.shields.io/apm/l/vim-mode?color=blue&style=for-the-badge)

Copyright 2020 Sumit Kumar

<!-- CONTACT -->
## Contact

Sumit Kumar - email me @[sksumit068@gmail.com](https://mail.google.com/)

Project Link: [https://github.com/IMsumitkumar/CommOn-Developers-Community](https://github.com/IMsumitkumar/CommOn-Developers-Community)

## References

- https://www.djangoproject.com/
- https://www.django-rest-framework.org/
- https://channels.readthedocs.io/en/stable/
- https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg
- https://stackoverflow.com/questions/49964028/spacy-oserror-cant-find-model-en

## Credits
- HTML templates are being used from open source.
- Modificatons are made by me.