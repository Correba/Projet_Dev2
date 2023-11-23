"use strict";

let idCurrentTab = "investigations";

document.addEventListener("DOMContentLoaded", initTabs);

function initTabs() {
    document.getElementById('aff_' + idCurrentTab).style.display = "block";
    document.getElementById(idCurrentTab).classList.add("active");
}

function changeTab(tabButton) {
    document.getElementById('aff_' + idCurrentTab).style.display = "none";
    document.getElementById(idCurrentTab).classList.remove("active");

    document.getElementById('aff_' + tabButton.id).style.display = "block";
    document.getElementById(tabButton.id).classList.add("active");

    idCurrentTab = tabButton.id;
}