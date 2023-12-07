"use strict";

eel.expose(getFormInfos);
eel.expose(addElement);

document.addEventListener('DOMContentLoaded', load);

function load(){
    eel.fill_table_investigations();
    eel.fill_type_forms();
    setMaxDate();
    getId('evidenceType').addEventListener('change', recordingValue);
}

function getFormInfos(forms){
    const new_name = forms.investigationName.value;
    eel.create_investigations(new_name);
}

function addElement(id, html){
    getId(id).innerHTML = html;
}

function setMaxDate() {
    const today = new Date().toISOString().split('T')[0];
    queryAll('input[type="date"]').forEach(inputDate => inputDate.setAttribute("max", `${today}`));
}

function addEvidence(forms){
    const chosenType = forms.evidenceType.value;
    const chosenInvestigation = forms.evidence_select.value;
    const name = forms.evidenceName.value;
    const description = forms.evidenceDescription.value;
    const date = forms.evidenceDate.value; //yyyy-mm-dd
    const file = forms.evidenceFile.value;
    const data = [name, description, date, file];
    switch (chosenType) {
        case 'picture':
            break;
        case 'object':
            break;
        case 'recording':
            break;
        default:
            eel.make_evidence(chosenType, chosenInvestigation, data);
    }
}

function addPeople(forms){
    const chosenType = forms.peopleType.value;
    const chosenInvestigation = forms.people_select.value;
    const firstname = forms.peopleFirstname.value;
    const lastname = forms.peopleLastname.value;
    const birthdate = forms.peopleBirthdate.value; //yyyy-mm-dd
    const gender = forms.peopleGender.value;
    const data = [firstname, lastname, birthdate, gender];
    switch (chosenType) {
        case 'suspect' || 'culprit':
            break;
        case 'witness' || 'victim':
            break;
        default:
            eel.make_person(chosenType, chosenInvestigation, data);
    }
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
