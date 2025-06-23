document.getElementById('addButton').addEventListener('click',function(){
    const input = document.getElementById('textInput');
    const text = input.value.trim()

    if(text != '')
    {
        const list = document.getElementById('textList');
        const item = document.createElement('li');
        item.textContent = text;
        item.addEventListener("click",() => {list.removeChild(item);});

        list.appendChild(item);
        input.value='';
    }
})