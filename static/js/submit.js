const submitButton = document.querySelector(".submitButton");
submitButton.addEventListener("click", (e) => {
  //prevent the button from carrying ou its default action
  e.preventDefault();
  //get the form elements from th page
  let formElem = document.querySelectorAll(".formElem");

  //loop over the form elements and extract the checked radio values
  let selectedOptions = [];
  for (let forms of formElem) {
    const eachFormElements = forms.elements;
    //save the answers into the list
    selectedOptions.push(eachFormElements.option.value);
  }
  //save it as a json data structure
  dataToSend = {
    answers: selectedOptions,
  };

  fetch("/question-me", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataToSend),
  }).then(result => {
    return result.text()
  }).then(data =>{
    const documentReplacement = document.createElement('main')
    documentReplacement.innerHTML = data;
    const oldPage = document.getElementsByTagName('main')[0];
    console.log(oldPage)
    document.body.replaceChild(documentReplacement,oldPage);
  });
});
