                //Exercice 1 : Divisible Par Trois
/*Des Instructions
let numbers = [123, 8409, 100053, 333333333, 7]
Parcourez le tableau ci-dessus et déterminez si chaque nombre est divisible par trois ou non.
Chaque fois que vous bouclez console.log true ou false.*/

let numbers = [123, 8409, 100053, 333333333, 7];

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 3 == 0) {
        console.log("true")
    } else { console.log("false") }
}

/**************************************************************************************************************************************/

                    //Exercice 2 : Présence
/*Des Instructions
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}


Étant donné l'objet ci-dessus où la clé est le nom de l'étudiant et la valeur est le pays d'où il vient.

Invitez l'élève à donner son nom.

Si le nom est dans l'objet, console.log le nom de l'étudiant et le pays d'où il vient.
Par exemple:"Hi! I'm [name], and I'm from [country]."
Astuce : Vous n'avez pas besoin d'utiliser une boucle for, recherchez simplement l'instructionif ... in

Si le nom n'est pas dans l'objet, console.log :"Hi! I'm a guest." */

let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
}
let prenom = prompt("Quel est votre nom ? :");
console.log(prenom)
if (prenom in guestList) {
    console.log("Hi! I'm " + " " + prenom + "," + "and I 'm from" + " " + guestList.prenom)
} else {
    console.log("Hi! I'm a guest.")
}

/**************************************************************************************************************************************/

                    //Exercice 3 : Jouer Avec Les Chiffres
/*Des Instructions
let age = [20,5,12,43,98,55];
Exigences : N'utilisez pas les méthodes Javascript intégrées pour répondre aux questions suivantes. Vous devez créer la logique par vous-même. Utilisez des boucles for simples.


1. Console.log la somme de tous les nombres dans le tableau d'âge.
2. Console.log l'âge le plus élevé de la baie. */

let age = [20, 5, 12, 43, 98, 55]
let somme = 0
let maximun = age[0]
for (let i = 0; i < age.length; i++) {
    somme = somme + age[i]
    if (age[i] > maximun) {
        maximun = age[i]
    }
}

console.log("La somme de tout les nombres du tableau est :" + somme);
console.log("l'âge le plus élevé de la baie est :" + maximun);