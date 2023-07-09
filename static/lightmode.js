const inputContainer = document.querySelector('.checkbox')
const rootElement = document.documentElement

window.onload = getThemeFromLocalStorage


const darkTheme = {
  '--main-color': '#d0435a',
  '--background-color': '#0D0A17',
  '--dark-color': '#0D0A17',
  '--text-color': '#EEEEEE',
}



const lightTheme = {
  '--background-color': '#e2e0fb',
  '--main-color': '#7267EF',
  '--dark-color': '#1b1c31',
  '--text-color': '#262626',
}



inputContainer.addEventListener('change', function(){
  const isChecked = inputContainer.checked
  isChecked ? changeTheme(darkTheme) : changeTheme (lightTheme)
})

function changeTheme(theme){
    //Alteraçao do tema
  for (let prop in theme){
    changeProperty(prop, theme[prop])
  }
  saveThemeToLocalStorage(theme)

}

function changeProperty(property, value){
  rootElement.style.setProperty(property, value)
}

function saveThemeToLocalStorage(theme){
  localStorage.setItem('theme', JSON.stringify(theme)) // CONVERTE OBJETO EM JSON

}

function getThemeFromLocalStorage(){
  const theme = JSON.parse(localStorage.getItem('theme') ) //CONVERTE JSON STRING EM OBJETO
  changeTheme(theme)
}

