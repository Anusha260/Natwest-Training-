const input = document.querySelector('.input');

const tableBody= document.querySelector('.tableBody')
let allData = [];
function editName(index){
   let editedText =  prompt("Enter something")
   allData[index].input =editedText
   displayData()
}
function deleteRow(index){
    allData.splice(index,1);
    displayData()
}
//arr=[a,b,c]==> [...arr,d] ==>[a,b,c,d]
function displayData(){
    tableBody.innerHTML="";
    allData.map((item,index)=>{
        tableBody.innerHTML+=`
        <tr>
        <td>${item.input} <button onclick="editName(${index})">edit</button> </td>
    
       <td> <button onclick="deleteRow(${index})">Delete </button> </td>

        </tr>
        `
    })
}
function storeData(){
    allData = [...allData,
        {
            "input": input.value
        }
    ];
    input.value=""
   
    displayData()
}

const submitBtn = document.querySelector('.submitBtn');
submitBtn.addEventListener('click', storeData)
displayData()


