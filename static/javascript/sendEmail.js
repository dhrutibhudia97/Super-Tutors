function sendMail(contactForm) {
    emailjs.send("gmail", "Super Tutor", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "querysubmission": contactForm.querysubmission.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error)
        });
        return false; 
}