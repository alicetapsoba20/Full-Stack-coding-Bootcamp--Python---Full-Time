          /*  //Exercice 1 : Évaluation
    
            5 >= 1
    // Prediction:true car 5 est plus grand que 1
    console.log(5 >= 1);
    // Actual:true

            0 === 1
    // Prediction:false car 0 n'est pas égale à 1 meme s'ils sont du meme type
    console.log(0 === 1);
    // Actual:false

            4 <= 1
     // Prediction:false car 4 est plus grand que 1
    console.log( 4 <= 1);
    // Actual:false

            1 != 1
    // Prediction:false car 1 égal 1
    console.log(1 != 1);
    // Actual:false

            "A" > "B"
    // Prediction: false car selon le code ASCII A=065 qui est plus petit que B=066
    console.log("A" > "B");
    // Actual:false

              "B" < "C"
    // Prediction:true car 066 est plus petit que 067 selon le code ASCII
    console.log(5 >= 1);
    // Actual:true

             "a" > "A"
    // Prediction:true car a=097 est plus grand que A=065 selon le code ASCII
    console.log("a" > "A");
    // Actual:true

            "b" < "A"
     // Prediction:false car b=098 est plus grand que A=065 selon le code ASCII
    console.log("b" < "A");
    // Actual:false

            true === false
    // Prediction:false car true est différent de false
    console.log(true === false);
    // Actual:false
    
            true != true
    // Prediction:false car true n'est pas different de true
    console.log(true != true);
    // Actual:false*/


                    //Exercice 2 : Demander Des Nombres

     let numb = prompt("Saisir des chiffres separés par des virgules");
     n = numb.split(",");
     n = Number(n);
     console.log(n);



        /*Exercice 3 : Trouver Nemo
Des Instructions
Indice : if statement (la leçon de demain)

Demandez à l'utilisateur de vous donner une phrase contenant le mot "Nemo". Par exemple"I love the movie named Nemo"
Trouver le mot "Nemo"
Console.log une chaîne comme suit :"I found Nemo at [the position of the word Nemo]".
Si vous ne trouvez pas Nemo, console.log "Je ne trouve pas Nemo".*/

            let sentence = prompt("Entrer une phrase contenant le mot Nemo");
           let word = sentence.indexOf("Nemo");
            if( word > -1){

                console.log("le mot Nemo a été trouver à la "+word+" position");}
            else{
                console.log ("Je ne trouve pas Nemo. veuillez entrer une phrase avec Nemo");
            }

         /* Exercice 4 : Boum
Des Instructions
Indice : if statement (la leçon de demain)

Demander à l'utilisateur un numéro. En fonction du nombre d'utilisateurs, vous renverrez une chaîne du mot "Boom". Suivez les règles ci-dessous :

Si le nombre donné est inférieur à 2 : renvoie "boum"
Si le nombre donné est supérieur à 2 : la chaîne doit comporter n nombre de "o" (n étant le nombre donné)
Si le nombre donné est divisible par 2, ajoutez un point d'exclamation à la fin.
Si le nombre donné est divisible par 5, renvoyez la chaîne en MAJUSCULES.
Si le nombre donné est divisible à la fois par 2 et 5, renvoyez la chaîne en MAJUSCULES et ajoutez un point d'exclamation à la fin.*/

 //Exercice 4 : Boum
    let numb1 = Number(prompt("Entrez un numéro"));
    let number = "b";
     if (numb1 < 2) {
         number = "boum";
         console.log(number);
     } else {
         for (let i = 1; i <= numb1 ; i++) {
             number=number+"o";
         }
         number=number+"u";
         number=number+"m";
         if ((numb1 % 2) == 0){
             console.log("le nombre est divisible par 2" , number + "!");
         } else if ((numb1 % 5) == 0){
             console.log("le nombre est divisible par 5" , number.toUpperCase() + "!");
         } else if ((numb1 % 5) && (numb1 % 2) == 0){
             console.log("le nombre est divisible par 2 et par 5",number.toUpperCase() + "!");
         } else {
             console.log(number);
         }
     } 