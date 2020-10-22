var barbeiro = document.getElementById("barbeiro");
var horarios = document.getElementById("hora");
var datas = document.getElementById("data")
var alert = document.getElementById("alert")

var currentDate = new Date();

var date = currentDate.getDate();
var month = currentDate.getMonth(); 
var year = currentDate.getFullYear();

var dateString = year + "-" + pad(month + 1) + "-" + dayArred(date);

datas.value = dateString;

function pad(n){
    if (n < 10){
        return "0" + n;
    } 
    else{
        return n
    }
}

function dayArred(numero){
    if (numero < 10){
        return "0" + numero;
    }
    else{
        return numero
    }
}

function reverseDate(date){
    data = date.split('-')
    return data[2] + '/' + data[1] + '/' + data[0]
}


barbeiro.onchange  = function(){

    fetch('Agendamento/' + barbeiro.value + "/" + datas.value) .then(function(response){

          response.json().then(function(data) {
            
            optionHTML = '';
            for (disponiveis = 0; disponiveis < data[1].horarios_disponiveis.length; disponiveis++){
                optionHTML += '<option value="' + data[1].horarios_disponiveis[disponiveis] +'">' + data[1].horarios_disponiveis[disponiveis] + '</option>'
                horarios.innerHTML = optionHTML;
                alert.innerHTML = "";
            }
            if (data[1].horarios_disponiveis.length === 0){
                alert.innerHTML = "<br/><div class='alert alert-danger' role='alert'> Todos os horarios já estão agendados para a data " + "<b>" + reverseDate(datas.value) + "</b>" + ", por favor,  selecione outro dia ou verifique a agenda de outro barbeiro.</div>"
                horarios.innerHTML = optionHTML;
            }
          });
         });
        }

datas.onchange = function(){
    barbeiro.onchange()
}


barbeiro.onchange()