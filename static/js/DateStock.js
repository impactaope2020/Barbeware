var datastock = document.getElementById('data')

const date = new Date()

const day = date.getDay()
const month = date.getMonth()
const year = date.getFullYear()

function date_arred(day, month, year){
    if (day < 10){
        day = '0' + day
    }
    if (month < 10){
        month = '0' + month
    }
    return year + '-' + month + '-' + day;
}

datastock.value = date_arred(day, month, year)