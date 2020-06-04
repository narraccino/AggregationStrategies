function createUsernames(N){
    // var N = 10;

    var user = document.getElementById('username-container-0');
    var button = document.getElementById('ok-btn').cloneNode(true);
    for(i=0; i<N; i++){
        var num = i + 1;
        var child = user.cloneNode(true);
        child.setAttribute('id', 'user-container-'.concat(num.toString()));
        child.setAttribute('placeholder', 'Username '.concat(num.toString()));
        child.setAttribute('style', 'display:block;');
        var first = child.getElementsByTagName('input')[0];
        first.setAttribute('name', 'name'.concat(num.toString()));
        first.setAttribute('placeholder', 'Username '.concat(num.toString()));
        // child.setAttribute("style", "display:block");

        document.getElementById('form-grp').appendChild(child);
    }
    var first = document.getElementById('username-container-0').getElementsByTagName('input')[0];
    first.setAttribute('value', 'default');
    button.setAttribute('id', 'real-btn');
    button.setAttribute("style", "display:block");
    document.getElementById('form-grp').appendChild(button);
}

