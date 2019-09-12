const axios = require('axios')
btn = document.getElementById("analyseBtn")
optext = document.getElementById('optext')
request = new XMLHttpRequest();



apiCall=()=>{
    document.getElementById("myChart").remove()
    var element = document.createElement("canvas")
    element.setAttribute('id','myChart')
    document.getElementsByClassName('canvasDiv')[0].appendChild(element)
    console.log(document.getElementById('inp').value);
    
    axios.post('http://192.168.2.240:5000/spamapi/',{
              input:document.getElementById('inp').value
          }).then((res)=>{
              optext.innerHTML = res.data.prediction
             drawDoughnutChart(res.data.spam_prob,res.data.ham_prob)
          }).catch((err)=>{
              console.error(err);
              
          })
}

clearTxt=()=>{
    document.getElementById('inp').value = ""
}


drawDoughnutChart=(spam_prob,ham_prob)=>{
    var canvas = document.getElementById('myChart')
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight
    ctx= canvas.getContext('2d');
    data = {
        datasets: [{
            data: [spam_prob, ham_prob],
            backgroundColor: [
                '#F2AA4CFF',
                '#000'

            ],color: [
                '#fff',
                '#fff'

            ],
        }],
        labels: [
            'Spam(%)',
            'Ham(%)'
        ]
    };
    options= {
        responsive: true,
        legend: {
            position: 'top',
        },
        animation: {
            animateScale: true,
            animateRotate: true
        }
    }

    var myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options:options
    });

}
