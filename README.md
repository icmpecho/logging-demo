# Centralised Logging Demo
Demonstrate Centralised Logging with EFK stack (Elasticsearch Fluentd Kibana). The whole stack and the demo app can be run locally using `docker-compose`

The related presentation can be found [here](https://docs.google.com/presentation/d/1TFDdceqojs50WtXgthw2re9h_uXKEGkhkM2zuU1LgEE/edit?usp=sharing)

## How to run
### EFK

    # Running for the first time
    $ cd efk/
    $ docker-compose up -d

    # Check if everything is running
    $ docker-compose ps

    # See the logs
    $ docker-compose logs -f

    # Stopping Everything
    $ docker-compose stop

    # Start it up again
    $ docker-compose start

    # Tear down
    $ docker-compose down -v

### Demo App

#### Traditional
Demo app that log in traditional text format

#### Structured
Demo app that log in JSON format

    # Running for the first time
    $ cd structured/ # or traditional/
    $ docker-compose up -d
    
    # Scaling in and out
    $ docker-compose scale processor=10
    $ docker-compose scale processor=1

## Customising
### Fluentd
- Edit `efk/fluent/config/fluent.conf`
- While inside `efk/` directory. Run `docker-compose restart fluentd`

### Demo Apps
- Edit `main.py` in the app directory
- While inside app directory. Run `docker-compose restart`
