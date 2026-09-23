# JavaScript - Objects, Scopes and Closures

![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=for-the-badge&logo=javascript&logoColor=black)
![NodeJS](https://img.shields.io/badge/Node.js-14.x-green?style=for-the-badge&logo=node.js&logoColor=white)
![Code Style](https://img.shields.io/badge/code%20style-semistandard-brightgreen?style=for-the-badge)

## 📌 Project Overview
This directory contains JavaScript projects exploring **Object-Oriented Programming (OOP)** in JavaScript, variable scoping, inheritance, closures, and custom modules. The exercises focus on creating and extending ES6 classes, managing object state, manipulating arrays without built-in methods, and building lexical closures.

All scripts adhere strictly to the `semistandard` style guide.

---

## 🛠️ Core Concepts Covered
* **Class Syntax & Construction:** Defining ES6 `class` structures, handling initialization logic, and managing empty objects.
* **Inheritance:** Extending classes using `extends` and calling parent constructors with `super()`.
* **Instance Methods:** Creating utility methods for rotation, scaling, and character-based grid rendering.
* **Closures:** Encapsulating state across function invocations and dynamic base conversion utilities.
* **Module Exports:** Exporting functions and classes for consumption via `require()`.

---

## 📂 File Breakdown & Project Tasks

| File | Description |
| :--- | :--- |
| `0-rectangle.js` | Defines an empty `Rectangle` class. |
| `1-rectangle.js` | `Rectangle` class with constructor taking `w` (width) and `h` (height). |
| `2-rectangle.js` | `Rectangle` class that creates an empty object if `w` or `h` is $\le 0$ or not an integer. |
| `3-rectangle.js` | Adds a `print()` method to `Rectangle` to render the shape using `X`. |
| `4-rectangle.js` | Adds `rotate()` and `double()` methods to `Rectangle`. |
| `5-square.js` | Defines a `Square` class that inherits from `Rectangle` of `4-rectangle.js`. |
| `6-square.js` | Extends `Square` with a `charPrint(c)` method to print using a specified character. |
| `7-occurrences.js` | Function that counts and returns element occurrences in a list. |
| `8-esrever.js` | Function that returns a reversed array without using `.reverse()`. |
| `9-logme.js` | Function that tracks and prints call counts along with the argument value using closures. |
| `10-converter.js` | Function returning a closure that converts numbers between dynamic bases. |

---

## 💻 Setup & Execution

### Prerequisites
Ensure Node.js and `semistandard` are installed:
```bash
node -v
npm install -g semistandard
