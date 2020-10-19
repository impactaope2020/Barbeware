const idDataAgendamento = document.getElementById("date")
const idBarbeiro = document.getElementById("barbeiros")
const idTabela = document.getElementById("tbody")
var dados = '';

idDataAgendamento.onchange = function(){

    fetch('Agenda/' + idDataAgendamento.value + "/" + idBarbeiro.value).then(function(response){

        response.json().then(function(data) {
            
            idTabela.innerHTML = '';
            let agendamentos = '';
            dados = '';
            for(contador = 0; contador < data.Agendamentos.length; contador++){
                agendamentos = '';
                for (contador_atributos = 0; contador_atributos < data.Agendamentos[contador].length;contador_atributos++){
                    if(contador_atributos === 3){
                        excluir_agendamento = "<td><a href='Agenda/" + data.Agendamentos[contador][contador_atributos] + "'><button class='btn btn-danger'>Excluir</button></a></td>"
                        agendamentos += excluir_agendamento
                    }
                    if (contador_atributos !== 3){
                        agendamentos += '<td>' + data.Agendamentos[contador][contador_atributos] + '</td>' 
                    }                 
                }
                dados += '<tr>' + agendamentos + '</tr>';
            }
            if (dados){
                idTabela.innerHTML += dados; 
            }
            else {
                idTabela.innerHTML = '';
                dados = '';
            }
        }
    )}    
)}

idDataAgendamento.onchange()

idBarbeiro.onchange = function(){
    idDataAgendamento.onchange()
}
