# Specification Pattern (car showroom)
Car Showroom Management System using Specification Design Pattern in Python

## Overview
This repository contains a small Python implementation of the Specification Design Pattern, applied to a car showroom management system. The code is designed to provide a flexible and efficient way to filter and manage a collection of cars based on various criteria such as brand, model, year, and mileage.

## Features
- Specification Pattern Implementation: Utilizes the Specification Design Pattern for filtering cars, allowing for easy addition of new specifications.
- Car Types with Polymorphism: Defines different types of cars (ElectricCar, GasCar, PetrolCar) using polymorphism, inheriting from an abstract CarType class.
- Extensible Car Specifications: Includes various specifications like BrandSpecification, ModelSpecification, YearSpecification, and MilageSpecification, which can be combined using logical operations.
- Car Showroom Management: The CarShowroom class serves as a management entity for storing and querying cars using the defined specifications.

## Usage
The Specification Design Pattern is an excellent choice for scenarios where objects need to be selected based on some criteria, and these criteria may be combined by logical operations. It offers a clear separation of selection criteria from the objects being selected, leading to more maintainable and scalable code.