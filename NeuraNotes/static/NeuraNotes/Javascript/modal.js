const cards = document.querySelectorAll(".note-card")
const modal = document.querySelector("#noteModal")

cards.forEach(card =>{
    card.addEventListener("click", ()=>{
        document.getElementById("modalTitle").innerText = card.dataset.title
        document.getElementById("modalContent").value = card.dataset.content
        modal.style.display = "flex"
        console.log("Modal Clicked")
    })
})

document.querySelector(".close-btn").onclick = function(){
    modal.style.display = "none"
    console.log("Close button clicked")
}

window.addEventListener("click", ()=>{
    modal.style.display = "none"
})
