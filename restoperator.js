// function abc(a,...arg){
//     a.count=0
//     for()
// }

// destructuring/////.......................

// const obj={
//     "name":"anu",
//     "lastname":"nanabala"
// }
// const {name,lastname}=obj
// console.log(name)

// .........object map....obj={
const obj1= {"name":"anu",
    "lastname":"nanabala",
    age:22,
    age:67

}
const data=obj1.filter((item)=>{
    return item.age>=40
})
console.log(data)
    
