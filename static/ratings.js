function collectRatings(data){

    var array = data.dict;

    var new_data = {'dict' : []} ;

    for(i = 0; i < array.length; i++){

        d = array[i];

        var rating = document.getElementById(d.id).getAttribute("value");

        var element = {'poi' : d.poi, 'rating' : rating};
        new_data.dict.push(element)
    }

    console.log(new_data);

    // $.ajax({
    //     type: 'POST',
    //     contentType: 'application/json',
    //     data: JSON.stringify(new_data),
    //     dataType: 'json',
    //     url: 'http://localhost:5000/addRates',
    //     success: function (e) {
    //         console.log("oleeee");
    //         console.log(e);
    //     },
    //     error: function(error) {
    //         console.log("cazzzzz");
    //         console.log(error);
    //     }
    // });

    $.post("addRates", JSON.stringify(new_data), function(response){

        document.open();
        document.write(response);
        document.close();

    });



}


function populate(data){

    var array = data.dict;
    var default_div = document.getElementById("default");
    for(i = 0; i < array.length; i++){

        d = array[i];

        var div = default_div.cloneNode(true);
        var img = div.getElementsByTagName("img")[0];
        img.src = d.image;

        var poi = div.getElementsByClassName('poi')[0];
        poi.innerText = d.poi;

        var cat = div.getElementsByClassName('cat')[0];
        cat.innerText = d.cat;

        var description = div.getElementsByClassName('description')[0];
        description.innerText = d.description;

        // var sito = div.getElementsByClassName('sito')[0];
        // sito.innerText = d.sito;
        var sito= div.getElementsByClassName('sito')[0];
        var str = d.sito;
        var result = str.link(d.sito);
        sito.innerHTML = result;

        var spacing = document.createElement("div");
        spacing.classList.add("spacing");
        spacing.setAttribute("style", "display: inline-block; width: 600px");
        div.appendChild(spacing);

        var rate_div = document.createElement("div");
        rate_div.classList.add("rateyo");
        rate_div.setAttribute("style", "display: inline-block; position: absolute; top: 25%");
        div.appendChild(rate_div);

        div.id = d.id;

        div.style.display = "block";

        document.getElementById('poi-container').appendChild(div);
    }

    var button = document.createElement("div");
    button.classList.add("container-contact100-form-btn");
    var subbutton = document.createElement("button");
    subbutton.classList.add("contact100-form-btn");
    subbutton.innerText = "SUBMIT";
    subbutton.onclick = function(){ collectRatings(data) };
    button.appendChild(subbutton);

    document.getElementById('poi-container').appendChild(button);
}


function pop_rec(fairness, least){

    var fs = fairness.fairness;
    var ls = least.least;

    var list = document.getElementById('fairness-list');

    for(i = 0; i < fs.length; i++){

        var element = document.createElement("li");
        element.classList.add("elementList");
        element.innerText = fs[i];
        list.appendChild(element);
    }

    var list = document.getElementById('least-list');

    for(i = 0; i < ls.length; i++){

        var element = document.createElement("li");
        element.classList.add("elementList");
        element.innerText = ls[i];
        list.appendChild(element);
    }

}

