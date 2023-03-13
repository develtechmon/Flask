function display() {
  var table = document.getElementById("userdata");
  var rows = table.getElementsByTagName("tr");
  var tickets, process, subject,question,topic,answer

  for (var i = 0; i < rows.length; i++) {
  rows[i].onclick = function(event) {
      if (!event.target.matches("#display")){event.preventDefault();}
      else{ 
      // Get the data from the clicked row
      var cells = this.getElementsByTagName("td");
      tickets  = cells[0].textContent;
      process  = cells[1].textContent;
      subject  = cells[2].textContent;
      question = cells[3].textContent;
      topic    = cells[4].textContent;
      answer   = cells[5].textContent;
      console.log(tickets,process,subject,question,topic,answer)
      }
      data = {
              'tickets'  : tickets,
              'process'  : process,
              'subject'  : subject,
              'question' : question,
              'topic'    : topic,
              'answer'   : answer
              };
    
      $.ajax({
      type: 'POST',
      url: '/open',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: function(response) {
          window.open(response.redirect_url, '_blank');
      }
      
      });
  }}
}

function edit() {
  var table = document.getElementById("userdata");
  var rows = table.getElementsByTagName("tr");
  var tickets, process, subject,question,topic,answer

  for (var i = 0; i < rows.length; i++) {
  rows[i].onclick = function(event) {
      if (!event.target.matches("#edit")){event.preventDefault();}
      else{ 
      // Get the data from the clicked row
      var cells = this.getElementsByTagName("td");
      tickets  = cells[0].textContent;
      process  = cells[1].textContent;
      subject  = cells[2].textContent;
      question = cells[3].textContent;
      topic    = cells[4].textContent;
      answer   = cells[5].textContent;
      console.log(tickets,process,subject,question,topic,answer)
      }
      data = {
              'tickets'  : tickets,
              'process'  : process,
              'subject'  : subject,
              'question' : question,
              'topic'    : topic,
              'answer'   : answer
              };
    
      $.ajax({
      type: 'POST',
      url: '/edit',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: function(response) {
          window.open(response.redirect_url, '_blank');
      }
      
      });
  }}
}


function reset(){
  var table = document.getElementById("userdata");
  var rows = table.getElementsByTagName("tr");
  for (var i = 0; i < rows.length; i++) {
  rows[i].onclick = "" 
  }
}

function opendata(){
  var table = document.getElementById("userdata");
  var rows = table.getElementsByTagName("tr");
  // var flag = document.getElementById("op").dataset.info;

  for (var i = 0; i < rows.length; i++) {
  rows[i].onclick = function(event) {

      if (!event.target.matches("#ok")){
          event.preventDefault();
      }
      else{ 
      // Get the data from the clicked row
      var cells = this.getElementsByTagName("td");
      var tickets = cells[0].textContent;
      var process = cells[1].textContent;
      var subject = cells[2].textContent;
      var description = cells[3].textContent;
      var topic = cells[4].textContent;
      var support = cells[5].textContent;
      console.log(tickets,process,subject,description,topic,support)}
      
      window.location.href = '/open?subject=' + subject;

  }}
  //location.reload()
}
// window.onload = opendata;

function test(){
var tickets  = document.querySelector("td:nth-of-type(1)");
var process  = document.querySelector("td:nth-of-type(2)");
var subject  = document.querySelector("td:nth-of-type(3)");
var question = document.querySelector("td:nth-of-type(4)");
var topic    = document.querySelector("td:nth-of-type(5)");
var answer   = document.querySelector("td:nth-of-type(6)");
tickets.classList.add("selected");

console.log(tickets.textContent, process.textContent, subject.textContent, question.textContent, topic.textContent, answer.textContent);
window.location.href = 'open.html?output=' + encodeURIComponent(output);

}

// This function to select data from table cell
function opendatax(){

// Get a reference to the table element
var table = document.getElementById("userdata");

// Add a click event listener to the table
table.addEventListener("click", function(event) {

  // Check if the clicked element is a table cell
if (event.target.tagName === "TD") {
  // Get the row data of the clicked cell
  var tickets = [];
  var process = [];
  var subject = [];
  var cells = event.target.parentElement.cells;

  //Here we iterate one time only from the cells column
  for (var i = 0; i < 1; i++) 
  {
  // rowData.push(cells[i].textContent);
  tickets.push(cells[0].textContent);
  process.push(cells[1].textContent);
  subject.push(cells[2].textContent);
  }

  var data = {
      tickets: tickets,
      process: process,
      subject: subject
  };
  
  // Convert the row data to JSON
  var json = JSON.stringify(data);
  
  // Do something with the JSON data
  console.log(json);
}
}
)}