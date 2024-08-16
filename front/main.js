import { users } from './mocks/all-user.js';

function getRowClass(user) {
    const sum = user.average_coefficient + user.maximum_coefficient + user.median_coefficient;

    if (sum > 1.4) {
        return 'red-row';
    } else if (sum > 1.2) {
        return 'yellow-row';
    } else {
        return 'green-row';
    }
}

function createTableRow(user) {
    const rowClass = getRowClass(user);
    return `
        <tr data-id="${user.id_user}" class="${rowClass}">
            <td>${user.id_user}</td>
            <td>${user.name}</td>
            <td>${user.level}</td>
            <td>${user.average_coefficient.toFixed(4)}</td>
            <td>${user.maximum_coefficient.toFixed(4)}</td>
            <td>${user.median_coefficient.toFixed(4)}</td>
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

document.addEventListener('DOMContentLoaded', () => {
    sortData('average_coefficient');
    setActiveButton('sort-average');
});
