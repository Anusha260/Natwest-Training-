// class parentClass{
//     constructor(){
//         this.name="anus"
//     }
// }
// class childClass extends parentClass{
//     constructor(Group,fathername){
//         super()
//         this.Group=Group
//         this.fathername=fathername

//     }

// }
// let person1=new childClass("MPC","komurelly")
// console.log(person1)


// another example

class parentClass{
    constructor(firstName,lastName){
        this.firstName=firstName,
        this.lastName=lastName
    }
    display(){
        console.log(`my name is ${this.firstName} ${this.lastName} and I am the GOA age:${22}`)
    }
}
class childClass extends parentClass{
    constructor(firstName,lastName,age,gender){
        super(firstName,lastName)
        this.age=age
        this.gender=gender
    }
}
let person1=new childClass("Anu","nanabala",22,"female")
console.log(person1)
person1.display()