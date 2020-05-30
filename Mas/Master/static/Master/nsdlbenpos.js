document.querySelector(".loader").style.display = "none";


document.querySelector("label[for='id_filepath']").textContent = "";


document.querySelector("label[for='id_filepath']").insertAdjacentHTML('afterbegin',
    '<i class="fas fa-file-upload"></i><span style="color:white;">  Upload *.txt file </span></i>');


document.querySelector("input[id='id_filepath']").addEventListener("change", function(event) {

    document.querySelector(".filetargeted").textContent = event.target.files[0].name;
});


document.querySelector(".main_form").addEventListener('submit', function(event) {
    //
    document.querySelector(".loader").style.display = "flex";
    document.querySelector(".submitfile").remove();

    event.preventDefault();

    var formData = new FormData(event.currentTarget);

    fetch("http://127.0.0.1:8000/Master/nsdlbenpos/", {

        method: "post",

        body: formData

    }).then(function(response) {
        document.querySelector(".loader").remove();
        return response.json()

    }).then(function(response) {

        var li = [];
        Object.keys(response).forEach(function(value) {
            li.push(`<li>${value} :  ${response[value]}</li>`)
        })

        response = `<div class="main_form">
        <h3><span style="color:rgb(0, 159, 183)"> Attributes </span> </h3>
        <ul>
        ${li.join()}
        </ul>
        </div>`

        document.querySelector(".formclass").insertAdjacentHTML('beforeend', response);

    }).catch(function(response) {
        alert("Some Error");
        return response.text()
    }).then(function(response) {
        console.log(response)
    })

    document.querySelector(".main_form").remove()

})

//0124-4444121