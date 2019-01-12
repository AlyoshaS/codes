const { log } = console;

const laboratoryWork = 2;
const semiannualEvaluation = 3;
const finalExam = 5;

// Receber 3 notas e informar a média
const nota_trab = ( arg ) => arg * laboratoryWork;
const aval_sem = ( arg ) => arg * semiannualEvaluation;
const exam = ( arg ) => arg * finalExam;

const checkAverage = ( x, y, z ) => {
    let average = (x, y, z) => (nota_trab(x) + aval_sem(y) + exam(z)) / 10;
}

// function checkArgs(x, y, z) {
//     return arguments.length > 3 ?
//         ? null
//             : z
//             ? (x + y) / z
//             : y
//                 ? (x + y)
//                 :x
//             ? (x)
//             :false

log( checkAverage(1, 2, 3))