// Créez une variable appelée sentence. La valeur de la variable doit être une chaîne contenant les mots « not » et « bad ».
// Par exemple, "Le film n'est pas si mal, j'aime bien" .

// Créez une variable appelée wordNotoù sa valeur est la première apparition (c'est-à-dire la position) de la sous-chaîne "not" (de la sentencevariable).

// Créez une variable appelée wordBadoù sa valeur est la première apparition (c'est-à-dire la position) de la sous-chaîne "bad" (de la sentencevariable).

// Si le mot "bad" vient après le mot "not", vous devez remplacer toute la sous-chaîne "not…bad" par "good", puis console.log le résultat.
// Par exemple, le résultat ici devrait être : "Le film est bon, je l'aime"
// Si le mot "bad" ne vient pas après "not" ou si les mots ne sont pas dans la phrase, console.log la phrase originale.
 
 let sentence = prompt("entrer une phrase contenant le mot'not' et 'bad'");
 sentence = sentence.split(" ")
 let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

 if (wordBad > wordNot){
     sentence.splice (wordNot,wordBad-wordNot+1,"good");
     sentence = sentence.join(" ");
     }
  else if (wordBad) 
     {
     	wordBad = sentence.indexOf("bad,");
     	sentence.splice (wordNot,wordBad-wordNot+1,"good,");
    		sentence = sentence.join(" ");	
     }
  else {
 	sentence = sentence.join(" ");}
     console.log(sentence);
