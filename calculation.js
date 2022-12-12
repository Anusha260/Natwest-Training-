const number1=document.querySelector("#input1")
const number2=document.querySelector("#input2")

const data=()=>{
    alert(Number(number1.value)+Number(number2.value))
}
submitbtn.addEventListener("click",data)

