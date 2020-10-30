//modal

function openModal(){
    document.getElementById('id01').style.display='block';
}

function closeModal(){
    document.getElementById('id01').style.display='none';
}

function closeModal2(){
    var modal = document.getElementById('id01');

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}


//Store

function addToCart(){
    alert('Your game has been added');
}


//Login

function register(){
    n = document.getElementById('nickname').value;

    locate='index.html';
    alert('Welcome to Retro Games '+ n);
}


/*function samePassword(){
    psw1 = document.getElementById('clave1').value;
    psw2 = document.getElementById('clave2').value;

    if (psw1==psw2){
        return true;
    }
    else{
        return false;
    }
}*/