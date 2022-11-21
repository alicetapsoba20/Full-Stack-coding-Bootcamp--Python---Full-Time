                     //Exercice 1 : Liste Des Personnes

                     //Partie I - Examen Des Tableaux

       let people = ["Greg", "Mary", "Devon", "James"];
       people.shift();//Suppression de "Greg" du tableau people
       people.splice( 2, 1,"Jason");//remplacement de "James" par "Jason"
       people.push("Alice");//ajout de mon nom
       console.log(people.indexOf("Mary"));//index de Mary
       console.log(people.slice(1,3));
       console.log(people)
       // 6. Écrivez le code qui donne l'index de "Foo". Pourquoi renvoie-t-il -1 ?
       console.log(people.indexOf("Foo"));
       // l'index de "Foo renvoie" -1 car "Foo" n'est pas présent dans tableau people.
       let last = people[people.length -1];
       //console.log(last);

                     //Partie II - Boucles

//1.À l'aide d'une boucle, parcourez le peopletableau et console.log chaque personne.
for(let i=0;i<=[people.length -1];i++){

       console.log(people[i]);}

//2.À l'aide d'une boucle, parcourez le peopletableau et quittez la boucle après avoir console.log "Jason" .

for (let i= 0;i<=[people.length -1];i++){
       if (people[i]=="Jason"){
              break;
       }
       console.log("Jason");
}

/**************************************************************************************************************************************************************/

                     //Exercice 2 : Vos Couleurs Préférées

let colors =["Bleu","Rouge","Blanc","Violet","Marron"]
 for(let i=1;i<=[colors.length -1];i++){
console.log("Mon choix n°",i, "est :",colors[i]);}

/**************************************************************************************************************************************************************/

      
                            // Exercice 3 : Répéter La Question
// Des Instructions
// Demander à l'utilisateur un numéro.
// Astuce : Vérifiez le type de données que vous recevez à partir de l'invite (c.-à-d. Utilisez la typeofméthode)

// Tant que le nombre est inférieur à 10, continuez à demander à l'utilisateur un nouveau numéro.
// Astuce : Quelle whileboucle est la plus pertinente pour cette situation ?

let numero = prompt("veuillez entrer un numéro")
typeof(numero);
while(numero < 10){
       numero++;
       console.log(prompt("veuillez entrer un numéro"))
}

/**************************************************************************************************************************************************************/


                                   // Exercice 4 : Gestion Du Bâtiment
// Des Instructions:
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }


// Revue Sur Les Objets
// Copiez et collez l'objet ci-dessus dans votre fichier Javascript.

// Console.log le nombre d'étages du bâtiment.

// Console.log combien d'appartements sont aux étages 1 et 3.

// Console.log le nom du deuxième locataire et le nombre de pièces qu'il possède dans son appartement.

// Vérifiez si la somme du loyer de Sarah et de David est supérieure au loyer de Dan. Si c'est le cas, augmentez le loyer de Dan à 1200.

const building = {
       numberOfFloors: 4,
       numberOfAptByFloor: {
           firstFloor: 3,
           secondFloor: 4,
           thirdFloor: 9,
           fourthFloor: 2,
       },
       nameOfTenants: ["Sarah", "Dan", "David"],
       numberOfRoomsAndRent:  {
           sarah: [3, 990],
           dan:  [4, 1000],
           david: [1, 500],
       },
   }
  /*2*/console.log("le nombre d'etages du batiment est : ",building.numberOfFloors);
  /*3*/Console.log ("le nombre d'appartements qui sont aux étages 1 et 3 sont : "+ building.numberOfAptByFloor.thirdFloor);
  /*4*/Console.log ("le nom du deuxième locataire et le nombre de pièces qu'il possède dans son appartement est : ",building.nameOfTenants[1] + ":" + building.numberOfRoomsAndRent.dan[0]);

  /*5-Vérifiez si la somme du loyer de Sarah et David est plus
importante que celle de Dan. Si c’est le cas, augmentez le loyer de Dan à 1200.*/

if ((building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]) > building.numberOfRoomsAndRent.dan[1]) {
    let danLoyer = building.numberOfRoomsAndRent.dan[1] + 200;
    console.log(danLoyer)
}

/**************************************************************************************************************************************************************/

                            //Exercice 5 : Famille
/* Des Instructions
Créez un objet appelé famille avec quelques paires clé-valeur.
A l' aide d'une for inboucle, console.log les clés de l'objet.
À l' aide d'une for inboucle, console.log les valeurs de l'objet.*/

let famille = {
       papa: 'TAPSOBA Papa',
       prenom: 'TAPSOBA Maman',
       soeur: 'TAPSOBA soeur',
       frere:'TAPSOBA frère',
   }
   
   for (let i in famille) {
       console.log(i)
   }
   
   for (let i in famille) {
       console.log(famille[i])
   }

/**************************************************************************************************************************************************************/
                            //Exercice 6 : Rodolphe
/*Des Instructions
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}
Étant donné l'objet ci-dessus et en utilisant un for loop, console.log "mon nom est Rudolf le raindeer"
 */

let details = {
       my: 'name',
       is: 'Rudolf',
       the: 'raindeer'
   }
   let tab = []
   for (let i in details) {
       tab.push(i);
   }
   console.log(tab[0] + " " + details.my + " " + tab[1] + " " + details.is + " " + tab[2] + " " + details.the)

   /**************************************************************************************************************************************************************/


                        //Exercice 7 : Groupe Secret
/*Des Instructions
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
Un groupe d'amis a décidé de créer une société secrète. Le nom de la société sera la première lettre de chacun de leurs noms triés par ordre alphabétique.
Indice : une chaîne est un tableau de lettres
Console.log le nom de leur société secrète. La sortie doit être "ABJKPS" */
   
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

console.log(names[0][0].concat(names[1][0]).concat(names[2][0]).concat(names[3][0]).concat(names[4][0]).concat(names[5][0]))