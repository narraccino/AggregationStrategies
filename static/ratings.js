function collectRatings(data) {

    console.log("Sollldiiii soldiiii");
    var new_data = {'dict': []};

    for (i = 0; i < data.infoPOI.length; i++) {

        var rating = document.getElementById(data.infoPOI[i].id).getAttribute("value");

        var element = {'poi': data.infoPOI[i].id, 'rating': rating};
        new_data.dict.push(element)
    }

    console.log(new_data);


    $.post("addRates", JSON.stringify(new_data), function (response) {

        document.open();
        document.write(response);
        document.close();

    });


}

function populate(data){

    var div_containter = document.createElement("div");
    div_containter.classList.add("container", "section");



    for(i = 0; i <  data.infoPOI.length ; i++) {

        var div_row = document.createElement("div");
        div_row.classList.add("row");

        var div_col = document.createElement("div");
        div_col.classList.add("col-md-6");
        div_col.setAttribute("id", String(data.infoPOI[i].id));

        var attr = document.createAttribute("value");
        attr.value = "0";
        div_col.setAttributeNode(attr);


        // var attr_id = document.createAttribute("id");
        // attr_id.value = data.infoPOI[i].id;
        // div_col.setAttributeNode(attr_id);

        var h7_1 = document.createElement("h7");
        h7_1.innerHTML = "categories:";

        var h3 = document.createElement("h3");
        h3.innerHTML = data.infoPOI[i].poi;

        var p1 = document.createElement("p");
        p1.innerHTML = data.infoPOI[i].cat;

        var h7_2 = document.createElement("h7");
        h7_2.innerHTML = "Description:";

        var p2 = document.createElement("p");
        p2.innerHTML = data.infoPOI[i].description;

        var p3 = document.createElement("p");
        var str = data.infoPOI[i].sito;
        var result = str.link(data.infoPOI[i].sito);
        p3.innerHTML = result;

        var p_rate = document.createElement("p");
        p_rate.classList.add("rateyo")


        var div_col2 = document.createElement("div");
        div_col2.classList.add("col-md-6");

        var image = document.createElement("img");
        image.src = "https://igx.4sqi.net/img/general/width540/U4qNR1906bNs1JJ44BdWWDU4fM8kR97wxayjTZdA8vM.jpg";
        image.setAttribute('alt', "NO IMAGE");
        div_col2.appendChild(image);



        div_col.appendChild(h3);
        div_col.appendChild(h7_1);
        div_col.appendChild(p1);
        div_col.appendChild(h7_2);
        div_col.appendChild(p2);
        div_col.appendChild(p3);
        div_col.appendChild(p_rate);

        if(i % 2 == 1) {
            div_row.appendChild(div_col);
            div_row.appendChild(div_col2);
        }

        if(i % 2 == 0)
        {
            div_row.appendChild(div_col2);
            div_row.appendChild(div_col);
        }


        div_containter.appendChild(div_row);
    }
            var div_button = document.createElement("div");
            div_button.classList.add("wrapper");
            div_button.style.position= "absolute";
            div_button.style.width= "100%";
            div_button.style.padding= "50px";


            var button = document.createElement("button");
            button.type = "button";
            button.classList.add("btn", "btn-secondary", "btn-lg");
            button.innerHTML= "Submit";
            button.onclick = function(){ collectRatings(data) };


            div_button.appendChild(button);
            div_containter.appendChild(div_button);

            document.body.appendChild(div_containter);

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

