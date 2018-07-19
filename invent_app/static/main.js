function SetDisplay(data){
    var x = document.getElementsByClassName("update");
    var i;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = data;
    }
}

function HideUpdates(){
    SetDisplay('none');
    var btn = document.getElementById("hideButton");
    btn.innerText = "Show Updates";
    btn.onclick = ShowUpdates;

}

function ShowUpdates(){
    SetDisplay('');
    var btn = document.getElementById("hideButton");
    btn.innerText = "Hide Updates";
    btn.onclick = HideUpdates;
}
