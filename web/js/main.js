"use strict";

//Table of investigations
let investigations = [];

//Function to get the id
function getId(id) {
    return document.getElementById(id);
}

// Function to confirm the add of an investigation
function confirmation() {
    event.preventDefault();
    let investigation = {
        name : getId("investigationName").value,
        state : "fonctionnal"
    }
    investigations.push(investigation);


    let id = getId("confirmation")
    id.innerHTML = "<p>The investigation <i>" + getId("investigationName").value + "</i>  been added</p>";

}

//Add investigation in investigation table
function investigationTable() {
    confirmation();
    let thead = getId("thead");
    thead.innerHTML = "<th>Name</th><th>Sate</th>";
    let tbody = getId("tbody");
    tbody.innerHTML = "";
    for(let i in investigations) {
        tbody.innerHTML += "<tr><td>" + investigations[i]["name"] + "</td><td>" + investigations[i]["state"] + "</td>";
    }



    return false;
}