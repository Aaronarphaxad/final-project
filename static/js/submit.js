const submitButton = document.querySelector('.submitButton')
const formData = document.querySelectorAll('.formElem')

submitButton.addEventListener('click', (e)=>{
    
  e.preventDefault()
  
  //loop over the form elements and extract the checked radio values
  let selectedOptions = [];
  let correctOptions =[]
  for (let forms of formData) {
    const eachFormElements = forms.elements;
    correctOptions.push(eachFormElements.option[4].value);
    //save the answers into the list
    selectedOptions.push(eachFormElements.option.value);
  }
  //save it as a json data structure (dictionary)
  dataToSend = {
    answers: selectedOptions,
    correct: correctOptions
  };

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

