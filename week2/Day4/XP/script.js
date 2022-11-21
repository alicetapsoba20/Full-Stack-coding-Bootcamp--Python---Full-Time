                //Exercice 1 : Informations
/*Des Instructions
Partie I : fonction sans paramètres

Créez une fonction appelée infoAboutMe()qui ne prend aucun paramètre.
La fonction devrait console.log une phrase vous concernant (c'est-à-dire votre nom, votre âge, vos loisirs, etc.).
Appelez la fonction.


Partie II : fonction à trois paramètres

Créez une fonction appelée infoAboutPerson(personName, personAge, personFavoriteColor)qui prend 3 paramètres.
La fonction doit console.log une phrase sur la personne (c'est-à-dire "Vous vous appelez ..., vous avez .. ans, votre couleur préférée est ...")
Appelez la fonction deux fois avec les arguments suivants :
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")
 */

        //Partie1
function infoAboutMe() {
    console.log("je me nommes TAPSOBA ALICE j'ai ... age et j'aime bien la lecture")
}
infoAboutMe()


   
        //Partie2

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log("Vous vous appelez" + " " + personName + "," + "vous avez " + " " + personAge + " " + "ans, votre couleur préférée est" + " " + personFavoriteColor)
}
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")

/********************************************************************************************/
            //Exercice 2 : Conseils

/*Des Instructions
John a créé un calculateur de pourboire simple pour aider à calculer le montant du pourboire quand lui et sa famille vont au restaurant.

Créez une fonction nommée calculateTip()qui ne prend aucun paramètre.

À l'intérieur de la fonction, utilisez promptpour demander à John le montant de la facture.

Voici les règles
Si la facture est inférieure à 50 $, laissez un pourboire de 20 %.
Si la facture est comprise entre 50 $ et 200 $, pourboire de 15 %.
Si la facture est supérieure à 200 $, laissez un pourboire de 10 %.

Console.log le montant du pourboire et la facture finale (facture + pourboire).

Appelez la calculateTip()fonction.*/

function calculateTip() {

    let montantFacture = prompt("John veillez entrer le montant de la facture:");

    if (montantFacture <= 50) {
        let pourboir = (montantFacture * 20) / 100;
        
    } else if (montantFacture > 50 && montantFacture <= 200) {
        let pourboir = (montantFacture * 15) / 100;
        
    } else {
        let pourboir = (montantFacture * 10) / 100;
        
    }
    let sommeTotale = montantFacture + pourboir;
    console.log("Le montant du pourboire et  de la facture finale est :" + " " + sommeTotale)
}
calculateTip()
/********************************************************************************************/

            //Exercice 3 : Trouver Les Nombres Divisibles Par 23


/*Des Instructions
Créez un appel de fonction isDivisible()qui ne prend aucun paramètre.

Dans la fonction, parcourez les nombres de 0 à 500.

Console.log tous les nombres divisibles par 23.

À la fin, console.log la somme de tous les nombres divisibles par 23.

Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
391 414 437 460 483
Sum : 5313


Bonus : Ajoutez un diviseur de paramètre à la fonction.

isDivisible(divisor)

Example:
isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
isDivisible(45) : Console.log all the numbers divisible by 45, and their sum
 */

function isDivisible() {
    for (let i = 0; i <= 500; i++) {
        if ((i % 23) == 0) {
            console.log(i)
            let somme = i;
            somme += somme;
        }
    }
    console.log("la valeur de la somme :" + somme)
}
isDivisible()

/********************************************************************************************/

                    //Exercice 4 : Liste De Courses
/*Des Instructions
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
Ajoutez les objets stocket pricesà votre fichier js.

Créez un tableau appelé shoppingListavec les éléments suivants : "banane", "orange" et "pomme". Cela signifie que vous avez 1 banane, 1 orange et 1 pomme dans votre panier.

Créez une fonction appelée myBill()qui ne prend aucun paramètre.

La fonction doit retourner le prix total de votre shoppingList. Pour ce faire, vous devez suivre ces règles :
L'article doit être en stock. ( Astuce : vérifier if .. in)
Si l'article est en stock, découvrez le prix dans l' pricesobjet.

Appelez la myBill()fonction.

Bonus : Si l'article est en stock, diminuez le stock de l'article de 1 */

let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

let shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let somme = 0;
    for (let i = 0; i <= shoppingList.length; i++) {
        
        for (let j in stock) {
            if (shoppingList[i] == j) {
                
                somme = somme + prices[j];
            }
        }
    }
    return somme;
}
/********************************************************************************************/

                //Exercice 5 : Qu'y A-T-Il Dans Mon Portefeuille ?
/*Des Instructions
Remarque : Lire l'illustration (point 4), tout en lisant les instructions

Créez une fonction nommée changeEnough(itemPrice, amountOfChange)qui reçoit deux arguments :
un prix d'article
et un tableau représentant le montant de la monnaie dans votre poche.

Dans la fonction, déterminez si vous pouvez ou non vous permettre l'article.
Si la somme du changement est supérieure ou égale au prix de l'article (c'est-à-dire que cela signifie que vous pouvez vous permettre l'article), la fonction doit renvoyer true
Si la somme du changement est inférieure au prix de l'article (c'est-à-dire que cela signifie que vous ne pouvez pas acheter l'article), la fonction doit renvoyer false

Le changement sera toujours représenté dans l'ordre suivant : quarts, dimes, nickels, pennies.
A quarters is 0.25
A dimes is 0.10
A nickel is 0.05
A penny is 0.01


4. Pour illustrer :

Après avoir créé la fonction, invoquez-la comme ceci :

changeEnough(4.25, [25, 20, 5, 0])
La valeur 4.25représente le prix de l'article
Le tableau [25, 20, 5, 0]représente 25 quarts, 20 dimes, 5 nickels et 0 centimes.
La fonction devrait retourner true, car avoir 25 quarts, 20 dimes, 5 nickels et 0 centimes vous donne ce 6.25 + 2 + .25 + 0 = 8.50qui est supérieur à 4,25 (le montant total dû)


Exemples

changeEnough(14.11, [2,100,0,0]) => returns false
changeEnough(0.75, [0,0,20,5]) => */

function changeEnough(itemPrice, amountOfChange) {
    let quarter = amountOfChange[0] * 0.25;
    let dimes = amountOfChange[1] * 0.10;
    let nickel = amountOfChange[2] * 0.05;
    let penny = amountOfChange[3] * 0.01;

    let montTotal = quarter + dimes + nickel + penny;

    if (montTotal > itemPrice) {
        return true;
    } else {
        return false;
    }
}
console.log(changeEnough(14.11, [2, 100, 0, 0]))

/********************************************************************************************/

                //Exercice 6 : Frais De Vacances
/*Des Instructions
Créons des fonctions qui calculent les coûts de vos vacances :

Définissez une fonction appelée hotelCost().
Il doit demander à l'utilisateur le nombre de nuits qu'il souhaite séjourner à l'hôtel.
Si l'utilisateur ne répond pas ou si la réponse n'est pas un chiffre, redemandez.
L'hôtel coûte 140 $ par nuit. La fonction doit être returnle prix total de l'hôtel.

Définissez une fonction appelée planeRideCost().
Il devrait demander à l'utilisateur sa destination.
Si l'utilisateur ne répond pas ou si la réponse n'est pas une chaîne, redemandez.
La fonction devrait avoir returnun prix différent selon l'emplacement.
"Londres": 183$
"Paris" : 220$
Toute autre destination : 300$

Définissez une fonction appelée rentalCarCost().
Il doit demander à l'utilisateur le nombre de jours qu'il souhaite louer la voiture.
Si l'utilisateur ne répond pas ou si la réponse n'est pas un chiffre, redemandez.
Calculez le coût de location de la voiture. La voiture coûte 40 $ par jour.
Si l'utilisateur loue une voiture pendant plus de 10 jours, il bénéficie d'une réduction de 5 %.
La fonction doit returnindiquer le prix total de la location de voiture.

Définissez une fonction appelée totalVacationCost()qui renvoie le coût total des vacances de l'utilisateur en appelant les 3 fonctions que vous avez créées ci-dessus.
Exemple : La voiture coûte : $x, l'hôtel coûte : $y, les billets d'avion coûtent : $z.
Astuce : Vous devez appeler les fonctions hotelCost(), planeRideCost()et rentalCarCost()à l'intérieur de la fonction totalVacationCost().

Appelez la fonctiontotalVacationCost()

Bonus : Au lieu d'utiliser un promptà l'intérieur des 3 premières fonctions, utilisez uniquement une invite à l'intérieur de la totalVacationCost()fonction. Vous devez modifier les 3 premières fonctions en conséquence. */

function hotelCost() {
    let nombresNuits = parseInt(prompt("Combien de nuits souhaitez vous passer à l'hotel ? :"));
    while ((typeof(nombresNuits) != 'number') || nombresNuits == null) {
        let nombresNuits = parseInt(prompt("Combien de nuits souhaitez vous passer à l'hotel ? :"));
    }

    let prix = nombresNuits * 140;
    return prix;
}

function planeRideCost() {
    let destination = prompt("Quelle est votre destination ? :");
    while ((typeof(destination) != 'string') || destination == null) {
        let destination = prompt("Quelle est votre destination ? :");
    }
    if (destination == 'Londres') {
        return 183;
    } else if (destination == 'Paris') {
        return 220;
    } else {
        return 300;
    }
}

function rentalCarCost() {
    let nombresJours = parseInt(prompt("Combien de jours souhaitez vous loué la voiture ? :"));
    while ((typeof(nombresJours) != 'number') || nombresJours == null) {
        let nombresJours = parseInt(prompt("Combien de jours souhaitez vous loué la voiture ? :"));
    }

    if (nombresJours >= 10) {
        let reduction = nombresJours - ((nombresJours * 5) / 100);
        let prix = reduction * 40;
        return prix;
    } else {
        let prix = nombresJours * 40;
        return prix;
    }

}



function totalVacationCost() {
    let coutTotal = planeRideCost() + rentalCarCost() + hotelCost();
    return coutTotal;
}

totalVacationCost()