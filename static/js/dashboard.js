
function updateClock(){

const now = new Date();

const time = now.toLocaleTimeString("fa-IR");

const date = now.toLocaleDateString("fa-IR",{

weekday:"long",
year:"numeric",
month:"long",
day:"numeric"

});

document.getElementById("clock").innerHTML = time;

document.getElementById("date").innerHTML = date;

}

updateClock();

setInterval(updateClock,1000);