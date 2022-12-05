            //Exercice 1 : Is_Blank


/*Des Instructions
Écrivez un programme pour vérifier si une chaîne est vide ou non.

console.log(isBlank('')); --> true
console.log(isBlank('abc')); --> false*/


function isBlank(mot) {
    if (mot == "") return true;
    else return false;
}

console.log(isBlank(''));
console.log(isBlank('abc'));

/*********************Exercice 2***************************/

            /*Exercice 2 : Abrév_name
Des Instructions
Écrivez une fonction JavaScript pour convertir une chaîne en une forme abrégée.

console.log(abbrevName("Robin Singh")); --> "Robin S."*/


function abbrevName(mot) {
    mot = mot.split(" ");
    motC = mot[0] + " ";
    for (let i = 1; i < mot.length; i++)
        motC += mot[i][0].toUpperCase() + ". ";
    return motC;
}


console.log(abbrevName("Robin Singh"));
console.log(abbrevName("Kiswendsida Alice Nicole Tapsoba"));

/************************Exercice 3******************************/

            /*Exercice 3 : SwapCase

Des Instructions
Écrivez une fonction JavaScript qui prend une chaîne comme argument et échange la casse de chaque caractère.
Par exemple :

if you input 'The Quick Brown Fox' 
the output should be 'tHE qUICK bROWN fOX'.*/

function swapCase (mot) {
    let motC = "";
    for (let i = 0; i <mot.length;i++)
        if (mot[i] == mot[i].toUpperCase()) 
            motC += mot[i].toLowerCase();
        else 
            motC += mot[i].toUpperCase();
    console.log(motC);
}

swapCase('The Quick Brown Fox');


/******************************Exercice 4************************/

            /*Exercice 4 : Valeur Omniprésente
Des Instructions
Créez une fonction qui détermine si un argument est omniprésent pour un tableau donné.
Une valeur est omniprésente si elle existe dans chaque sous-tableau à l'intérieur du tableau principal.
Pour illustrer:

[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// 3 exists in every element inside this array, so is omnipresent.
Exemples

isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false */


function isOmnipresent(tabNumber, Number) {
    for (x of tabNumber) 
        for (y of x)
            if (Number == y) return true;
            else return false;
    }
    
    isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1);
    isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6);

