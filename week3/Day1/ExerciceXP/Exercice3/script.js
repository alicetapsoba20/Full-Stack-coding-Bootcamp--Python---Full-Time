/*Exercice 3 : Changer La Barre De Navigation
Des Instructions

Dans le <div>, modifiez la valeur de l'attribut id de navBar à socialNetworkNavigation , à l'aide de la setAttributeméthode .

Nous allons ajouter un nouveau <li>au <ul>.
Tout d'abord, créez une nouvelle <li>balise (utilisez la createElementméthode).
Créez un nouveau nœud de texte avec "Déconnexion" comme texte spécifié.
Ajoutez le nœud de texte au nœud de liste nouvellement créé ( <li>).
Enfin, ajoutez ce nœud de liste mis à jour à la liste non ordonnée ( <ul>), en utilisant la appendChildméthode.

Prime
Utilisez les firstElementChildpropriétés et lastElementChildpour récupérer le premier et le dernier <li>élément de leur élément parent ( <ul>). Affichez le texte de chaque lien. ( Astuce : utilisez la textContentpropriété). */

let div = document.getElementsByTagName("div");
	div[0].setAttribute("id","socialNetworkNavigation");
	console.log(div[0]);
	//3
	let ul = document.getElementsByTagName("ul");
	let li1 = document.createElement("li");
	let text = document.createTextNode("Déconnexion");
	li1.appendChild(text);
	ul[0].appendChild(li1);
	//4
	console.log(ul[0].firstElementChild.textContent)
	console.log(ul[0].lastElementChild.textContent)