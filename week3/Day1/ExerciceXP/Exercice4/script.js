/*Exercice 4 : Ma Liste De Livres
Des Instructions
Jetez un œil à ce lien pour obtenir de l'aide.

Le but de ce défi est d'afficher une liste de deux livres sur votre navigateur.

Dans le corps de la page HTML, créez un div vide :
<div class="listBooks"></div>
Dans le fichier js, créez un tableau appelé allBooks. Il s'agit d'un tableau d'objets. Chaque objet est un livre qui possède 4 clés (soit 4 propriétés) :
Titre,
auteur,
image : une url,
déjàRead : qui est un booléen (vrai ou faux).

Initiez le tableau avec 2 livres de votre choix (c'est-à-dire ajoutez manuellement 2 objets livres dans le tableau)
Exigences : Toutes les instructions ci-dessous doivent être codées dans le fichier js :
À l'aide du DOM, rendez les livres dans un tableau HTML (le tableau HTML doit être ajouté au <div>créé dans la partie 1).
Pour chaque livre :
Vous devez afficher le titre du livre et l'auteur du livre.
Exemple : HarryPotter écrit par JKRolling.
La largeur de l'image doit être définie sur 100px.
Si le livre est déjà lu. Définissez la couleur des détails du livre sur rouge. */

let allBooks = [
	{
		title :"Tout pour reussir",
		author :"Tapsoba Alice",
		image :"http://",
		alreadyRead :false
	},
	{
		title :"Harry Potter",
		author :"Roman de J.K. Rowling",
		image :"http://",
		alreadyRead : true
	}
];
	let div = document.getElementsByClassName("listBooks")
	let table = document.createElement("table");
	let tr1 = document.createElement("tr");
	let tr2 = document.createElement("tr");
	let tr3 = document.createElement("tr");
	let th1 = document.createElement("th");
	let th2 = document.createElement("th");
	let th3 = document.createElement("th");
	let td1 = document.createElement("td");
	let td2 = document.createElement("td");
	let td22 = document.createElement("td");
	let td3 = document.createElement("td");
	let td4 = document.createElement("td");
	let td44 = document.createElement("td");
	let img1 = document.createElement("img");
	let img2 = document.createElement("img"); 
	div[0].appendChild(table);
	table.appendChild(tr1);
	table.appendChild(tr2);
	table.appendChild(tr3);
	tr1.appendChild(th1);
	tr1.appendChild(th2);
	tr1.appendChild(th3);
	tr2.appendChild(td1);
	tr2.appendChild(td2);
	tr2.appendChild(td22);
	tr3.appendChild(td3);
	tr3.appendChild(td4);
	tr3.appendChild(td44);
	td22.appendChild(img1);
	td44.appendChild(img2);
	th1.innerHTML = "Title";
	th2.innerHTML = "Author";
	th3.innerHTML = "Image";
	td1.innerHTML = allBooks[0].title;
	td2.innerHTML = allBooks[0].author;
	td3.innerHTML = allBooks[1].title;
	td4.innerHTML = allBooks[1].author;
	
	img1.setAttribute("src","logo.png");
	img2.setAttribute("src","img.jpg");
	img1.setAttribute("style","width : 100px");
	img2.setAttribute("style","width : 100px");
	console.log(img2);

	if (allBooks[0].alreadyRead == true) {
		tr1.setAttribute("style","color : red")	
	}
	if (allBooks[1].alreadyRead == true) {
		tr2.setAttribute("style","color : red")	
	}