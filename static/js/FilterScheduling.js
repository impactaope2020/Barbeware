const idDataAgendamento = document.getElementById("date")
const idBarbeiro = document.getElementById("barbeiros")
const idTabela = document.getElementById("tbody")
var dados = '';

idDataAgendamento.onchange = function(){

    fetch('Agenda/' + idDataAgendamento.value + "/" + idBarbeiro.value).then(function(response){

        response.json().then(function(data) {
            
            idTabela.innerHTML = '';
            for(contador = 0; contador < data.Agendamentos.length; contador++){
                var agendamentos= '';
                for (contador_atributos = 0; contador_atributos < data.Agendamentos[contador].length;contador_atributos++){
                    console.log(data.Agendamentos[contador][contador_atributos])
                    agendamentos += '<td>' + data.Agendamentos[contador][contador_atributos] + '</td>'                    
                }
                dados += '<tr>' + agendamentos + '</tr>';
            }
            idTabela.innerHTML += dados;
        }
    )}    
)}

