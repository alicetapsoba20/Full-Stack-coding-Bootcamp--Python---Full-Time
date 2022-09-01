            //Exercice1:Instruction If/Else Simple

let x = 22;
let y = 26;
if (x < y){
    console.log("y est plus grand que x");
}
else{
    console.log("x est plus grand que y");
}

                //Exercice 2 : Chihuahua

let newDog ="Chihuahua";
console.log(newDog.length);//le nombre de lettre
console.log(newDog.toUpperCase());//le mot en majuscule
console.log(newDog.toLowerCase());//le mot en minuscule
 if(newDog = "Chihuahua")
        {
    console.log("j\'adore les chihuahuas, c\'est ma race de chien préférée");
        }
else{
    console.log("je m\'en fous, je préfère les chats");
}       
                //Exercice 3 : Pair Ou Impair

let numb = prompt("veuillez saisir un nombre: ");
let num = Number (numb);
    if (num % 2 == 0){
    console.log( +num,"est un nombre pair");
}
    else {
    console.log(+num,"est un nombre impair");
}

                //Exercice 4 : Discussion De Groupe

let users = ["Lea123","Princess45","cat&doglovers", "helooo@000","Alice"];
if(users.length == 1){
    console.log (users[0]," est en ligne"); }
else if(users.length == 2){
    console.log (users[0]+"  et ",users[1]+" sont en ligne"); }
else if(users.length >2){
 let more = users.length -2 ;
 console.log (users[0]+", ",users[1]+" et ",more +" sont en ligne"); }
 else {
    console.log("Personne n\'est en ligne");
 }
