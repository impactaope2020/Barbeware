var date = document.getElementById("date");

var currentDate = new Date();

var day = currentDate.getDate();
var month = currentDate.getMonth();
var year = currentDate.getFullYear();

var day_month_year = year + "-" + arred_month(month + 1) + "-" + dayArred(day) ;

date.value = day_month_year;

function arred_month(mes){
    if ( mes < 10){
        return "0" + mes; 
    }
    return mes
}
function dayArred(numero){
    if (numero < 10){
        return "0" + numero;
    }
    else{
        return numero
    }
}