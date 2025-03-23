const scroll_on_click = (button, position) => {
  button.addEventListener('click', () => {
  window.scrollTo(0, position)
})
}
// const found = (search_container, title, position) => {
//   search_container.innerHTML = ""
//   let p = document.createElement('p')
//   p.innerText = "Film "+title+" found on the list"
//   let scroll_to = document.createElement('button')
//   scroll_to.innerText = "Scroll to film"
//   scroll_to.classList.add("scroll_to")
//   search_container.appendChild(p)
//   search_container.appendChild(scroll_to)
//   scroll_on_click(scroll_to, (position+1)*100) //poprawić działanie doprecyzować 
// }
// const not_found = (search_container, title, film_genre, type) => {
//   search_container.innerHTML = ""
//   let p = document.createElement('p')
//   p.innerText = "Film "+title+" not found on the list"
//   let add = document.createElement('button')
//   add.innerText = "Add Film"
//   search_container.appendChild(p)
//   search_container.appendChild(add)
//   add.addEventListener('click', () => {
//     search_container.innerHTML = ""
//     search_container.classList.remove('active')
//     let title_input = document.getElementsByName('title')[0]
//     let film_genre_input = document.getElementsByName('film_genre')[0]
//     let type_input = document.getElementsByName('type')
//     title_input.value = title
//     film_genre_input.value = film_genre
//     for (let i = 0; i < type_input.length; i++) {
//       if (type_input[i].value == type){
//         type_input[i].checked
//       }
//     }
//     let button = document.querySelector('#search')
//     button.innerText = 'search'
//   })
// }
// const search = (search_container) => {
//   let search_button = document.querySelector('.search_button')
//   search_button.addEventListener('click', () =>{
//     let title = document.getElementsByName("search_title")[0].value.toLowerCase()
//     let film_genre = document.getElementsByName("search_genre")[0].value.toLowerCase()
//     let type = document.getElementsByName("search_type")
//     let type_name = ""
//     for (let i = 0; i < type.length; i++) {
//       if (type[i].checked) {
//         type_name = type[i].value.toLowerCase()
//       }
//     }
//     let container = document.querySelector("#container")
//     let len = container.children.length
//     for (let i = 0; i < len; i++) {
//       if (container.children[i].children[0].children[1].innerText.toLowerCase() == title && container.children[i].children[1].children[1].innerText.toLowerCase() == film_genre && container.children[i].children[3].children[1].innerText.toLowerCase() == type_name){
//         found(search_container, title, i)
//         return
//       }
//     }
//     not_found(search_container, title, film_genre, type)
//   })
// }
// const create_search_container = () => {
//   let active = true
//   let button = document.querySelector('#search')
//   let search_container = document.querySelector('#search_container')
//   button.addEventListener("click", () => {
//     if (active) {
//       active = false
//       button.innerText = "hide"
//       search_container.classList.add("active")
//       let input_placeholder = ["search title", "search film genre"]
//       for (let i = 0; i < input_placeholder.length; i++) {
//         let div = document.createElement("div")
//         div.classList.add("input")
//         let input = document.createElement("input")
//         input.type = "text"
//         input.name = "search_"+input_placeholder[i].split(" ")[i+1]
//         let p = document.createElement("p")
//         p.classList.add("placeholder")
//         p.innerText = input_placeholder[i]
//         div.appendChild(input)
//         div.appendChild(p)
//         search_container.appendChild(div)
//       }
//       let radio_box = document.createElement("div")
//       radio_box.classList.add("radio_box")
//       let type = ["film", "series"]
//       for (let i = 0; i < type.length; i++) {
//         let div_radio = document.createElement("div")
//         div_radio.classList.add("div_radio")
//         let radio_input = document.createElement("input")
//         radio_input.type = "radio"
//         radio_input.name = "search_type"
//         radio_input.value = type[i]
//         let radio_p = document.createElement("p")
//         radio_p.innerText = type[i]
//         div_radio.appendChild(radio_input)
//         div_radio.appendChild(radio_p)
//         radio_box.appendChild(div_radio)
//       }
//       search_container.appendChild(radio_box)
//       let search_button = document.createElement('button')
//       search_button.innerText = 'search'
//       search_button.classList.add('search_button')
//       search_container.appendChild(search_button)
//       search(search_container)
//     }
//     else{
//       active = true
//       button.innerText = "search"
//       search_container.classList.remove("active")
//       search_container.innerHTML = ""
//     }
//   })
// }
// create_search_container()
let scroll_button = document.querySelector('#scroll_button');
scroll_on_click(scroll_button, 0)