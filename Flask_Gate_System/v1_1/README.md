# Internet Gate Control System

## Start
```
$sudo python3 app.py - For website server
$sudo python3 app_rpi_client_get_api_2nd_method.py - For rpi gate relay

```

## Gate service installation into RPI
```
$crontab -e

and below command

@reboot sudo /usr/bin/python3 /home/jlukas/Desktop/My_Project/Flask/Flask_Gate_System/v1_1/app_rpi_client_get_api_2nd_method.py &

$sudo reboot now

```

## Website Link
[Internet Gate Control System (ICGS)](http://develtechmon.pythonanywhere.com/home)