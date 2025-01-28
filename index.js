const data = [
    [
        { id: 1, name: 'John', age: 28 },
        { id: 2, name: 'Jane', age: 34 }
    ],
    [
        { id: 3, name: 'Bob', age: 22 }
        { id: 4, name: 'Alice', age: 29 }
    ]
];

const names = data.flatMap(innerArray => innerArray.map(person => person.name));

console.log(names); // Output: ['John', 'Jane', 'Bob']