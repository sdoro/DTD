
## storyBoard

### init environment

    # make a github.com repository DTD (Django Template Development)
    # make a c9.io workspace linked to gihub.com above repository
    # make a requirements.txt file
    # make a README.md stoyboard file
    virtualenv $HOME/.environment
    source $HOME/.env/bin/activate
    pip install -r requirements.txt
    git add README.md requirements.txt
    git commit -m "Init environment."
    git push -u origin master

### make a project

    django-admin.py startproject mycompany
    cd mycompany
    ./manage.py runserver $IP:$PORT
    git add ../README.md .
    git commit -m "Add new project."
    git push
