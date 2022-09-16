                     //Exercice 1 : Liste Des Personnes

                     //Partie I - Examen Des Tableaux

       let people = ["Greg", "Mary", "Devon", "James"];
       people.shift();//Suppression de "Greg" du tableau people
       people.splice( 2, 1,"Jason");//remplacement de "James" par "Jason"
       people.push("Alice");//ajout de mon nom
       console.log(people.indexOf("Mary"));//index de Mary
       console.log(people.slice(1,3));
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

              //Exercice 2 : Vos Couleurs Préférées

let colors =["Bleu","Rouge","Blanc","Violet","Marron"]