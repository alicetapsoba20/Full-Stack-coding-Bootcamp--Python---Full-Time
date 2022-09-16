/*let sentence = prompt("entrer une phrase contenant le mot'not' et 'bad'");
/*console.log(sentence);
let wordNot = sentence.indexOf("not");
let wordBad = sentence.charAt('bad');
console.log(wordBad)*/

for(let i=0;i<=15;i++){
    if (i % 2==0 ){
    console.log(i+" est paire");}
    else{
    console.log(i+" est impaire");}
}
function setTime(){
    setTimeout(function(){
        alert('hello');
    },3000)
    }

    let id;
    function setInter(){
    let num = 0
    id = setInterval(function(){
        console.log(num);
        num ++
    },1000);
    }

    function clearInter(){
    clearInterval(id);
    }

    let root = document.getElementById('root');

    let outer = document.createElement('div');
    let inner = document.createElement('div');
    outer.classList.add('outer');
    inner.classList.add('inner');
    inner.setAttribute('id','main');
    outer.appendChild(inner);
    root.appendChild(outer);

    function myMove() {
    var elem = document.getElementById("main");
    var pos =0;
    elem.style.top = 150 + "px";
    elem.style.left = 0 + "px";
    let id = setInterval(function() {
        if (pos ==350) {
        clearInterval(id);
        }
        else {
            pos++;
            elem.style.top =150 + 150*Math.sin(pos*Math.PI/180) + "px";
            elem.style.left = pos + "px";
            }
    }, 5);
    }