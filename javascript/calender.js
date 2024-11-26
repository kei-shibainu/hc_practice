const { argv } = require('process');

function getYearMonth() {
    const now = new Date();
    const year = now.getFullYear();
    let month = now.getMonth() + 1;

    if (argv.length > 2 && argv[2] === '-m' && argv[3]) {
        const inputMonth = parseInt(argv[3], 10);
        if (isNaN(inputMonth) || inputMonth < 1 || inputMonth > 12) {
            console.error(`${argv[3]} is neither a month number (1..12) nor a name`);
            process.exit(1);
        }
        month = inputMonth;
    }
    
    return { year, month };
}

function printHeader(year, month) {
    const monthOfYear = `${month}月 ${year}`.padStart(12, ' ').padEnd(12, ' ');
    console.log(monthOfYear);
    const weeks = "月 火 水 木 金 土 日";
    console.log(weeks);
}

function printBody(year, month) {
    const firstDay = new Date(year, month - 1, 1);
    const lastDay = new Date(year, month, 0);

    const startDay = firstDay.getDay();

    const blanks = Array(startDay).fill('  ');

    let days = [];
    for (let i = 1; i <= lastDay.getDate(); i++) {
        days.push(i.toString().padStart(2, ' '));
    }

    let daysOfMonth = [...blanks, ...days];
    for (let i = 0; i < daysOfMonth.length; i += 7) {
        const week = daysOfMonth.slice(i, i + 7).join(' ');
        console.log(week);
    }
}

function run() {
    const { year, month } = getYearMonth();
    printHeader(year, month);
    printBody(year, month);
}

run();