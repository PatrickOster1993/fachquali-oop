// Aufgabe 1: Teilnehmer-Daten definieren

// Enum in JS
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

// Aufgabe 2: Begrüßung mit Template Literals

function begruesseTeilnehmer(teilnehmer) {
  const { name, alter, geschlecht, interessen } = teilnehmer // Object Destructuring
  console.log(
    `Hallo ${name}!\nDu bist ${alter} Jahre alt!\nDein Geschlecht ist ${geschlecht}!\nUnd deine Interessen sind:`
  )
  interessen.forEach((interesse) => {
    console.log(`- ${interesse}`)
  })
}

begruesseTeilnehmer(teilnehmerListe[0]) // testen der Funktion

// Aufgabe 3: Teilnehmer auswerten mit map()
//["Anna (28)", "Ben (31)", ...]

const alleNamenMitAlter = teilnehmerListe.map(
  (tln) => `${tln.name} (${tln.alter})`
)

// zusätzliches Beispiel: map() für 2 Arrays (zur Verknüpfung)
// const alterUndAdresse = [
//   {
//     alter: 21,
//     adresse: "Blabla",
//   },
//   {
//     alter: 27,
//     adresse: "Straße und so",
//   },
// ]

// const nameArray = ["Patrick", "Sven"]

// const neuesArray = alterUndAdresse.map((element, idx) => {
//   const alter = element.alter
//   const adresse = element.adresse
//   const name = nameArray[idx]

//   return {
//     name: name,
//     alter: alter,
//     adresse: adresse,
//   }
// })

// console.log(neuesArray)

console.log(alleNamenMitAlter)

// Aufgabe 4: Teilnehmer filtern mit filter()

// bei geschweiften Klammern MUSS ein return gesetzt werden!
const nurMaennlich = teilnehmerListe.filter((tln) => {
  return tln.geschlecht === gender.m
})

const interessiertSichFuerSport = teilnehmerListe.filter((tln) =>
  tln.interessen.includes("Sport")
)

console.log(nurMaennlich)
console.log(interessiertSichFuerSport)

// Aufgabe 5: Destructuring & Rest-Operator

// Object Destructuring: name u. alter extrahieren + Rest-Operator...

const logSpecificInfosByName = (tlnName) => {
  filteredTeilnehmer = teilnehmerListe.filter((tln) => tln.name === tlnName)
  const { name, alter, ...restInfos } = filteredTeilnehmer[0]
  console.log(`Name: ${name} | Alter: ${alter}`)
  console.log(restInfos)
}

logSpecificInfosByName("Patrick")

// Aufgabe 6: Teilnehmeranalyse mit Funktionen
// Schreibe eine Funktion statistik(teilnehmerArray), die Folgendes berechnet:
// • Durchschnittsalter aller Teilnehmer (map + Rechenoperation)
// • Anzahl Teilnehmer je Geschlecht (m/w/div)
// Gib die Ergebnisse mit einem Template Literal formatiert in der Konsole aus.

function getDurchschnittsalter(tlnListe) {
  //   let sum = 0
  //   for (tln of tlnListe) {
  //     sum += tln.alter
  //   }

  // alternativer Weg über map() und reduce()
  const sum = tlnListe
    .map((tln) => tln.alter)
    .reduce((acc, curr) => acc + curr, 0) // zur Wiederholung
  return sum / tlnListe.length
}

console.log(getDurchschnittsalter(teilnehmerListe)) // testen

function getAnzTlnJeGeschlecht(tlnListe) {
  geschlechterListe = tlnListe.map((tln) => tln.geschlecht)
  // console.log(geschlechterListe)
  const geschlechterZaehler = { m: 0, w: 0, div: 0 }
  geschlechterListe.forEach((geschlecht) => {
    geschlechterZaehler[geschlecht] += 1
  })
  // console.log(geschlechterZaehler)
  return geschlechterZaehler
}

console.log(getAnzTlnJeGeschlecht(teilnehmerListe)) // testen

const statistik = (teilnehmerArray) => {
  geschlechter = getAnzTlnJeGeschlecht(teilnehmerArray)
  durchschnittsalter = getDurchschnittsalter(teilnehmerArray)
  console.log(
    `STATISTIK\n# Durchschnittsalter: ${Math.round(
      durchschnittsalter
    )}\n# Geschlechterverteilung:\n### Männlich: ${
      geschlechter.m
    }\n### Weiblich: ${geschlechter.w}\n### Divers: ${geschlechter.div}`
  )
}

statistik(teilnehmerListe)

// Aufgabe 7: Teilnehmer prüfen (Exception Handling)
// Schreibe eine Funktion pruefeTeilnehmer(teilnehmer), die folgende Bedingungen
// überprüft:
// •name muss ein String sein
// •alter darf nicht kleiner als 0 sein
// •interessen muss ein Array sein
// Falls ein Fehler auftritt, wirf eine Exception mit einer aussagekräftigen Fehlermeldung und
// fange sie mit try/catch ab. Gib im Fehlerfall eine Fehlermeldung aus und setze den
// Teilnehmer nicht auf die Liste

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

pruefeTeilnehmer(teilnehmerListe[0])
