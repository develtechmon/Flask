# Hotline Wikipidea Discussion
## Date : 21/3/2023

1. Deployment method
```
Question
a. Using My X-Fab container
Question : Is it able to run Flask server ?

Suggested method:
a. Docker and deploy in a server (Gunicorn and etc)

Internal
1. deploy in x-fab server
2. --> export as json file (can be shared with customer)
3. Note Here 
   a. Backend - use elastic output to generate html(?), pdf and etc
   b. Front End - 

elastic - hotlinefaq -> xdocgen -> generate html/pdf -1 
                     -> xdocgen -> json/file -2 

FAQ container 
a. index.html
   -> request (elastic) external (doesnt work) - api token (My X-Fab server) -x

b. index.html
   -> read the data from -2
   -> 

c. PDF
   -> 

Conclusion:
recommendation : use PDF as it's xdocgen
alternatively : html (css, js)

External
1. Static html
2. ajax script (downloaded json file above)

Integration FAQ + CTS (Next Generation CTS)
1. use FAQ PDF as it's.

```

2. Demo, Flow and impression feedback
```
Bear in mind, this is still in very early development. 
Feedback and advise are most welcome.

```

3. Customer Front End part
```
Discuss about the layout and feature we want to show
```