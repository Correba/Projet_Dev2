"use strict";

eel.expose(getFormInfos);
eel.expose(addElement);

document.addEventListener('DOMContentLoaded', eel.fill_table_investigations);
document.addEventListener('DOMContentLoaded', eel.fill_type_forms)
document.addEventListener('DOMContentLoaded',  setMaxDate)

function getFormInfos(){
    eel.create_investigations(getId('investigationName').value);
}

function addElement(id, html){
    getId(id).innerHTML = html;
}

function setMaxDate() {
    let today = new Date();
    let day = today.getDate();
    let month = today.getMonth() + 1; //January is 0!
    let year = today.getFullYear();

    if (day < 10) {
        day = '0' + day;
    }
    if (month < 10) {
        month = '0' + month;
    }
    document.querySelectorAll('input[type="date"]').forEach(x => x.setAttribute("max", `${year}-${month}-${day}`));
}

/*
//Table of investigations

let investigations = [];

// Function that add an investigation in the investigation table and confirms it
function confirmationInvestigation() {

    let investigation = {
        "name": getId("investigationName").value,
        "proofs": [],
        "persons": {},
        "state": "fonctionnal"
    }
    investigations.push(investigation);


    let confirmationInvest = getId("confirmation_investigation")
    confirmationInvest.innerHTML = "<p>The investigation <i>" + getId("investigationName").value + "</i>  been added</p>";

}

//Creates the table of the investigations
function createTabInvest() {
    let thead = getId("theadInvest");
    thead.innerHTML = "<th>Name</th><th>Proof(s)</th><th>Person(s)</th><th>Sate</th>";
    let tbody = getId("tbodyInvest");
    tbody.innerHTML = "";
    for (let i in investigations) {
        tbody.innerHTML += "<tr id='" + investigations[i]["name"] + "'><td>" + investigations[i]["name"] + "</td><td onclick=\"createTabProofs('" + investigations[i]["name"] + "')\">" + investigations[i]["proofs"].length + "</td><td>" + Object.keys(investigations[i]["persons"]).length + "</td><td>" + investigations[i]["state"] + "</td>";
    }
}


//Confirms the add of the investigation, reset invetigation table and add investigation in list of form for the proofs
function addInvestigation() {
    //Confirms the add of the investigation in the investigation table
    confirmationInvestigation();

    //Creates the table of investigations
    createTabInvest();

    //Create the list of investigations for encoding the proofs after
    let inputSelect = getId("investigation_select");
    inputSelect.innerHTML = "<option>--Please choose an option--</option>"
    for (let a in investigations) {
        inputSelect.innerHTML += "<option value=" + investigations[a]["name"] + ">" + investigations[a]["name"] + "</option>"
    }
}

//Function that add the proof(s) in the right investigation and confirms it
function confirmationProof() {
    for (let i in investigations) {
        if (investigations[i]["name"] === getId("investigation_select").value) {
            investigations[i]["proofs"].push(getId("proofsName").value)
        }
    }

    let confirmationProof = getId("confirmation_proof");
    confirmationProof.innerHTML = "<p>The proofs are added</p>";
}


function createTabProofs(investName) {
    let titleProofTable = getId("title_proof_table");
    titleProofTable.innerHTML = "Tab where all the proofs are displayed";

    let tbody = getId("tbodyProof");
    tbody.innerHTML = "";
    for (let a in investigations) {
        if (investigations[a]["name"] === investName) {
            let count = 1;
            for (let x in investigations[a]["proofs"]) {
                tbody.innerHTML += "<tr></tr><th>Proof " + count + " : </th><td>" + investigations[a]["proofs"][x] + "</td>";

                tbody.innerHTML += "</tr>";
                count += 1;
            }
        }
    }
}

//Confirms the add of the proof in the right investigation, confirms it, reset investigation table and reset proof table
function addProof() {
    //Confirms the add of the proof(s) in the right investigation
    confirmationProof();

    //Creates the table of investigations
    createTabInvest();
    //console.log(investigations);


}


//Add persons in the right investigation
function addPerson() {

}
 */
