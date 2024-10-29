/****************************************************************************************************************/
/* In-Class Exercises                                                                                           */
/****************************************************************************************************************/
/* 1. create an array called "fruits" and assign the values "Strawberry", "Raspberry", and "Apple" to it         */
// add code here
let fruits = ["Strawberry", "Raspberry", "Apple"];
/* 2. add two more fruits to the "fruits" array using the correct array method                                   */
// add code here
console.log(fruits);
fruits.push("Lemon", "Bananna");
/* 3. sort the fruits array alphabetically using the correct array method                                        */
// add code here
fruits.sort();
/* 4. create a function called printFruit that prints each item in the fruits array to the console              */
/*    and call the printFruit function                                                                          */
// add code here
function printFruit() {
    for (let i = 0; i < fruits.length; i++) {
        console.log(fruits[i]);
    }
}
printFruit(); 

/* 5. create a fruit class that has three properties: name, color, and season and one method: printFruit()      */
/*    that prints all three properties of the fruit to the console. Then, create 3 fruit objects and print      */
/*    them using the printFruit() method             
// add code here*/

class Fruit {
    constructor(name, color, season) {
        this.name = name;   
        this.color = color;  
        this.season = season; 
    }
    printFruit() {
        console.log(`Name: ${this.name}, Color: ${this.color}, Season: ${this.season}`);
    }
}
const apple = new Fruit('Apple', 'Red', 'Fall');
const strawberry = new Fruit('Strawberry', 'Red', 'Summer');
const lemon = new Fruit('Lemon', 'Yellow', 'Spring');


apple.printFruit();
strawberry.printFruit();
lemon.printFruit();
/* In-Class Lab                                                                                              */
/****************************************************************************************************************/
/* 1. Write a function that asks the user if they want to say hi. If the user selects "Okay" (true), then       */
/*    display a welcome message. If the user selects "Cancel" (false), then display a different message         */
function areYouSure() {
    const userResponse = confirm("Do you want to say hi?");
    
    if (userResponse) {
        alert("Welcome! It's great to see you!");
    } else {
        alert("If you don't like me you can just say so");
    }
}
areYouSure();

/* 2. Write a function to change 3 styles on the webpage                                                        */
function changeStyle() {

    var button1 = document.getElementById('button1');
    button1.style.backgroundColor = 'yellow';
    var button1 = document.getElementById('button1');
    button1.style.color = 'black';

    var button2 = document.getElementById('button2');
    button2.style.backgroundColor = 'black';
    var button2 = document.getElementById('button2');
    button2.style.color = 'yellow';

    var heading = document.getElementById('welcome');
    heading.style.fontSize = '24px';
    heading.innerText = ('According to all known laws of aviation, there is no way a bee should be able to fly.');
}

