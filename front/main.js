import { users } from './mocks/all-user.js';

function getThresholdValues() {
    const yellowThreshold = parseFloat(document.getElementById('yellow-threshold').value) || 0.3;
    const redThreshold = parseFloat(document.getElementById('red-threshold').value) || 0.5;
    return { yellowThreshold, redThreshold };
}

function getCellClass(value) {
    const { yellowThreshold, redThreshold } = getThresholdValues();

    if (value > redThreshold) {
        return 'red-row';
    } else if (value > yellowThreshold) {
        return 'yellow-row';
    } else {
        return 'green-row';
    }
}

function createTableRow(user) {
    return `
        <tr data-id="${user.id_user}">
            <td>${user.id_user}</td>
            <td>${user.name}</td>
            <td>${user.level}</td>
            <td class="${getCellClass(user.average_coefficient)}">${user.average_coefficient.toFixed(4)}</td>
            <td class="${getCellClass(user.maximum_coefficient)}">${user.maximum_coefficient.toFixed(4)}</td>
            <td class="${getCellClass(user.median_coefficient)}">${user.median_coefficient.toFixed(4)}</td>
        </tr>
    `;
}

function updateTable(data) {
    const tableBody = document.getElementById('user-table-body');
    tableBody.innerHTML = data.map(createTableRow).join('');
    addRowClickListeners();
}

function sortData(criterion) {
    const sortedUsers = [...users].sort((a, b) => b[criterion] - a[criterion]);
    updateTable(sortedUsers);
}

function addRowClickListeners() {
    const rows = document.querySelectorAll('#user-table-body tr');
    rows.forEach(row => {
        row.addEventListener('click', () => {
            const userId = row.getAttribute('data-id');
            window.location.href = `user?id=${userId}`;
        });
    });
}

function setActiveButton(activeId) {
    document.querySelectorAll('.sort-button').forEach(button => {
        button.classList.toggle('active', button.id === activeId);
    });
}

document.getElementById('sort-average').addEventListener('click', () => {
    setActiveButton('sort-average');
    sortData('average_coefficient');
});

document.getElementById('sort-median').addEventListener('click', () => {
    setActiveButton('sort-median');
    sortData('median_coefficient');
});

document.getElementById('sort-maximum').addEventListener('click', () => {
    setActiveButton('sort-maximum');
    sortData('maximum_coefficient');
});

document.getElementById('yellow-threshold').addEventListener('input', () => {
    sortData(document.querySelector('.sort-button.active').id.split('-')[1]);
});

document.getElementById('red-threshold').addEventListener('input', () => {
    sortData(document.querySelector('.sort-button.active').id.split('-')[1]);
});

document.addEventListener('DOMContentLoaded', () => {
    sortData('average_coefficient');
    setActiveButton('sort-average');
});
