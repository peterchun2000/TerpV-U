var phoneUserCount = 0; // its 0 by default. It either increases or decreases, depending on whether users pull out their phones or puts them away.

var timesArray = []; // This array will store the times users used their phones in the form of hr:min

function incr_Users(){
    phoneUserCount++;
    // var timeTargets = new Date();
    // var Hour = timeTargets.getHours();
    // var Minute = timeTargets.getMinutes();
    // var Second = timeTargets.getSeconds();
    // timesArray.push([Hour, Minute, Second]);
    document.getElementById("phoneUserCount").textContent = "Usage Count: " + phoneUserCount;
    // console.log(timesArray);
}


/*
function getTimeList(){
    for(var i = 0; i < timesArray.length; i++){
        document.getElementById("timeTable").innerHTML += "<tr> <td>" + timesArray[i] + "</td> </tr>";
        //document.getElementById("timeList").innerText += timesArray[i].toString(); //innerText works better than textContent when it comes to adding html
        //document.getElementById("timeList").innerHTML += "<br>";
    }
    //document.getElementById("timeList").textContent += (timesArray.toString() + "\n");
}
*/