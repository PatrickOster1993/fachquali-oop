// Konsolenausgabe:
console.log("### Playground ###")
console.warn("Warnings ausgeben!")
console.error("Fehler ausgeben!")

// Datentypen
//// String
let letName = "Patrick" // Variable (= veränderlich)
var varName = "Patrick" // Variable (= veränderlich)
const constName = "Patrick" // Konstante (= unveränderlich)
//// Number
let x = 5
let y = 7.37 // kein Unterschied zwischen Integer u. Float! Alles als Number gehandhabt!
const PI = 3.14 // Konstante
//// boolean
let active = true // Boolscher Datentyp
//// null & undefined
let nullVariable = null
let undefiniert = undefined

{
  let scopeVariableLet = "letVariable" // Gültigkeit nur innerhalb des Scopes!
  var scopeVariableVar = "varVariable" // auch außerhalb des Scopes zugreifbar!
}

// Exception-Handling
try {
  console.log(scopeVariableLet)
} catch (error) {
  console.error(
    "let-Variable nur innerhalb des Scopes gültig, anonsten Fehler:",
    error.message
  )
}

console.log(scopeVariableVar)

try {
  PI += 5 // Achtung, Konstante!!!
} catch (error) {
  console.error(error)
}

// Typeof
console.log(
  typeof x,
  typeof y,
  typeof letName,
  typeof active,
  typeof undefiniert,
  typeof nullVariable,
  typeof bla, // -> 'undefined', da noch nicht definiert!
  typeof PI
)

// Operatoren
//// klassisch

let a = 2

console.log(x + y) // Addition
console.log(x - y) // Subtraktion
console.log(x * y) // Multiplikation
console.log(x / y) // Division
console.log(x % y) // Modulo
console.log(x ** y) // Potenzierung
console.log(2 ** 3) // 2 hoch 3 = 8
console.log(2 ** 0.5) // Quadratwurzel von 2 = 1.4142135623730951
console.log(2 ** -1) // 1/2 = 0.5
console.log(2 ** -2) // 1/4 = 0.25
console.log(++a) //Pre-Inkrement
console.log(--a) //Pre-Dekrement
console.log(a++) //Post-Inkrement
console.log(a--) //Post-Dekrement
console.log(a)

//// logisch
beideWahr = true && false
einerWahr = true || false

console.log(beideWahr, einerWahr)

active = false

// Bedingungen
//// IF-Statements (best-practice: wenn ich nur 1 alternativen Zweig, also 'else if', benötige)
if (active) {
  // boolscher Vergleich
  console.log("IF-Zweig wahr!")
} else if (2 < 2) {
  // Bedingte Überprüfung mittels Vergleichsoperatoren: ==, <, >, <=, >=, ...
  console.log("ELSE-IF-Zweig wahr (UND IF-Zweig falsch)!")
} else {
  console.log("Kein vorhergehender Zweig wahr!")
}

//////// Beispiel: IF mit Vergleichsoperatoren -> Was wird in der Konsole ausgegeben?
x = 3
y = 6
z = 9

if (x < 10 && y > 10) {
  console.log("Hallo")
} else if (x < 0 || y < 10) {
  if (z == 9) {
    console.log("Welt")
  } else {
    console.log("Nicht-Welt")
  }
} else {
  console.log("Nicht-Hallo")
}

//// Switch-Case (best-practice: wenn ich mehr als 1 alternativen Zweig benötige)
a = 6

switch (a) {
  case 1:
    console.log("a ist 1")
    break
  case 2:
    console.log("a ist 2")
    break
  case 3:
    console.log("a ist 3")
    break
  case 4:
    console.log("a ist 4")
    break
  case 5:
    console.log("a ist 5")
    break
  default:
    console.log("a ist", a)
}

//// Ternärer Operator

a = 4
let name = a > 5 ? "Patrick" : "Nicht-Patrick"

console.log("### Ternärer Operator ###")
console.log(name)

// Scope ohne "Syntax-Konstrukt":
{
  let hallo = "hallo"
}

// Schleifen
//// while (= kopfgesteuert) -> Bedingung bereits zu Beginn überprüft!
console.log("WHILE")
i = 0

while (i < 0) {
  console.log("Schleifendurchlauf:", i)
  i++
}

//// do-while (= fußgesteuert) -> wird immer mind. 1 x ausgeführt (Bedingung erst am Ende überprüft)
console.log("DO-WHILE")
i = 0

do {
  console.log("Schleifendurchlauf:", i)
  i++
} while (i < 0)

//// for
console.log("FOR")

for (n = 5; n > 0; n--) {
  console.log("n =", n)
}

// Arrays
let array1 = [1, 6, 7, 9, 3, 3]
let array2 = [3.4, "hallo", true, undefined] // JS nicht so streng wie statisch typisierte Sprachen (ähnlich wie bei Python)
let array3 = [5, () => console.log("hallo")]

//// for of
for (zahl of array3) {
  console.log(typeof zahl)
}

//// for in
for (index in array3) {
  console.log(typeof index)
}

//// Wichtige Array-Methoden:
array1.push(100) // 100 am Ende des Arrays einfügen
console.log(array1)

array1.pop() // Das letzte Element eines Arrays entfernen
console.log(array1)

array1.shift() // Das erste Element eines Arrays entfernen!
console.log(array1)

array1.unshift(6000)
console.log(array1)

array1.reverse()
console.log(array1)

// Funktionen

//// klassisch
function myFunction(x, y) {
  return x + y
}

console.log("klassische Funktion:", myFunction(3, 5))

myArrayFunction = (x, y) => console.log("Arrow-Funktion:", x + y)

// function matheStuff(operation) {
//   return operation
// }

// addiere = (a, b) => {
//   return a + b
// }
// matheStuff(addiere(a, b))
// matheStuff(() => console.log("Heute keine Operation!"))

// Objects

let person = {
  name: {
    vorname: "Patrick",
    nachname: "Oster",
  },
  alter: {
    echt: 31,
    gelogen: 25,
  },
  lieblingsessen: "Pad Thai",
}

console.log(typeof person)
console.log(person)
console.log("Mein Lieblingsessen:", person.lieblingsessen)
console.log("Mein echtes Alter:", person.alter.echt)

// Ein paar String-Manipulationen / -Methoden:

let myString = "       Hallo DAA!"

console.log(myString.toLowerCase()) // alles in Kleinbuchstaben
console.log(myString.toUpperCase()) // alles in Großbuchstaben

let trimString = myString.trim() // Use-Case: Leerzeichen zu Beginn entfernen (= trimmen)

console.log(trimString)

console.log(myString.includes("DAA")) // Enthält String übergebenen Substring?

let subString = trimString.slice(0, 3) // Subsring von Beginn- und End-Index erstellen!
console.log(subString)

function myReplacementFunc(oldSub, newSub) {
  if (trimString.includes(oldSub)) {
    console.log(trimString.replace(oldSub, newSub))
  } else {
    console.log(trimString)
  }
}

myReplacementFunc("DAA", "Welt")
myReplacementFunc("DOO", "Welt")
myReplacementFunc("Hallo", "Servus")

// Advanced Stuff

//// Set-Datentyp:
let uniqueVals = new Set([1, 2, 3, 3, 2, 1])
console.log(uniqueVals)

//// Symbol-Datentyp:
let id1 = Symbol("id")
let id2 = Symbol("id")

let id3 = "id"
let id4 = "id"

console.log(id1, id2)
console.log(id1 == id2) // false! Symbole sind immer einzigartig!!!
console.log(id3 == id4) // true! Andere Datentypen sind NICHT einzigartig!!!
