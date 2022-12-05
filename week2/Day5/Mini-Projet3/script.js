/*Créez Un Jeu De Pendu :
Des Instructions:
Créez le jeu « Pendu ». Votre jeu fonctionnera dans la console.
Vous devez deviner un mot caché. Chaque lettre que vous devinez apparaîtra dans la console. Vous avez 10 chances avant de perdre la partie.

Vérifiez le ici

Demander au joueur 1 un mot. Le mot doit avoir un minimum de 8 lettres. Présentez le mot dans la console avec des étoiles ( ********).
À ce stade, demandez continuellement au joueur 2 d'écrire une lettre.
Si la lettre se trouve dans le mot choisi par le joueur 1 , affichez à nouveau le mot en étoiles mais avec la bonne lettre ( *****t**).
Si la lettre apparaît plusieurs fois dans le mot, assurez-vous qu'elle est visible aux bons endroits lorsque vous affichez les étoiles avec les suppositions correctes ( ***t**t*).
Si le joueur 2 devine mal 10 fois, affichez un message dans la console indiquant YOU LOSE.
Afficher une liste de toutes les suppositions après chaque tour. Dans votre code, empêchez le joueur 2 de deviner deux fois la même lettre.
Si le joueur 1 gagne, affichez un message indiquant CONGRATS YOU WIN.
 */

/*************************************1****************************/

function verifTaille(mot) {
    if (mot.length < 8)
        return false;
    else
        return true;
}

function entrezMot(){
    let mot;
    do{
        mot = prompt("Entrez un mot de 8 lettres minimum"); 
    } while (!verifTaille(mot))
    return mot;
}


/*********************************2**************************************/

function verifLettre(lettre) {
    if (lettre.length != 1)
        return false;
    else
        return true;
}

function entrezLettre() {
    let lettre;
    do {
        lettre = prompt("Entrez une lettre");
    } while(!verifLettre(lettre))
    return lettre;
}

function verif(mot,mot1,lettre) {
    let mot2 = "";
    for(let i = 0; i < mot.length; i++){
        if ( mot[i] == lettre && lettre != mot1[i]) {
            mot2 += mot[i];
        } else {
            mot2 += mot1[i];
        }
    }
    return mot2;
}

function timeOut(mot1,mot2) {
    if (mot1 == mot2)
        return false;
    else {
        return true;
    }
}



function jeuPendu() {
    let mot = entrezMot();
    let mot1 = "*".repeat(mot.length);
    console.log(mot1);
    let error = 0;
    do {
        let lettre = entrezLettre();
        let mot2 = verif(mot,mot1,lettre);
        if (timeOut(mot1,mot2)){
            mot1 = mot2;
            console.log(mot1);;
        } else {
            error += 1;
            console.log("Try again");
        }
        
        if (mot1 == mot) {
            console.log("CONGRATS YOU WIN")
            return;
        }
        if (error == 10)
            console.log("YOU LOSE");
    } while( error < 10)
}

jeuPendu();