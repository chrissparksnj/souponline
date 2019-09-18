const serializeMainForm = (form) => {
    // Serializes form data
    var formData = new FormData(form);
    let url = formData.get('url')
    let links_value = formData.get('links')
    let images_value = formData.get('images')
    let text_value = formData.get('text')
    let data = {
        "images": images_value,
        "url": url,
        "links": links_value,
        "text": text_value,
    }
    return data
}


const postMainForm = (data) => {
    // POSTs data to /handler
    let xhr = new XMLHttpRequest()
    xhr.open("POST", "/handler", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            // remove loading bar
            destroyElem("loading_bar")
            handle_json(xhr.responseText)
        }
    }
    // show loading bar
    var loading_props = { "class": "progress is-small is-primary", "max": "100", "id": "loading_bar" }
    appendToId("main_form", createCustomElement("progress", loading_props, "15%"))
    xhr.send(JSON.stringify(data));
}

const createTile = (ancestor_tile, json, color) => {
    let new_div = document.createElement("div")



    Object.values(json).map(val => {
        let li = document.createElement("div");
        li.textContent = val;
        new_div.appendChild(li);}
        )

    // Make class props for tile
    tile_props = {"class":`tile is-4 ${color} is-child notification`}

    // Make new tile
    let tile = createCustomElement("div", tile_props)
    console.log(tile)
    tile.appendChild(new_div)
    // append tile to ancestor (main) tile
    ancestor_tile.appendChild(tile)
}

const handle_json = (json) => {
    var json = JSON.parse(json)
    var json_keys = Object.keys(json)



    // Create main tile
    let tile_props = {"class":"tile is-primary is-ancestor notification"}
    let ancestor_tile = createCustomElement("div", tile_props)

    // Get JSON keys and create a tile for each and append to main tile
    json_keys.map((key, index)=> {
        let colors = ["is-danger", "is-info", "is-success"]
        createTile(ancestor_tile, json[key], colors[index])
    })

    // Append main tile to main-section
    appendSibling("main-section", ancestor_tile)
}

const appendToId = (parent, child) => {
    document.getElementById(parent).appendChild(child)
}

const appendSibling = (parent, sibling) => {
    var par = document.getElementById(parent)
    par.parentNode.insertBefore(sibling, par.nextSibling)
}

const destroyElem = (elemId) => {
    // Destroys element
    var elem = document.getElementById(elemId);
    elem.parentNode.removeChild(elem)

}
const createCustomElement = (typee, attributes = [], text_content = '', html_content = '') => {
    // creates an element with a JSON dictionary for attributes
    obj = document.createElement(typee)
    attr_json = Object.entries(attributes)
    attr_json.map(a => obj.setAttribute(a[0], a[1]))
    obj.textContent = text_content
    obj.innerHtml = html_content
    return obj
}


