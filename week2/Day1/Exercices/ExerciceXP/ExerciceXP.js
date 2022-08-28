    //Exercice1:votre plat prefere
let platPrefere="poulet";
let repasPrefere="diner";
console.log("I eat",platPrefere,"at every",repasPrefere);

                         //Exercice2: Série

    //partieI;

let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = 3;
let myWatchedSeriesSentence = "black mirror, money heist, et the big bang theory.";
console.log( "j\'ai suivie",myWatchedSeriesLength,"series:",myWatchedSeriesSentence);

    //partieII;
myWatchedSeries.splice(2,2,"friends" );
myWatchedSeries.push("Nikita");
myWatchedSeries.unshift("Charmed");
myWatchedSeries.splice(1,1);
console.log(myWatchedSeries[1][2]);
console.log(myWatchedSeries);

                        //Exercice3: Série

let temperature = 37;
let fahrenheit = (((37/5)*9) + 32);
console.log(temperature,"°C est",fahrenheit,"°F");

                        //Exercice4: Série

//1.Quel sera le résultat de a + b dans la première expression ?

        let c;
        let a = 34;
        let b = 21;
        console.log(a+b); //first expression
            // Prediction: le résultat de a+b est 55; car c'est l'addition de deux nombres entiers 34 et 21
            // Actual:55

//2.Quel sera le résultat de a + b dans la seconde expression ?
        a = 2;

        console.log(a+b); //second expression
        // Prediction: le résultat de a+b est 23; car on a affecté un autre chiffre à la variable a =2
        // Actual:23

//3.Quelle est la valeur de c?
        console.log(c); //la valeur de c n'est pas définie

//4.Analysez le code ci-dessous, quel sera le résultat ?
        console.log(3 + 4 + '5');
        /* Prediction: 3 et 4 sont des nombres on peut les additionnés et '5' est considéré comme
         un caractere à cause des guillemet.la console fera le calcul de 3+4 d'abord ensuite il fera une concatenation avec
         le resultat de 3 + 4 = 7 il affichera donc 75*/
        // Actual:75

                        //Exercice5:Devinez Les Réponses #2

    console.log(typeof(15));
    // Prediction: nombre entier
    // Actual:number

    console.log( typeof(5.5));
    // Prediction:nombre décimal
    // Actual:number

    console.log(typeof(NaN));
    // Prediction: une variable
    // Actual:number

   console.log(typeof("hello"));
    // Prediction:chaine de caractere
    // Actual:string

    console.log(typeof(true));
    // Prediction:booléen
    // Actual:boolean

    console.log(typeof(1 != 2));
    // Prediction: vrai car 1 est different de 2
    // Actual:boolean

    console.log("hamburger" + "s");
    // Prediction:hamburgers car c'est une concatenation de caractere;
    // Actual:

        console.log("hamburger" - "s");
    // Prediction:
    // Actual:NaN

    console.log("1" + "3");
    // Prediction:13 c'est considerer comme des caractere à cause des guillemet
    // Actual:13

    console.log("1" - "3");
    // Prediction:
    // Actual: -2

    console.log("johnny" + 5);
    // Prediction:
    // Actual:johnny5

    console.log("johnny" - 5);
    // Prediction:on ne peut pas faire de soustraction entre des nombres et une chaine de caractere
    // Actual:NaN

    console.log(99 * "hello");
    // Prediction:on ne peut pas faire de multiplication entre des nombres et une chaine de caractere
    // Actual:NaN

    console.log(1 != 1);
    // Prediction: non
    // Actual: false

    console.log(1 == "1");
    // Prediction:oui
    // Actual:true

    console.log(1 === "1");
    // Prediction:non
    // Actual:false

                     //Exercice 6 : Devinez Les Réponses #3

    console.log(5 + "34");
    // Prediction:534 c'est une concatenation
    // Actual:534

    console.log(5 - "4");
    // Prediction:1
    // Actual:1

    console.log(10 % 5);
    // Prediction:0 est le reste de la division 
    // Actual:0

    console.log(5 % 10);
    // Prediction:5
    // Actual:5

    console.log("Java" + "Script"); 
    // Prediction:javaScript
    // Actual:javaScript

    console.log(" " + " ");
    // Prediction:rien
    // Actual:rien

    console.log(" " + 0);
    // Prediction:0
    // Actual:0

    console.log(true + true);
    // Prediction: 2 car true est considéré comme 1 en booleen
    // Actual:2

    console.log(true + false);
    // Prediction:1 car true est considéré comme 1 et false est considéré comme 0 en booleen
    // Actual:1

    console.log(false + true);
    // Prediction:0+1=1
    // Actual:1

    console.log(false - true);
    // Prediction:0-1=-1
    // Actual:-1

    console.log(!true);
    // Prediction:
    // Actual:false

    console.log(3 - 4);
    // Prediction:-1
    // Actual:-1

    console.log("Bob" - "bill");
    // Prediction:impossible
    // Actual:NaN
