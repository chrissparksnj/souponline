const serializeMainForm = (form) => {

    var formData = new FormData(form);
    let url = formData.get('url')
    let links_value = formData.get('links')
    let images_value = formData.get('images')
    let text_value = formData.get('text')
    let data = {
        "images":images_value, 
        "url": url, 
        "links":links_value, 
        "text":text_value,
    }
    return data
}


const postMainForm = (data) => {
    let xhr = new XMLHttpRequest()
    xhr.open("POST", "/handler", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function(){
        if (xhr.readyState === 4){
            destroyElem("loading_bar")
            console.log(xhr.responseText)
        }

    
        
    }
    var loading_props = {"class":"progress is-small is-primary","max":"100", "id":"loading_bar"}
    document.querySelector('form').appendChild(createCustomElement("progress", loading_props, "15%"))
    xhr.send(JSON.stringify(data));
}

const destroyElem = (elemId) => {
    var elem = document.getElementById(elemId);
    elem.parentNode.removeChild(elem)

}
const createCustomElement = (typee, attributes=[], text_content='') => {
    obj = document.createElement(typee)
    attr_json = Object.entries(attributes)
    attr_json.map(a => obj.setAttribute(a[0], a[1]))
    obj.textContent = text_content
    return obj
}

