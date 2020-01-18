const trackedFeatures = ['age','sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','traveltime','studytime','activities','higher','internet','romantic','freetime','goout','Dalc','Walc','absences']


window.onload = function () {
    let mainForm = document.getElementById('mainForm')

    mainForm.addEventListener('submit', async function (e) {
        e.preventDefault()
        let features = getFeatures()
        let data = await callApi({features})
        plot(data)
    })

    async function callApi(data) {
        let res = await fetch('/predict', {
            method: 'POST',
            body: JSON.stringify(data),
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

    function getFeatures() {
        let features = []
        for(let featureName of trackedFeatures) {
            let element = document.getElementById(featureName)
            if(Number(element.value)) features.push(Number(element.value))
            else features.push(element.value)
        }
        features.push(0)
        return features
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
