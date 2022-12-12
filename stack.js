// class Quece{
//     constructor(){
//         this.arr=[]
//     }
//     adding(element){
//         this.arr.push(element)
//     }
//     removing(){
//         this.arr.shift()
//     }
//     top(){
//         console.log(this.arr[0])
//     }
//     isEmpty(){
//         return this.arr.length==0
//     }
// }
// queue=new Queue
// queue.adding(10)
// queue.adding(50)
// console.log(queue)
// queue.top()

class Stack{
    constructor(){
        this.arr=[]
    }
    adding(element){
        this.arr.push(element)
    }
    removing(){
        this.arr.pop()
    }
    
}
stack=new Stack
stack.adding(50)
stack.adding(20)
console.log(stack)
