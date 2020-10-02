var date = document.getElementById("date");

var currentDate = new Date();

var day = currentDate.getDate();
var month = currentDate.getMonth();
var year = currentDate.getFullYear();

var day_month_year = year + "-" + arred_month(month + 1) + "-" + day ;

date.value = day_month_year;

function arred_month(mes){
    if ( mes < 10){
        return "0" + mes; 
    }
    return mes
}