// //       Exercice

/* Demander à l'utilisateur plusieurs mot (séparés par des virgules).
Mettez les mot dans un tableau.
Console.log les mot un par ligne, dans un cadre rectangulaire comme indiqué ci-dessous.
Consultez les conseils et les exigences ci-dessous.
Par exemple, si l'utilisateur vous donne :
Hello, World, in, a, frame
vous le transformerez en : ["Hello", "World", "in", "a", "frame"]
qui s'afficherra comme suit :

des étoiles et des mot
 */


function motLong(mot) {
	let etoile = 0;
	for (let x of mot)
		if (etoile < x.length) 
			etoile = x.length;
	return etoile;
}

function etoile(etoile) {
	let etoile = "*";
	for (var i = etoile + 4; i > 1; i--) 
		etoile = etoile + "*";
	return etoile;
}

function afficher(mot) {
	mot = mot.split(",");
	etoile=motLong(mot);
	etoile=etoile(etoile);
	console.log(etoile);
	for (let x of mot) {
		let mot = "* " + x;
		for (i=mot.length; i < etoile+3; i++)
			mot = mot + " ";
		console.log(mot + "*");
	}
	console.log(etoile);
}

afficher(prompt("Entrez plusieurs mots séparés par des virgules"));


