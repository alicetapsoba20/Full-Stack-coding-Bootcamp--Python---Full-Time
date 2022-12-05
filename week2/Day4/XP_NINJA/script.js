/*Exercice 1 : Nombre Aléatoire
Des Instructions
Obtenez un nombre aléatoire entre 1 et 100.
Console.log tous les nombres pairs de 0 au nombre aléatoire.*/

let min = Math.ceil(1);
	let max = Math.floor(101);
	let nombre = Math.floor(Math.random()* (max - min)) + min;
	console.log(nombre);
	//2
	let pair= "";
	for ( let i = 1; i <= nombre; i++) 
		if (i%2 == 0 && i < nombre) 
			pair += i + " ";	
	console.log(pair);

    /********************** Exercice 2************************/

/*Exercice 2 : Lettres Majuscules
Des Instructions
Créez une fonction qui prend une chaîne comme argument.
Que la fonction retourne :
La chaîne, mais toutes les lettres des index pairs doivent être en majuscules.
La chaîne mais toutes les lettres des index impairs doivent être en majuscules.
Remarque :

L'indice 0 sera considéré comme pair.
L'argument de la fonction doit être une chaîne en minuscules sans espaces.
Par exemple,

capitalize("abcdef") will return ['AbCdEf', 'aBcDeF']*/

function capitalize(mot) {
    let motP = "";
    let motI = "";
    for ( let i = 0; i < mot.length; i++)
        if (i%2 == 0)
            motP += mot[i].toUpperCase();
        else
            motP += mot[i];
    for ( let i = 0; i < mot.length; i++)
        if (i%2 != 0)
            motI += mot[i].toUpperCase();
        else
            motI += mot[i];
    let result = [motP,motI];
    return result;
}

capitalize("abcdef");


    /********************** Exercice 3************************/


/*Exercice 3 : Est-Ce Palindrome ?
Des Instructions
Écrivez une fonction JavaScript qui vérifie si une chaîne est un palindrome ou non.
Remarque Un palindrome est un mot, une phrase ou une séquence qui s'écrit de la même manière à l'envers et à l'envers, par exemple madame, bob ou kayak.
palindrome*/



function palindrome(mot) {
    mot=mot.toLowerCase();
    if (mot.length%2 == 0)
        return false;
    else
        for(let i = 0; i < mot.length; i++)
            if (mot[i] != mot[mot.length-i-1])
                    return false;
    return true;
}

palindrome("Madam");

    /********************** Exercice 4************************/


/*Exercice 4 : Plus Grand Nombre
Des Instructions
Créez une fonction appelée biggestNumberInArray(arrayNumber)qui prend un tableau comme paramètre et renvoie le plus grand nombre.
Note : Cette fonction devrait fonctionner avec n'importe quel tableau ;
Exemple:

const array = [-1,0,3,100, 99, 2, 99] ;// should return 100 
const array2 = ['a', 3, 4, 2]; // should return 4 
const array3 = []; // should return 0*/

function biggestNumberInArray(arrayNumber) {
    let biggestNumber = 0;
    if (arrayNumber == [])
        return 0;
    for (x of arrayNumber)
        if (Number(x) && x > biggestNumber)
            biggestNumber = x;
    return biggestNumber;
}

biggestNumberInArray([-1,0,3,100, 99, 2, 99]);
biggestNumberInArray(['a', 3, 4, 2]);
biggestNumberInArray([]);

    /********************** Exercice 5************************/


/*Exercice 5 : Éléments Uniques
Des Instructions
Écrivez une fonction JS qui prend un tableau et renvoie un nouveau tableau avec uniquement des éléments uniques.

Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5] */

function uniqueListe(tabNumber) {
    let tabNumber1 = [];
    for (x of tabNumber){
        let valide = 0;
        for (y of tabNumber1)
            if (tabNumber1 == [])
                tabNumber1[0]=x;
            else if (x == y)
                valide = 1;
        if (valide==0)
            tabNumber1[tabNumber1.length]=x;
    }
    return tabNumber1;
}

uniqueListe([1,2,3,3,3,3,4,5]);
	