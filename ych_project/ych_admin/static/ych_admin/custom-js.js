var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 3000);
}

function showPage() {
    // localStorage.setItem('first', 'null');
    // function toBeExecutedOnFirstLoad(){
    //     // ...
    //     document.getElementById("loader").style.display = "none";
    //     document.getElementById("myDiv").style.display = "block";
    // }
    // if(localStorage.getItem('first') === 'null'){
    //     toBeExecutedOnFirstLoad();
    //     localStorage.setItem('first','nope!');
    // }
    
    document.getElementById("loader").style.display = "none";
    document.getElementById("myDiv").style.display = "block";
}
