var barbeiro = document.getElementById("barbeiro");
var horarios = document.getElementById("hora");
var datas = document.getElementById("data")

barbeiro.onchange = function(){

    fetch('Agendamento/' + barbeiro.value + "/" + datas.value) .then(function(response){

          response.json().then(function(data) {
            
           optionHTML = '';
            for (disponiveis = 0; disponiveis < data[1].horarios_disponiveis.length; disponiveis++){
                optionHTML += '<option value="' + data[1].horarios_disponiveis[disponiveis] +'">' + data[1].horarios_disponiveis[disponiveis] + '</option>'
                console.log(data[1].horarios_disponiveis[disponiveis])
                horarios.innerHTML = optionHTML;
            }
            if (data[1].horarios_disponiveis.length === 0){
                alert("Todos horarios Agendados")
            }
          });
         });
        }