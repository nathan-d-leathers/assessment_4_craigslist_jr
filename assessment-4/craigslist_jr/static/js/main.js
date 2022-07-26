function saveCategory() {
    const name = document.getElementById("newName").value
    const description = document.getElementById("newDescription").value

    axios.post("", {name: name, description: description}).then((response) => {
        window.location.href = "../"
    })
}

function editCategory() {
    const name = document.getElementById("newName").value
    const description = document.getElementById("newDescription").value

    axios.put("", {name: name, description: description}).then((response) => {
        window.location.href = "../../"
    })
}

function deleteCategory() {

    axios.delete("").then((response) => {
        window.location.href = "../../../"
    })
}

function savePost() {
    const title = document.getElementById("newTitle").value
    const description = document.getElementById("newDescription").value
  
    axios.post("", {title: title, description: description}).then((response) => {
        window.location.href = "../../"
    })
}

function editPost() {
    const title = document.getElementById("newTitle").value
    const description = document.getElementById("newDescription").value

    axios.put("", {title: title, description: description}).then((response) => {
        window.location.href = "../../"
    })
}

function deletePost() {

    axios.delete("").then((response) => {
        window.location.href = "../../"
    })
}
