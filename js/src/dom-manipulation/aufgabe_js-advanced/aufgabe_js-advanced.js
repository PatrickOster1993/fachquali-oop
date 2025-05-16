// Aufgabenstellung:
// - Erstellen Sie ein Array mit mehreren Aufgaben (als Object mit den Eigenschaften "text" und "erledigt")
//     z. B. text: "Einkaufen gehen" ... erledigt: false
// - filtern Sie die noch ausstehenden Aufgaben (filter())!
// - geben Sie all diese gefilterten Aufgaben als Text in die Console aus (untereinander -> map(), template literals)
// - Alle möglichen Fehler immer schön abfangen!
function getFilteredElements(tasks, id, element) {
  const outputContainer = document.getElementById(id) // Hier ID korrekt verwenden
  const offeneAufgaben = tasks
    .filter((aufgabe) => !aufgabe.erledigt)
    .map((aufgabe) => {
      const outputElement = document.createElement(element)
      outputElement.textContent = aufgabe.text
      outputContainer.appendChild(outputElement)
      return outputElement
    })
  return offeneAufgaben
}

const aufgaben = [
  { text: "Einkaufen gehen", erledigt: false },
  { text: "Kochen", erledigt: true },
  { text: "Gassi gehen", erledigt: false },
  { text: "Unterrichten", erledigt: false },
  { text: "Mama anrufen", erledigt: true },
]

try {
  getFilteredElements(aufgaben, "loesung1", "h1")
  getFilteredElements(aufgaben, "loesung2", "p")
} catch (error) {
  console.error("Error:", error.message)
}
