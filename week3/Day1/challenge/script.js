/*Des Instructions
Dans cet exercice, nous allons créer une page Web avec un fond noir comme univers et nous remplirons l'univers de planètes et de leurs lunes.
Nous fournirons la page HTML.
Vous n'avez qu'à travailler avec un fichier JS.

Créez un tableau dont la valeur est les planètes du système solaire.
Pour chaque planète du tableau, créez un <div>fichier using createElement. Cette div doit avoir une classe nommée "planet".
Chaque planète doit avoir une couleur de fond différente. ( Astuce : vous pouvez ajouter une nouvelle classe à chaque planète - chaque classe contenant une couleur de fond différente).
Enfin, ajoutez chaque div au <section>dans le HTML (présenté ci-dessous).
Bonus : Faites le même processus pour créer les lunes.
Attention, chaque planète possède un certain nombre de lunes. Comment devez-vous les afficher ?
Faut-il encore utiliser un tableau pour les planètes ? Ou un tableau d'objets ?
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Challenge: Create a solar system</title>
        <style>
            body {
                background-color: black;
                padding: 10px;
            }
            .planet {
                width: 100px;
                height: 100px;
                border-radius: 50%;
                text-align: center;
                padding: 10px;
                position: relative;
                border: 2px solid white;
            }
            .moon {
                position: absolute;
                width: 30px;
                height: 30px;
                border-radius: 50%;
                background: rgb(237, 237, 237);
                border: 5px solid red;
            }
        </style>
    </head>
    <body>

    <section class="listPlanets"></section>

    <script src="..."></script>
    </body>
</html> */

let planètes = ["Sun", "Mercury", "Venus", "Earth", "Mars","Pluto", "Neptune", "Uranus", "Jupiter", "Saturn"];
let colorList = ["yellow", "gray", "brown", "blue","orange", " violet", "blue", "green", "red", "#F5F5DC"];

let lunes = [0, 0, 0, 1, 2, 5, 14, 27, 79, 82]


for (let i = 0; i < planètes.length; i++) {
    let div1 = document.createElement("div");
    let newContent = document.createTextNode(planètes[i]);
    div1.appendChild(newContent);
    div1.className = (`planet ${i}`) // add  class planet + i which is a number & a second class 
    div1.style.marginTop='10px';
    document.body.appendChild(div1);
    let backgroundColor = document.getElementsByClassName("planet")[i].style.backgroundColor = colorList[i];

    let margin_left =80 
    if (lunes[i] != 0){
        for (let a =0; a <lunes[i]; a++){
            margin_left+=60
            let div = document.createElement('div');
            div.classList.add('moon');
            div.style.marginLeft=margin_left + 'px';
            div1.appendChild(div)    
        }
    }
}  