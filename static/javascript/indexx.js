
document.addEventListener("DOMContentLoaded", function() {
    // getting the names of tags and elements
    let buttton = document.getElementsByClassName("chhange");
    let boxxx = document.getElementsByClassName("huhh")[0];
    let unkk = document.getElementsByClassName("foees");
    let yhh =  document.getElementsByClassName("knowwws");
    
    // For the font changer
    let foons = document.getElementsByName("fonnn");
    let fonns = document.getElementsByName("fonts");
    let tarea = document.getElementById("nnn");

    // For ppl u know of privately or publically
    let pUblic = document.getElementById("pUblic");
    let pRivate = document.getElementById("pRivate");

    // For messages
    let meggs = document.getElementsByClassName("meggas")


    fonns[0].checked = true;
    tarea.value = "";

    buttton[0].addEventListener("click", function chenga() {
        if (boxxx.id == "friendd") {
            boxxx.id = "findd";
            ioo(unkk, boxxx.id, yhh)
        }
        else if (boxxx.id == "findd") {
            boxxx.id = "friendd";
            ioo(yhh, boxxx.id, unkk)
        } 

    });



    foons[0].addEventListener("click", function rr() {
        const j = jui(fonns);
        console.log(j);
        tarea.style.fontFamily = j;

    });

    for (let t = 0; t < meggs.length; t++) {
        const terr = meggs[t];
        if (t == 0 || (t % 3) == 0){
            terr.style.backgroundColor = "#000066";
            console.log(t % 3)
        }
        else if (t == 1 || (t % 3) == 1){
            terr.style.backgroundColor = "#00004d";
            console.log(t % 3)
        }
        else if (t == 2 || (t % 3) == 2){
            terr.style.backgroundColor = "#000033";
            console.log(t % 3)
        }
        
    }

});

function jui(fon) {
    for (let i = 0; i < fon.length; i++) {
        if (fon[i].checked) {
        if (fon[i].value == "default") {
            return "Verdana";
        }
        return fon[i].value;
      }
    }
}


function p_or_p(prilic) {
    if (prilic == "public")
    {
        pUblic.style.borderColor = "lime";
        pRivate.style.borderColor = "";
        messer(pUblic.id);
    }
    else if (prilic == "private")
    {
        pRivate.style.borderColor = "lime";
        pUblic.style.borderColor = "";
        messer(pRivate.id);
    }
    
}

function huu (hh, gg){
    let peeps = ""
    hh.forEach(element => {
        if (element.checked) {
            peeps += element.id + " ";
        }
    });
    gg.forEach(element => {
        if (element.checked) {
            peeps += element.id + " ";
        }
    });
    return peeps;
}

function ioo(ru, f_f, losss) {
    if (f_f == "findd"){
        for (let i = 0; i < ru.length; i++) {
            let element1 = ru[i];
            let element2 = losss[i];

            element1.hidden = false;
            element2.hidden = true;
        }
    }
    else if (f_f == "friendd"){
        for (let i = 0; i < ru.length; i++) {
            let element1 = ru[i];
            let element2 = losss[i];

            element1.hidden = false;
            element2.hidden = true;
    }
}

}