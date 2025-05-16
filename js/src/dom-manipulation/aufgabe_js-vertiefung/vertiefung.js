const gender = {
  m: "m",
  w: "w",
  div: "div",
}

const teilnehmerListe = [
  {
    name: "Patrick",
    alter: 31,
    geschlecht: gender.m,
    interessen: ["Sport"],
  },
  {
    name: "Natascha",
    alter: 25,
    geschlecht: gender.w,
    interessen: ["Turnen", "Musik"],
  },
  {
    name: "Sven",
    alter: 43,
    geschlecht: gender.m,
    interessen: ["Fußball", "Netflix"],
  },
  {
    name: "Lisa",
    alter: 36,
    geschlecht: gender.div,
    interessen: ["Schach", "Programmieren", "Sport"],
  },
  {
    name: "Lars",
    alter: 18,
    geschlecht: gender.m,
    interessen: ["Zeichnen"],
  },
  {
    name: "Sabrina",
    alter: 37,
    geschlecht: gender.w,
    interessen: ["Zeichnen", "Kino", "Meditieren"],
  },
]

function pruefeTeilnehmer(teilnehmer) {
  try {
    message = ""
    hasError = false
    nameType = typeof teilnehmer.name
    alterType = typeof teilnehmer.alter
    if (nameType != "string") {
      message += `Name ist vom Typ '${nameType}' | 'string' wird jedoch erwartet!\n`
      hasError = true
    }
    if (alterType != "number") {
      message += `Alter ist vom Typ '${alterType}' | 'number' wird jedoch erwartet!\n`
      hasError = true
    }
    if (!Array.isArray(teilnehmer.interessen)) {
      message += `Interessen ist vom Typ '${typeof teilnehmer.interessen}' | 'array' wird jedoch erwartet!`
      hasError = true
    }
    if (hasError) {
      throw new Error(message)
    }
  } catch (err) {
    console.error(err.message)
  }
}

function renderSteckbrief(teilnehmer) {
  const container = document.getElementById("teilnehmerContainer")

  const steckbrief = document.createElement("div")
  steckbrief.className = "teilnehmer"
  steckbrief.innerHTML = `
            <h3>${teilnehmer.name}</h3>
            <p>Alter: ${teilnehmer.alter}</p>
            <p>Geschlecht: ${teilnehmer.geschlecht}</p>
            <p>Interressen: ${teilnehmer.interessen}</p>
        `
  container.appendChild(steckbrief)
}

// initialer Aufruf (= Mounting)
teilnehmerListe.forEach((tln) => renderSteckbrief(tln))

// alternative Möglichkeit über querySelector:
const form = document.querySelector("#teilnehmerForm")

form.addEventListener("submit", (event) => {
  event.preventDefault()
  const name = document.getElementById("name").value
  const alter = document.getElementById("alter").value
  const geschlecht = document.getElementById("geschlecht").value
  const interessen = document.getElementById("interessen").value

  const neuerTeilnehmer = { name, alter, geschlecht, interessen }
  pruefeTeilnehmer(neuerTeilnehmer)
  teilnehmerListe.push(neuerTeilnehmer)
  renderSteckbrief(neuerTeilnehmer)
  form.reset()
})
