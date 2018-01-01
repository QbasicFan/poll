# poll
basic poll app

basic django app to generate basic color pallette for menu , bady and footer

1)

2) install in settings.py
at 

################
# APPLICATIONS #
################

INSTALLED_APPS = (
    "poll",
...

3) add route in base urls.py
  url("^poll/", include("poll.urls")),


