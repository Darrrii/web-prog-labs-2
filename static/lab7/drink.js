function getPrice() {
    const milk= document.querySelector('[name=milk]').checked;
    const sugar= document.querySelector('[name=sugar]').checked;
    const drink= document.querySelector('[name=drink]').value;
}

    const obj={
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar:sugar
    }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })

    .then(function(data) {
        document.querySelector('#price').innerHTML= 'Цена напитка: ${data.result} руб';
        document.querySelector('#pay').computedStyleMap.display= '';
    })

    function pay() {
        const  drink= document.querySelector('[name=drink]').checked;
        const price= document.querySelector('[name=price]').checked;
        const card= document.querySelector('[name=card]').value;
        const cvv= document.querySelector('[name=cvv]').value;
    }

    const paycard={
        "method": "pay",
        "params": {
            drink: drink,
            price: price,
            card: card,
            cvv:cvv
    }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(paycard)
    })