const input=document.querySelector("#input1")
const input1=document.querySelector("#input2")



const add=()=>{
    alert(Number(input.value)+Number(input1.value))
}
submit1.addEventListener("click",add)
const substraction=()=>{
    alert(Number(input.value)-Number(input1.value))
}
submit2.addEventListener("click",substraction)

const multiplication=()=>{
    alert(Number(input.value)*Number(input1.value))
}
submit3.addEventListener("click",multiplication)
const divid=()=>{
    alert(Number(input.value)/Number(input1.value))
}
submit4.addEventListener("click",divid)

