const inputContainer = document.querySelector('#checkbox')
const rootElement = document.documentElement

const darkTheme = {
  '--background-color': '#292943',
  '--main-color': '#7267EF',
  '--dark-color': '#1b1c31',
  '--text-color': '#fff',
}



const lightTheme = {
  '--background-color': '#e2e0fb',
  '--main-color': '#7267EF',
  '--dark-color': '#1b1c31',
  '--text-color': '#000',
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
}

function changeProperty(property, value){
  rootElement.style.setProperty(property, value)
}