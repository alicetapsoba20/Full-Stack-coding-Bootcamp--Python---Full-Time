/*Des Instructions
Avez-vous entendu la tristement célèbre chanson "99 bouteilles de bière?"
Dans cet exercice, vous devez enregistrer sur console.log les paroles de notre propre chanson 99 Bottles of Beer.

=============================
Exemple
=================== ===========

99 bouteilles de bière au mur
99 bouteilles de bière
Prenez-en 1, passez-la autour de vous
98 bouteilles de bière au mur

98 bouteilles de bière au mur
98 bouteilles de bière
Prenez-en 2, passez-les
96 bouteilles de bière au mur

96 bouteilles de bière au mur
96 bouteilles de bière
Prenez-en 3, passez-les autour de
vous 93 bouteilles de bière au mur

ect…

==============================



Invitez l'utilisateur à entrer un nombre pour commencer à décompter les bouteilles.

Dans la chanson, chaque fois qu'une bouteille tombe,
le nombre soustrait doit augmenter de 1 .
Par exemple,

    We start the song at 99 bottles
    -> Take _1_ down, pass it around
    -> we have now 98 bottles

    -> then, Take _2_ down, pass them around
    -> we have now 96 bottles

    -> then, Take _3_ down, pass them around
    -> we have now 93 bottles

    ... ect


3. La chanson doit se terminer par "0 bouteille de bière sur le mur" ou "pas de bouteille de bière sur le mur".


4. Remarque : Assurez-vous que la grammaire est correcte.

Pour 1 bouteille, vous la faites passer.
Pour plus d'une bouteille, vous les faites passer.
 */

/*******************************1***********************************/
function verifNombre(nombre) {
  type = Number(nombre);
  if (!type) {
    console.log("Désolé, pas un numéro");
    return false;
  }else {
    return true;
  }
}

function entrezNombre() {
  let nombre;
  do {
    nombre = prompt("Entrez un nombre de bouteille pour commencer","99");
  } while (!verifNombre(nombre))
  return nombre;
}

/*********************************************2***************************/
function chant() {
  let nombre=entrezNombre();
  console.log("We start the song at",nombre,"bottles")
  nombre= nombre-1;
  console.log("-> Take _1_ down, pass it around");
  console.log("-> we have now" , nombre , "bottles");
  for ( let i = 2; i < nombre; i++) {
    console.log("-> Take _" + i + "_ down, pass them around");
    console.log("-> we have now" , nombre-i , "bottles");
    nombre = nombre-i;
  }
  console.log("-> Take _" + nombre + "_ down, pass them around");
  console.log("-> we have now 0 bottle");
}

chant();