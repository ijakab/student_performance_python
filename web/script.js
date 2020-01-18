window.onload = function () {
    let callBtn = document.getElementById('callBtn')

    callBtn.addEventListener('click', async function () {
        let data = await callApi()
        console.log(data)
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
        return await res.json()
    }
}
