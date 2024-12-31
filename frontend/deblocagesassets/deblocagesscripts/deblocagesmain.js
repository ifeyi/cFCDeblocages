let deblocageSvgEyeOn = document.getElementById("deblocage-svg-eye-on");
let deblocageSvgEyeOff = document.getElementById("deblocage-svg-eye-off");
let deblocagePassword = document.getElementById("deblocage-password");

if(deblocageSvgEyeOn){
    deblocageSvgEyeOn.addEventListener("click", () => {
        deblocageSvgEyeOn.classList.toggle("deblocage-none");
        deblocageSvgEyeOff.classList.toggle("deblocage-none");
        deblocagePassword.type = "text";
    });
    deblocageSvgEyeOff.addEventListener("click", () => {
        deblocageSvgEyeOff.classList.toggle("deblocage-none");
        deblocageSvgEyeOn.classList.toggle("deblocage-none");
        deblocagePassword.type = "password";
    });
}

/* ACCORDION */

let deblocageAccordionElt = document.querySelectorAll(".deblocage-accordion-elt");

if(deblocageAccordionElt){
    deblocageAccordionElt.forEach((elt) => {
        if(elt.classList.contains("deblocage-accordion-elt-active")){
            elt.querySelector(".deblocage-cacher-text").textContent = "Cacher";
        }else{
            elt.querySelector(".deblocage-cacher-text").textContent = "Afficher";
        }
        elt.querySelector(".deblocage-cacher-text").addEventListener("click", () => {
            elt.classList.toggle("deblocage-accordion-elt-active");
            if(elt.classList.contains("deblocage-accordion-elt-active")){
                elt.querySelector(".deblocage-cacher-text").textContent = "Cacher";
            }else{
                elt.querySelector(".deblocage-cacher-text").textContent = "Afficher";
            }
        });
    });
}
/* ACCORDION */

/* DEBLOCAGE SINGLE */

let deblocageBtnQuitter = document.getElementById("deblocage-btn-quitter");
let deblocageDemandeDePretsSingle = document.getElementById("deblocage-demande-de-prets-single");
let deblocageTableauPretsBody = document.querySelectorAll(".deblocage-tableau-prets-body");

deblocageTableauPretsBody.forEach((elt) => {
    elt.addEventListener("click", () => {
        deblocageDemandeDePretsSingle.classList.toggle("deblocage-none");
    });
});

if(deblocageBtnQuitter){
    deblocageBtnQuitter.addEventListener("click", () => {
        deblocageDemandeDePretsSingle.classList.toggle("deblocage-none");
    });
}

