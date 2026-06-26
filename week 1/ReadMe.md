# Week 1 – Python Design Patterns and Algorithms

---

## 📖 Overview

This repository contains the solutions for the **Week 1** exercises of the Digital Nurture Python Full Stack Engineer Track. The exercises focus on fundamental software engineering concepts, including **Design Patterns**, **SOLID Principles**, and core **Searching and Sorting Algorithms**.

---

## ✅ Exercises Completed

| Exercise No. | Topic                                    |
| -----------: | ---------------------------------------- |
|            1 | Singleton Design Pattern                 |
|            2 | Factory Method Pattern – Vehicle Factory |
|            3 | SOLID Principles                         |
|            4 | Binary Search Algorithm                  |
|            5 | Merge Sort Algorithm                     |

---

# Exercise 1: Singleton Design Pattern

## Objective

Implement the **Singleton Design Pattern** in Python to ensure that only one instance of a class exists throughout the application.

### Concept

The Singleton Pattern is a creational design pattern that restricts object creation to a single instance while providing a global access point to it.

### Applications

* Database Connection Managers
* Configuration Managers
* Logging Systems
* Cache Management Systems

### Key Learning

* Ensures only one object instance is created.
* Multiple references point to the same object.
* Reduces unnecessary object creation.

---

# Exercise 2: Factory Method Pattern – Vehicle Factory

## Objective

Implement the **Factory Method Design Pattern** to create different types of vehicles without exposing object creation logic to the client.

### Concept

The Factory Method Pattern delegates object creation to a factory class instead of creating objects directly.

### Applications

* Vehicle Manufacturing Systems
* Payment Gateways
* Notification Systems
* Document Generators

### Key Learning

* Centralizes object creation logic.
* Promotes loose coupling.
* Improves extensibility and maintainability.

---

# Exercise 3: SOLID Principles

## Objective

Implement the **SOLID Principles** using a Library Management System.

### Concept

SOLID is a collection of five object-oriented design principles that improve maintainability, scalability, and flexibility.

### Principles Implemented

#### Single Responsibility Principle (SRP)

A class should have only one responsibility and one reason to change.

**Examples**

* Book
* LibraryCatalog
* BookIssueService
* BookReturnService

---

#### Open/Closed Principle (OCP)

Software entities should be open for extension but closed for modification.

**Examples**

* EmailNotification
* SMSNotification
* PushNotification

---

#### Liskov Substitution Principle (LSP)

Objects of a parent class should be replaceable with objects of child classes without affecting correctness.

---

#### Interface Segregation Principle (ISP)

Clients should not be forced to depend on methods they do not use.

**Examples**

* BookSearcher
* BookReporter

---

#### Dependency Inversion Principle (DIP)

High-level modules should depend on abstractions rather than concrete implementations.

**Example**

LibraryManagementService depends on the `Notification` abstraction instead of a concrete notification class.

### Key Learning

* Improves maintainability.
* Encourages loose coupling.
* Makes software easier to extend.
* Promotes clean architecture.

---

# Exercise 4: Binary Search Algorithm

## Objective

Implement the **Binary Search Algorithm** to efficiently search for an element in a sorted array.

### Concept

Binary Search repeatedly divides the search space into two halves until the target element is found.

### Requirements

* Input array must be sorted.

### Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(1)       |
| Average | O(log n)   |
| Worst   | O(log n)   |

### Key Learning

* Faster than Linear Search.
* Efficient for large datasets.
* Widely used in searching applications.

---

# Exercise 5: Merge Sort Algorithm

## Objective

Implement **Merge Sort** using the Divide and Conquer technique.

### Concept

Merge Sort recursively divides an array into smaller subarrays, sorts them, and merges them back into a sorted array.

### Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |

### Space Complexity

| Complexity |
| ---------- |
| O(n)       |

### Key Learning

* Uses the Divide and Conquer strategy.
* Stable sorting algorithm.
* Performs efficiently on large datasets.

---

## 📂 Folder Structure

```text
Week1/
│
├── singleton.py
├── vehicle_factory.py
├── solid_principles.py
├── binary_search.py
├── merge_sort.py
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Design Patterns
* Data Structures and Algorithms
* Visual Studio Code
* Git & GitHub

---

## 🎯 Learning Outcomes

After completing these exercises, I gained practical experience in:

* Creational Design Patterns
* SOLID Principles
* Object-Oriented Design
* Searching Algorithms
* Sorting Algorithms
* Writing Maintainable and Scalable Code
