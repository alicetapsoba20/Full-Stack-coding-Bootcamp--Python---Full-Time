            //Exercice 1 : Vérification De L'IMC
/*Des Instructions
Astuce :
- Vous devez utiliser des fonctions pour réaliser cet exercice, pour cela jetez un œil à la leçon de demain.

Créez deux objets, chaque objet doit contenir les détails d'une personne. Voici les détails:
Nom et prénom
Masse
Hauteur

Chaque objet doit également avoir une clé dont la valeur est une fonction (c'est-à-dire une méthode), qui calcule l'indice de masse corporelle (IMC) de chaque personne

En dehors des objets, créez une fonction JS qui compare l'IMC des deux objets.

Affichez le nom de la personne qui a le plus grand IMC.*/


let personne = [
    {
        nom : "TAPSOBA",
        prenom : "Alice",
        masse : 60,
        taille : 160,
        imc : function () {
            return this.masse/(this.taille*this.taille);
        }
    },
    {
        nom : "TAPSOBA",
        prenom : "Olivia",
        masse : 70,
        taille : 165,
        imc : function () {
            return this.masse/(this.taille*this.taille);
        }
    }
];
//3//4
function compareImc(){
    if (personne[0].imc() > personne[1].imc())
        console.log(personne[0].nom, personne[0].prenom , "a le plus grand IMC");
    else
        console.log(personne[1].nom , personne[1].prenom  , "a le plus grand IMC");
}


/********************************************************************************************************************************************************************************************/





                //Exercice 2 : Moyenne Scolaire
/*Des Instructions
Astuce :
- Cet exercice est plus délicat que les autres. Vous devez réfléchir à sa structure avant de commencer à coder.
- Vous devez utiliser des fonctions pour réaliser cet exercice, pour cela jetez un oeil à la leçon de demain.

Dans cet exercice, nous allons créer une fonction qui prend un tableau de notes comme argument et console.log la moyenne.

Créez une fonction appelée findAvg(gradesList)qui prend un argument appelé gradesList.

Votre fonction doit calculer et console.log la moyenne.

Si la moyenne est supérieure à 65, faites savoir à l'utilisateur qu'il a réussi

Si la moyenne est inférieure à 65, faites savoir à l'utilisateur qu'il a échoué et qu'il doit répéter le cours.
Bonus Essayez de diviser les parties 1, 2 et 3, 4 de cet exercice en deux fonctions distinctes.
Astuce Une fonction doit appeler l'autre.*/

let note = [10,15,16,11,18,05,09,16,20,17,12];
let somme = 0;
let moyenne = 0;
for(let i=0; i<note.length;i++){
  somme = somme+note[i];
  moyenne = somme/note.length;
}
console.log("votre moyenne est de :", moyenne);
if(moyenne<10){
  console.log("Vous avez échoué au test");
}
else if (moyenne>10){
  console.log("Vous etes admis au test");
}