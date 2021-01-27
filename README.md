# Flaskweb Frame
Inspirated by springboot

# Structure
- ``wsgi.py`` launch the webserver
- ``app.py`` bootstrap file of the whole service
- demo: a micro service  
directories at the same level can also be created if there are other micro services
    - controller
    - service 
    - model
    - dao
- config: just configs...
- library: basic and universal tools or utilities
- requirements.txt: run ``pip install -r requirements`` to install every thing you need for this demo    
- ``gunicorn_config.py``: todo: convert from wsgi to gunicorn, a more powerful webserver for python
- logs: Writed down log and seperate them into several level is a good idea for a big and sophisticated system. I recommend using log.

# Todo
- docker containers
- dao level