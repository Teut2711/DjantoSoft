document.querySelector(".lds-ring").style.display = "none";

document.querySelector("label[for='id_filepath']").textContent = "";

document.querySelector("label[for='id_filepath']").insertAdjacentHTML('afterbegin',
    '<i class="fas fa-file-upload"></i><span style="color:white;">  Upload *.txt file </span></i>');
// document.querySelector("label[for='id_filepath']")

document.querySelector("input[id='id_filepath']").addEventListener("click", function(event) {

    document.querySelector(".filetargeted").textContent = event.target.files[0].name;
});


document.querySelector(".main_form").addEventListener('submit', function(event) {
    //
    document.querySelector(".lds-ring").style.display = "flex";
    document.querySelector(".submitfile").remove();

    event.preventDefault();

    var formData = new FormData(event.currentTarget);

    fetch("http://127.0.0.1:8000/Master/nsdlbenpos/", {

        method: "post",

        body: formData

    }).then(function(response) {
        document.querySelector(".lds-ring").remove();
        return response.text()

    }).then(function(response) {
        document.querySelector(".formclass").insertAdjacentHTML('beforeend', response);

    }).catch(function(response) {
        console.log("Error");
    })

    document.querySelector(".main_form").remove()

})