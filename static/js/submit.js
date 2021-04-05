const submitButton = document.querySelector('.submitButton')
const formData = document.querySelectorAll('.formElem')

submitButton.addEventListener('click', (e)=>{
    
    e.preventDefault()
const submitButton = document.querySelector(".submitButton");
submitButton.addEventListener("click", (e) => {
  //prevent the button from carrying out its default action
  e.preventDefault();
  //get the form elements from the page
  let formElem = document.querySelectorAll(".formElem");

  //loop over the form elements and extract the checked radio values
  let selectedOptions = [];
  for (let forms of formElem) {
    const eachFormElements = forms.elements;
    //save the answers into the list
    selectedOptions.push(eachFormElements.option.value);
  }
  //save it as a json data structure (dictionary)
  dataToSend = {
    answers: selectedOptions,
  };

    fetch('/question-me',
    {
        method:'POST',
        headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body:new formData(formElem.json())
    }).then(response)


})

  fetch("/questions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataToSend),
  }).then(function(result){
    return result.text()
  }).then(function(data){
    const documentReplacement = document.createElement('main')
    documentReplacement.innerHTML = data;
    const oldPage = document.getElementsByTagName('main')[0];
    document.body.replaceChild(documentReplacement,oldPage);
  });
});

