
function deleteElement(y){
    let x = document.getElementById(y)
    tasks[y]=``
    x.classList.add('active')
}
document.getElementById("add-button").addEventListener('click', addTask)
let main = document.getElementById('tasks')
let index = 0
let tasks=[]
let peak=[]
let active=[]
function addTask(){
    let current_task = document.getElementById('task').value
    document.getElementById('task').value=''
    if (current_task === '') return
    let htmltask=`
        <div class='lol' id = ${index}>
            <input type="checkbox" class="custom-checkbox ${active[index]}" id="happy${index}" name="happy${index}" onclick="stayon(${index})">
            <label for="happy${index}">${current_task}</label>
            <span onclick="deleteElement(${index})">x</span>
        </div>`
    peak.push(current_task)
    index+=1
    tasks.push(htmltask)
    active.push('')
    show()
}
function show(){
    main.innerHTML = ``
    for (let i =0;i<tasks.length;i++)
    {   
        if(tasks[i].toString().length!=0){
        main.innerHTML+=tasks[i]
        }
    }
}
function stayon(id){
    tasks[id]=`<div class='lol' id = ${id}>
    <input type="checkbox" class="custom-checkbox" id="happy${id}" name="happy${id}" onclick="stayon(${id})" checked='checked'>
    <label for="happy${id}">${peak[id]}</label>
    <span onclick="deleteElement(${id})">x</span>
</div>`
    console.log('lol')
}
