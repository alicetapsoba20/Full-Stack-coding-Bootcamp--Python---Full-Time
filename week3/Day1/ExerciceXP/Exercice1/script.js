/*Exercice 1 : Utilisateurs
Des Instructions

Utilisation de Javascript :
Récupérez le divet console.log it
Changez le nom "Pete" en "Richard".
Remplacez chaque prénom des deux <ul>'spar votre nom.
Supprimez le <li>qui contient le nœud de texte "Sarah".

Bonus - Utilisation de Javascript :
Ajoutez une classe appelée student_listaux deux <ul>'s.
Ajoutez les classes universityet attendanceau premier <ul>. */

let div = document.getElementById("container");
	console.log(div);
	let lis = document.getElementsByTagName("li");
	for(let i=0;i<lis.length;i++){
		if (lis[i].innerHTML == "Pete") {
			lis[i].innerHTML = "Richard";
		}
	}
	for(let i=0;i<lis.length;i++){
		if (lis[i].innerHTML == "Sarah") {
			lis[i].setAttribute("id","sup")
		}
		lis[i].innerHTML = "Tapsoba";
	}
	let sup = document.getElementById("sup")
	let ul = document.getElementsByClassName("list");
	ul[1].removeChild(sup);
	//3
	ul[0].setAttribute("class",ul[0].className+" student_list")
	ul[1].setAttribute("class",ul[1].className+" student_list")
	ul[0].setAttribute("class",ul[0].className+" university attendance")