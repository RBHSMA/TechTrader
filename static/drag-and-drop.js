const draggables = document.querySelectorAll('.draggable')
const containers = document.querySelectorAll('.container')

// add all necessary eventlisteners to the draggable elements.
draggables.forEach(draggable => {
  draggable.addEventListener('dragstart', () => {
    draggable.classList.add('dragging')
    draggable.querySelector('.number').innerHTML = ""
  }) //when we start dragging the item  add  the class dragging. For styling purposes

  draggable.addEventListener('dragend', () => {
    // elementChildren(containers[0])[0].querySelector('.number').innerHTML = 211
    draggable.classList.remove('dragging')
    //console.log(elementChildren(containers[0])[0].querySelector('.number').innerHTML)
  }) // when we stop dragging, remove the dragging class
})

containers.forEach(container => {
  container.addEventListener('dragover', e => { //the event "dragover" is happening whenever an element is over any container, when not over container, this event stops
    e.preventDefault() // to enable the dropping of elements, otherwise the mouse changes to  "do not allow" symbol. By default dropping inside of an element is disabled 
    const afterElement = getDragAfterElement(container, e.clientY)
    const draggable = document.querySelector('.dragging') // get the currently dragged element, this applies to only one element
    if (afterElement == null) {
      container.appendChild(draggable) // append the dragged element to the container the mouse is inside of if its at the last position
      
    } else {
      container.insertBefore(draggable, afterElement) //otherwise insert the dragged element before the afterElement
      //change the number of the dragged element as well as all following numbers
    }
    numberEach()
  })
})

function postToView(){
  //go through all rules in the container and add only the necessary elements to a json
  var regeln = elementChildren(containers[0])
  regelnJson = []
  regeln.forEach(regel=>{
    var regelChildren = elementChildren(regel)
    regelJson = {
      "id": regelChildren[1].innerHTML,
      "name": regelChildren[2].innerHTML,
      "code": regelChildren[3].innerHTML,
    }
    regelnJson.push(regelJson)
  })
  
  $("#id_regeln").val(JSON.stringify(regelnJson));
}


// goes over each child of each container and gives it the corresponding number it has in the array list
function numberEach(){
  containers.forEach(container =>{
    children = elementChildren(container)
    counter = 1;
    children.forEach(element => {
      element.querySelector('.number').innerHTML=counter;
      counter++;
    })
  })
}
function elementChildren (element) {
  var childNodes = element.childNodes,
      children = [],
      i = childNodes.length;

  while (i--) {
      if (childNodes[i].nodeType == 1) {
          children.unshift(childNodes[i]);
      }
  }

  return children;
}
//this function determines the elementthat is below (after) the mouse cursor
function getDragAfterElement(container, y) { // y is the y position of the mouse
  const draggableElements = [...container.querySelectorAll('.draggable:not(.dragging)')] //determine all the elements inside the container we are hovering over except the element that is being dragged

  return draggableElements.reduce((closest, child) => { //reduce determines the single element that is after the mouse cursor based on the y position
    const box = child.getBoundingClientRect()
    const offset = y - box.top - box.height / 2 //Dinstance between closest element and mouse cursor
    if (offset < 0 && offset > closest.offset) { // if offset negative, it means that were above another element, if positive, we're below the elemenet
      return { offset: offset, element: child }
    } else {
      return closest
    }
  }, { offset: Number.NEGATIVE_INFINITY }).element
}