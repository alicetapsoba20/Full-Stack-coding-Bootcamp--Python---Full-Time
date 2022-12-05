            //Exercice 1 : Jouez À Un Jeu De Devinettes
	
    /*Exercice 1 : Jouez À Un Jeu De Devinettes
Des Instructions
Créez un nouveau dossier sur votre ordinateur.
Clonez ou téléchargez les fichiers index.htmlet à partir de ce lien github .style.css
Suivez les étapes écrites ci-dessous


Pas
Explication du jeu : le but du jeu est de deviner le nombre que l'ordinateur a en tête.

Première Partie
Créez un fichier JS et liez-le au fichier index.html .

Jetez un oeil à votre fichier html, vous devriez avoir un bouton avec un événement "onclick". Cet événement est égal à la fonction playTheGame() . Cela signifie que lorsque vous cliquerez sur le bouton, la fonction playTheGame() sera appelée.
Nous en apprendrons plus sur les événements la semaine prochaine ;)


Créons maintenant la fonction :

Dans le fichier JS, créez une fonction appelée playTheGame() qui ne prend aucun paramètre.
Dans la fonction, commencez par demander à l'utilisateur s'il souhaite jouer au jeu (Astuce : utilisez la confirm()fonction intégrée).

Si la réponse est fausse, alertez « Pas de problème, au revoir ».

Si sa réponse est vraie, suivez ces étapes :
Demandez à l'utilisateur d'entrer un nombre entre 0 et 10 (Astuce : utilisez la prompt()fonction intégrée). Vous devez ensuite vérifier la validité du numéro d'utilisateur :

Si l'utilisateur n'a pas saisi de numéro (c'est-à-dire s'il a saisi un autre type de données), l'alerte « Désolé, pas un numéro, au revoir ».
Si l'utilisateur n'a pas saisi de chiffre entre 0 et 10, l'alerte « Désolé, ce n'est pas un bon chiffre, au revoir ».
Sinon (c'est-à-dire qu'il a entré un nombre entre 0 et 10 ), créez une variable nommée computerNumberoù la valeur est un nombre aléatoire entre 0 et 10 (Astuce : utilisez la Math.random()fonction intégrée). Assurez-vous que le nombre est arrondi.


Deuxième Partie
En dehors de la fonction playTheGame() , créez une nouvelle fonction nommée compareNumbers(userNumber,computerNumber) qui prend 2 paramètres : userNumber et computerNumber

Le but de cette fonction est de vérifier si le userNumber est le même que le computerNumber :
Si userNumber est égal à computerNumber, alertez "WINNER" et arrêtez le jeu.

Si userNumber est plus grand que computerNumber, alertez "Votre numéro est plus grand que celui de l'ordinateur, devinez à nouveau" (Astuce : utilisez la prompt()fonction intégrée pour demander à l'utilisateur un nouveau numéro).

Si userNumber est inférieur à computerNumber, alertez "Votre numéro est plus petit que celui de l'ordinateur, devinez à nouveau" (Astuce : utilisez la prompt()fonction intégrée pour demander à l'utilisateur un nouveau numéro).

Si l'utilisateur a deviné plus de 3 fois, alertez "hors de chances" et quittez la fonction.
 */
    
            //Premiere partie
	function vNomb(nombre) {
		type = Number(nombre);
		if (!type) {
			console.log("Désolé, pas un numéro");
			return false;
		} else if (nombre < 0 && nombre > 10){
			console.log("Désolé, ce n'est pas un bon chiffre");
			return false;
		} else {
			return true;
		}
	}

	function numAléatoire(min,max) {
		min = Math.ceil(min);
		max = Math.floor(max+1);
		let nombre = Math.floor(Math.random()* (max - min)) + min;
		return nombre;
	}

	function playTheGame() {
		let confirmation=confirm("Voulez vous jouer au jeu?")
		if (!confirmation) {//1
			console.log("Pas de problème au revoir");
			return;
		} else {//2
			let userNumber;
			do {
				userNumber = prompt("Entrez un nombre entre 0 et 10",);
				if (vNomb(userNumber)) {
					computerNumber = numAléatoire(0,10);
					compareNumbers(userNumber,computerNumber);
				}
			} while (!vNomb(userNumber))//prime
		}

	}

/***********************************Deuxieme partie**********************************************/

	function compareNumbers(userNumber,computerNumber) {
		let i=0;
		while(i!=4) {
			if (userNumber == computerNumber) {
				alert("WINNER");
				return;
			} else if (userNumber > computerNumber && i!=3) {
				userNumber = prompt("Votre numéro est plus grand que celui de l'ordinateur, devinez à nouveau"); 
				while(!vNomb(userNumber))
					userNumber = prompt("Entrez un nombre entre 0 et 10");
			}
			else if (userNumber < computerNumber && i!=3) {
				userNumber = prompt("Votre numéro est plus petit que celui de l'ordinateur, devinez à nouveau"); 
				while(!vNomb(userNumber))
					userNumber = prompt("Entrez un nombre entre 0 et 10");
			}	
			else if ( i == 3) {
				alert("Hors de chances");
				return;
			}
			i++;
		}
	}