/*Exercice 2 : Utilisateurs Et Style
Des Instructions

Ajoutez une couleur d'arrière-plan "bleu clair" et un peu de rembourrage au fichier <div>.

Ne pas afficher le <li>qui contient le nœud de texte "John".

Ajoutez une bordure au <li>qui contient le nœud de texte "Pete".

Modifiez la taille de la police de tout le corps.

Bonus : Si la couleur de fond du divest "bleu clair", alertez "Bonjour x et y" (x et y sont les utilisateurs dans la div). */

let divElem = document.getElementsByTagName('div')[0];
    divElem.style.background = "blue"

	let li = document.getElementsByTagName("li");
	let ul = document.getElementsByTagName("ul");
	for(let i=0;i<li.length;i++){
		if (li[i].innerHTML == "John") {
			ul[0].removeChild(li[i]);
		}
	}

	for(let i=0;i<li.length;i++){
		if (li[i].innerHTML == "Pete") {
			li[i].style.border = "2px solid black";
		}
	}
	
	body = document.getElementsByTagName("body");
	body[0].setAttribute("style","font-size: 150%;");