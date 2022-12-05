/*Créez Une Calculatrice Complète En Javascript.
Introduction:
Aujourd'hui, nous allons créer une calculatrice entièrement fonctionnelle. Pour ce faire, nous devons faire interagir nos fichiers HTML et Javascript.
Nous utiliserons Javascript pour calculer dynamiquement le résultat des boutons qui ont été cliqués sur le HTML.
Nous ajouterons un attribut appelé onclickà chaque bouton . L' onclickattribut nous permet d'appeler une fonction de notre fichier Javascript lorsque le bouton est cliqué.
Par exemple, si vous cliquez sur le chiffre 2 sur la calculatrice (c'est-à-dire vu ci-dessous dans les assets), la fonction number(2)sera appelée. L'argument est la valeur du bouton .

Utilisez HTML CSS pour le visuel.

Des Instructions:
Créez un fichier HTML pour votre calculatrice et un fichier JS pour les fonctionnalités de la calculatrice.
Vous devez créer 3 fonctions dans le fichier js :
number(num)
operator(operator)
equal()
Astuce : vous pouvez utiliser la eval()méthode pour vous aider dans vos calculs.
Avant de coder, prenez le temps de comprendre toutes les parties de l'exercice et leur processus. Vous pouvez l'écrire quelque part si cela vous aide (recommandé).
Bonus : créer les boutons RESET et CLEAR.
 */

let tabOperation = "";

function number(num) {
	tabOperation += num;
}


function operator(operator) {
	tabOperation += operator;
}


function equal() {
	alert(`${tabOperation} = ${eval(tabOperation)}`);
	tabOperation = "";
}

function reset() {
	tabOperation = "";
}

function clean() {
	tabOperation = tabOperation.split("");
	tabOperation.pop();
	tabOperation = tabOperation.join("");
}