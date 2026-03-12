// Show message after booking appointment
function appointmentBooked() {
    alert("Appointment booked successfully!");
}


// Simple form validation for register page
function validateRegister() {

    let name = document.querySelector("input[name='name']").value;
    let email = document.querySelector("input[name='email']").value;
    let password = document.querySelector("input[name='password']").value;

    if(name === "" || email === "" || password === "") {
        alert("Please fill all fields");
        return false;
    }

    return true;
}


// Simple login validation
function validateLogin() {

    let email = document.querySelector("input[name='email']").value;
    let password = document.querySelector("input[name='password']").value;

    if(email === "" || password === "") {
        alert("Enter email and password");
        return false;
    }

    return true;
}


// Highlight active navigation link
document.addEventListener("DOMContentLoaded", function() {

    let links = document.querySelectorAll("nav a");
    let current = window.location.pathname;

    links.forEach(link => {
        if(link.getAttribute("href") === current){
            link.style.fontWeight = "bold";
        }
    });

});