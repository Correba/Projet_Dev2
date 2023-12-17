"use strict";

eel.expose(getFormInfos);
eel.expose(addElement);
eel.expose(clearElement);

document.addEventListener('DOMContentLoaded', load);
window.addEventListener('beforeunload', eel.log("Closing the app..."));

const logInv = "log_investigation";
const logEv = "log_evidence";
const logPe = "log_people";

function load(){
    eel.fill_investigations_table();
    eel.fill_type_forms();
    setMaxDate();
    getId('evidenceType').addEventListener('change', recordingValue);
    eel.log('App loaded');
}

async function getFormInfos(forms){
    const new_name = forms.investigationName.value;
    const new_status = forms.investigationStatus.value;
    let new_investigation = await eel.create_investigations(new_name, new_status)();
    addElement(logInv, new_investigation);
    getId(logInv).classList.add('ok');
}

function getId(id) {
    return document.getElementById(id);
}

function queryAll(selector){
    return document.querySelectorAll(selector);
}

function addElement(id, html){
    getId(id).innerHTML = html;
}

function clearElement(id){
    getId(id).innerHTML = '';
}

function setMaxDate() {
    const today = new Date().toISOString().split('T')[0];
    queryAll('input[type="date"]').forEach(inputDate => inputDate.setAttribute("max", `${today}`));
}

async function addEvidence(forms){
    const chosenType = forms.evidenceType.value;
    const chosenInvestigation = forms.evidence_select.value;
    const name = forms.evidenceName.value;
    const description = forms.evidenceDescription.value;
    const date = forms.evidenceDate.value; //yyyy-mm-dd
    const file = forms.evidenceFile.value;
    const data = [name, description, date, file];
    switch (chosenType) {
        case 'picture':
            data.push(forms.evidencePicture.value);
            break;
        case 'object':
            data.push(forms.evidenceObject.value);
            break;
        case 'recording':
            data[-1] = forms.evidenceRecording.value;
            break;
    }
    eel.log('Adding evidence...')
    let new_evidence = await eel.make_evidence(chosenType, chosenInvestigation, data)();
    if (new_evidence.includes('Invalid')){
        new_evidence = new_evidence.split(':')[1];
        getId(logEv).setAttribute('class', 'error');
        eel.log('Displaying evidence error...');
    } else {
        getId(logEv).setAttribute('class', 'ok');
    }
    addElement(logEv, new_evidence);
}

async function addPeople(forms){
    const chosenType = forms.peopleType.value;
    const chosenInvestigation = forms.people_select.value;
    const firstname = forms.peopleFirstname.value;
    const lastname = forms.peopleLastname.value;
    const birthdate = forms.peopleBirthdate.value; //yyyy-mm-dd
    const gender = forms.peopleGender.value;
    const data = [lastname, firstname, birthdate, gender];
    switch (chosenType) {
        case 'suspect' || 'culprit':
            data.push(forms.peoplePicture.value);
            data.push(forms.peopleSuspicion);
            data.push(forms.peopleCriminal_record.value);
            if (chosenType === 'culprit'){
                data.push(forms.peopleMotivation.value);
                data.push(forms.peopleVictim_relationship.value)
            }
            break;
        case 'witness' || 'victim':
            data.push(forms.peopleTestimony.value);
            data.push(forms.peopleContact.value);
            if (chosenType === 'witness'){
                data.push(forms.peopleCondition.value);
                data.push(forms.peopleCircumstance.value);
            }
            break;
    }
    eel.log('Adding people...')
    let new_people = await eel.make_person(chosenType, chosenInvestigation, data)();
    if (new_people.includes('Invalid')){
        new_people = new_people.split(':')[1];
        getId(logPe).setAttribute('class', 'error');
        eel.log('Displaying people error...');
    } else {
        getId(logPe).setAttribute('class', 'ok');
    }
    addElement(logPe, new_people);
}

function recordingValue(){
    const recordingTag = getId('evidenceType');
    const hidden = queryAll('.evidenceHidden');
    switch (recordingTag.value){
        case 'recording':
            recordingTag.removeAttribute('required');
            hidden.forEach(tag => tag.setAttribute('hidden', 'true'));
            break;
        default:
            recordingTag.setAttribute('required', 'true');
            hidden.forEach(tag => tag.removeAttribute('hidden'));
    }
}

function fillEvidencePeople(chosenInvestigation){
    eel.fill_evidence_table(chosenInvestigation);
    getId('evidenceTable').removeAttribute('hidden');
    eel.log('Evidence table filled successfully');
    eel.fill_people_table(chosenInvestigation);
    getId('peopleTable').removeAttribute('hidden');
    eel.log('People table filled successfully');
}

function selectInvestigation(node) {
    queryAll('.selected').forEach(tag => tag.classList.remove('selected'));
    node.classList.add('selected');
}

async function filterStatus(status, investigationName){
    if (await eel.filter_status(status)()){
        getId(investigationName).setAttribute('class', 'selected');
    }
}