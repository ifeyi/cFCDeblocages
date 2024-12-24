let deblocageSvgEyeOn = document.getElementById("deblocage-svg-eye-on");
let deblocageSvgEyeOff = document.getElementById("deblocage-svg-eye-off");
let deblocagePassword = document.getElementById("deblocage-password");

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