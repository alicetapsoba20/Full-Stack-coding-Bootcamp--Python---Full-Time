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

                //Exercice 3 :trouver Nemo

            let sentence = prompt("Entrer une phrase contenant le mot Nemo");
            