window.onload = function () {
    let callBtn = document.getElementById('callBtn')

    callBtn.addEventListener('click', async function () {
        let data = await callApi()
        console.log(data)
        plot(data)
    })

    async function callApi() {
        let res = await fetch('/predict', {
            method: 'POST',
            body: JSON.stringify({
                features: [16,"F","U","LE3","T",3,4,"health","teacher",2,3,"yes","no","yes","yes",1,3,2,4,23,0]
            }),
            mode: 'no-cors', // no-cors, *cors, same-origin
            headers: {
               'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        })
        let json = await res.json()
        for(let key of Object.keys(json)) {
            json[key] *= 5
            json[key] = json[key].toFixed(1)
            json[key] = Number(json[key])
        }
        return json
    }

    function plot(models) {
        var ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: Object.keys(models),
                datasets: [{
                    label: 'Model predictions',
                    data: Object.values(models),
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    }
}
