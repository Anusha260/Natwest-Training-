class parentClass{
    country(){
        console.log("india")

    }
    place(){
        console.log("pune")
        
    }
}
class childClass1 extends parentClass{


}
let person1= new parentClass
person1.country()
person1.place()