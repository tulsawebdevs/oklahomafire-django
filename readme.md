Oklahomafire Django App
====

This django app is self contained to plug into oklahomadata website to show the latest fires in oklahoma (and United States).

Installation Instructions
----

    1 git clone https://github.com/tulsawebdevs/oklahomafire-django.git oklahomafire
    2 pip install -r oklahomafire/requirements.txt
    3 add `oklahomafire` to settings INSTALLED_APPS
    4 add the following to top level `urls.py`
> url(r'^oklahomafire/', include('oklahomafire.urls')),

    5 run south migration `south migrate oklahomafire`
    6 setup cron job to run `./manage.py importfiredata`
    7 visit [oklahomadata.org] site

ToDo
----

  - write tests
