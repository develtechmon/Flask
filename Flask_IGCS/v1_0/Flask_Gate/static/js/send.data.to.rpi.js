var url = "http://10.60.215.170:80/api"

document.getElementById("OPE").addEventListener("submit", function(event) {
    // prevent the form from submitting in the usual way
    event.preventDefault();
    
    // make AJAX request to submit form data in the background
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        // handle the response from the server, if necessary
        console.log(this.responseText);
    }
    };
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    
    // To send multiple data
    //xhttp.send("param1=OPEN&param2=open");

    // To send single data
    xhttp.send("param1=open");
});

document.getElementById("PAU").addEventListener("submit", function(event) {
    // prevent the form from submitting in the usual way
    event.preventDefault();
    
    // make AJAX request to submit form data in the background
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        // handle the response from the server, if necessary
        console.log(this.responseText);
    }
    };
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    // To send multiple data
    //xhttp.send("param1=PAUSE&param2=pause");
    
    // To send single data
    xhttp.send("param1=pause");
});

document.getElementById("CLO").addEventListener("submit", function(event) {
    // prevent the form from submitting in the usual way
    event.preventDefault();
    
    // make AJAX request to submit form data in the background
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        // handle the response from the server, if necessary
        console.log(this.responseText);
    }
    };
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    // To send multiple data
    //xhttp.send("param1=CLOSE&param2=close");

    // To send single data
    xhttp.send("param1=close");
    
});