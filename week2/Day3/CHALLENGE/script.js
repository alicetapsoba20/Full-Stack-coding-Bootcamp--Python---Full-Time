/*Des Instructions
Écrivez un programme JavaScript qui recrée le modèle ci-dessous.
Faites ce défi deux fois : d'abord en utilisant une boucle, puis en utilisant deux boucles for imbriquées (imbriquées signifie l'une dans l'autre - consultez ce didacticiel sur les boucles imbriquées ).
Faites ce défi quotidien par vous-même, sans regarder les réponses sur Internet.
*  
* *  
* * *  
* * * *  
* * * * *
* * * * * * */

//MODEL1
let etoile = "*";
for (let i=0; i < 8; i++)
{
  console.log(etoile);
    etoile += "*";
}

//MODEL2
let etoile1 = "*";
let nbrLigne = 6;
for(let i=1; i<nbrLigne; i++){
        console.log(etoile1);
     etoile1+= " * ";
   
}
