var barbeiro = document.getElementById("barbeiro");
var horarios = document.getElementById("hora");
var datas = document.getElementById("data")
var alert = document.getElementById("alert")

var currentDate = new Date();

var date = currentDate.getDate();
var month = currentDate.getMonth(); 
var year = currentDate.getFullYear();

var dateString = year + "-" + pad(month + 1) + "-" + date;

datas.value = dateString;

function pad(n){
    if (n < 10){
        return "0" + n;
    } 
    else{
        return n
    }
}


barbeiro.onchange = function(){

    fetch('Agendamento/' + barbeiro.value + "/" + datas.value) .then(function(response){

          response.json().then(function(data) {
            
           optionHTML = '';
            for (disponiveis = 0; disponiveis < data[1].horarios_disponiveis.length; disponiveis++){
                optionHTML += '<option value="' + data[1].horarios_disponiveis[disponiveis] +'">' + data[1].horarios_disponiveis[disponiveis] + '</option>'
                horarios.innerHTML = optionHTML;
                alert.innerHTML = "";
            }
            if (data[1].horarios_disponiveis.length === 0){
                alert.innerHTML = "<br/><div class='alert alert-danger' role='alert'> Todos os horarios já estão agendados para a data " + "<b>" + datas.value + "</b>" + ", por favor,  selecione outro dia ou a agenda de outro barbeiro.</div>"
                horarios.innerHTML = optionHTML;
            }
          });
         });
        }