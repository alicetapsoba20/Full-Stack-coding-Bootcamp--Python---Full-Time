/*const numbers = [5,0,9,1,7,4,2,6,3,8];

À l'aide de la .toString()méthode, convertissez le tableau en chaîne.
À l'aide de la .join()méthode, convertissez le tableau en chaîne. Essayez de transmettre différentes valeurs dans la jointure.
Par exemple .join("+"), .join(" "), .join("")
Bonus : Pour ce faire, regardez comment travailler avec des boucles for imbriquées
. Triez le numberstableau dans l'ordre décroissant, faites-le en utilisant des boucles for (sans utiliser les méthodes de tri intégrées).
La sortie devrait être : [9,8,7,6,5,4,3,2,1,0]
Astuce : L'algorithme est appelé "Bubble Sort"
Utilisez une variable temporaire pour échanger des valeurs dans le tableau.
Utilisez 2 boucles for "imbriquées" (imbriquées signifie l'une dans l'autre).
Ajoutez des commentaires et console.log le résultat pour chaque étape, cela vous aidera à comprendre.
Exigence : Ne pas copier coller les solutions de Google
 */


                            //DeCroissant

function triDecroissant(arr) {
    //loop forwards through array:
    for (let i = 0; i < arr.length; i++) {
      //loop through the array, moving forwards:
      //note in loop below we set `j = i` so we move on after finding greatest value:
      for (let j = i; j < arr.length; j++) {
        if (arr[i] < arr[j]) {
          let tmp = arr[i]; //store original value for swapping
          arr[i] = arr[j]; //set original value position to greater value
          arr[j] = tmp; //set greater value position to original value
        };
      };
    };
    return arr;
  };
  
  console.log(triDecroissant([10,9,1000,12,-11,3]));
  // sorti//=> [ 1000, 12, 10, 9, 3, -11 ]
  
                            //Croissant
  
  
  function triCroissant(tab) {
    //nombre des éléments dans le tableau
    var len = tab.length;       
    var tmp, i, j;                  
    
    for(i = 1; i < len; i++) {
      //stocker la valeur actuelle 
      tmp = tab[i]
      j = i - 1
      while (j >= 0 && tab[j] > tmp) {
        // déplacer le nombre
        tab[j+1] = tab[j]
        j--
      }
      //Insère la valeur temporaire à la position 
      //correcte dans la partie triée.
      tab[j+1] = tmp
    }
    return tab
  }
  var tab = [5,0,9,1,7,4,2,6,3,8];
  triCroissant(tab);
  console.log(tab);
  
  //sorti//=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]