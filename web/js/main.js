"use strict";

//Table of investigations
let investigations = [];

//Function to get the id
function getId(id) {
    return document.getElementById(id);
}

// Function that add an investigation in the investigation table and confirms it
function confirmationInvestigation() {
    event.preventDefault();
    let investigation = {
        "name" : getId("investigationName").value,
        "proofs" : [],
        "state" : "fonctionnal"
    }
    investigations.push(investigation);


    let confirmationInvest = getId("confirmation_investigation")
    confirmationInvest.innerHTML = "<p>The investigation <i>" + getId("investigationName").value + "</i>  been added</p>";

}

//Creates the table of the investigations
function createTabInvest() {
    let thead = getId("thead");
    thead.innerHTML = "<th>Name</th><th>Proof(s)</th><th>Sate</th>";
    let tbody = getId("tbody");
    tbody.innerHTML = "";
    for(let i in investigations) {
        tbody.innerHTML += "<tr><td>" + investigations[i]["name"] + "</td><td>" + investigations[i]["proofs"].length + "</td><td>" + investigations[i]["state"] + "</td>";
    }
}


//Add investigation in investigation table
function addInvestigation() {
    //Confirms the add of the investigation in the investigation table
    confirmationInvestigation();

    //Creates the table of investigations
    createTabInvest();

    //Create the list of investigations for encoding the proofs after
    let inputSelect = getId("investigation_select");
    inputSelect.innerHTML = "<option>--Please choose an option--</option>"
    for(let a in investigations) {
        inputSelect.innerHTML += "<option value=" + investigations[a]["name"] + ">" + investigations[a]["name"] + "</option>"
    }

}

//Function that add the proof(s) in the proof table and the right investigation, and confirms it
function confirmationProof() {
    event.preventDefault();

    for(let i in investigations) {
        if (investigations[i]["name"] === getId("investigation_select").value) {
            investigations[i]["proofs"].push(getId("proofsName").value)
        }
    }

    let confirmationProof = getId("confirmation_proof");
    confirmationProof.innerHTML = "<p>The proofs are added</p>"
}


//Add proof in proof table
function addProof() {
    //Confirms the add of the proof(s) in the right investigation
    confirmationProof();

    //Creates the table of investigations
    createTabInvest();
    console.log(investigations);
}