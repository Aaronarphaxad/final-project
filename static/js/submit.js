const submitButton = document.querySelector('.submitButton')
const formData = document.querySelectorAll('.formElem')

submitButton.addEventListener('click', (e)=>{
    
    e.preventDefault()

    fetch('/question-me',
    {
        method:'POST',
        headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body:new formData(formElem.json())
    }).then(response)


})