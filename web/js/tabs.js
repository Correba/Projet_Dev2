"use strict";

let idCurrentTab = "investigations";

document.addEventListener("DOMContentLoaded", initTabs);

function initTabs() {
    getId('aff_' + idCurrentTab).style.display = "block";
    getId(idCurrentTab).classList.add("active");
}

function changeTab(tabButton) {
    getId('aff_' + idCurrentTab).style.display = "none";
    getId(idCurrentTab).classList.remove("active");

    getId('aff_' + tabButton.id).style.display = "block";
    getId(tabButton.id).classList.add("active");

    idCurrentTab = tabButton.id;
}